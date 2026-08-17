#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <tuple>
#include <vector>

namespace {

constexpr int kWords = 4;
using Mask = std::array<std::uint64_t, kWords>;
using Speeds = std::array<int, 4>;
using Relation = std::array<int, 4>;

std::vector<std::pair<int, int>> test_times() {
  std::vector<std::pair<int, int>> times;
  for (int denominator = 2; static_cast<int>(times.size()) < 64 * kWords;
       ++denominator) {
    for (int numerator = 1; numerator * 2 <= denominator; ++numerator) {
      if (std::gcd(numerator, denominator) != 1) continue;
      times.emplace_back(numerator, denominator);
      if (static_cast<int>(times.size()) == 64 * kWords) break;
    }
  }
  return times;
}

bool safe_at(int speed, int numerator, int denominator) {
  const int residue = static_cast<int>(
      (static_cast<long long>(speed) * numerator) % denominator);
  const int distance = std::min(residue, denominator - residue);
  return 9 * distance > 2 * denominator;
}

std::vector<Mask> speed_masks(int bound) {
  const auto times = test_times();
  std::vector<Mask> masks(bound + 1);
  for (int speed = 1; speed <= bound; ++speed) {
    masks[speed].fill(0);
    for (int index = 0; index < static_cast<int>(times.size()); ++index) {
      if (safe_at(speed, times[index].first, times[index].second)) {
        masks[speed][index / 64] |= std::uint64_t{1} << (index % 64);
      }
    }
  }
  return masks;
}

bool has_grid_witness(const Speeds& speeds, const std::vector<Mask>& masks) {
  for (int word = 0; word < kWords; ++word) {
    if (masks[speeds[0]][word] & masks[speeds[1]][word] &
        masks[speeds[2]][word] & masks[speeds[3]][word]) {
      return true;
    }
  }
  return false;
}

bool has_exact_first_band_witness(const Speeds& speeds) {
  for (int first = 0; first < 4; ++first) {
    for (int second = first; second < 4; ++second) {
      const int denominator = speeds[first] + speeds[second];
      for (int numerator = 1; numerator * 2 <= denominator; ++numerator) {
        bool safe = true;
        for (const int speed : speeds) {
          const int residue = static_cast<int>(
              (static_cast<long long>(numerator) * speed) % denominator);
          const int distance = std::min(residue, denominator - residue);
          if (9 * distance <= 2 * denominator) {
            safe = false;
            break;
          }
        }
        if (safe) return true;
      }
    }
  }
  return false;
}

Relation primitive_relation(Relation relation) {
  int divisor = 0;
  for (const int entry : relation) divisor = std::gcd(divisor, std::abs(entry));
  for (int& entry : relation) entry /= divisor;
  const auto first = std::find_if(
      relation.begin(), relation.end(), [](int entry) { return entry != 0; });
  if (*first < 0) {
    for (int& entry : relation) entry = -entry;
  }
  return relation;
}

bool proportional(const Relation& first, const Relation& second) {
  int pivot = 0;
  while (pivot < 4 && first[pivot] == 0 && second[pivot] == 0) ++pivot;
  if (pivot == 4 || first[pivot] == 0 || second[pivot] == 0) return false;
  for (int index = 0; index < 4; ++index) {
    if (first[index] * second[pivot] != second[index] * first[pivot]) return false;
  }
  return true;
}

int coefficient_two_relation_rank_at_least_two(const Speeds& speeds) {
  bool found = false;
  Relation basis{};
  for (int a = -2; a <= 2; ++a) {
    for (int b = -2; b <= 2; ++b) {
      for (int c = -2; c <= 2; ++c) {
        for (int d = -2; d <= 2; ++d) {
          if (a == 0 && b == 0 && c == 0 && d == 0) continue;
          Relation relation{a, b, c, d};
          long long dot = 0;
          for (int index = 0; index < 4; ++index) {
            dot += static_cast<long long>(relation[index]) * speeds[index];
          }
          if (dot != 0) continue;
          relation = primitive_relation(relation);
          if (!found) {
            basis = relation;
            found = true;
          } else if (!proportional(basis, relation)) {
            return 2;
          }
        }
      }
    }
  }
  return found ? 1 : 0;
}

bool pairwise_gcd_at_most_two(const Speeds& speeds) {
  for (int first = 0; first < 4; ++first) {
    for (int second = first + 1; second < 4; ++second) {
      if (std::gcd(speeds[first], speeds[second]) > 2) return false;
    }
  }
  return true;
}

}  // namespace

int main(int argc, char** argv) {
  if (argc != 4) {
    std::cerr << "usage: verify_h33_n4 SUM_BOUND SHARD_INDEX SHARD_COUNT\n";
    return 2;
  }
  const int bound = std::stoi(argv[1]);
  const int shard = std::stoi(argv[2]);
  const int shard_count = std::stoi(argv[3]);
  if (bound < 10 || shard_count < 1 || shard < 0 || shard >= shard_count) {
    throw std::invalid_argument("invalid bound or shard");
  }

  const auto masks = speed_masks(bound);
  std::uint64_t enumerated = 0;
  std::uint64_t grid_rejected = 0;
  std::uint64_t nonprimitive = 0;
  std::uint64_t gcd_excluded = 0;
  std::uint64_t exact_rejected = 0;
  std::uint64_t first_band = 0;
  std::uint64_t rank_failures = 0;

  for (int first = 1; first < bound; ++first) {
    if ((first - 1) % shard_count != shard) continue;
    for (int second = first + 1; second < bound; ++second) {
      for (int third = second + 1; third < bound; ++third) {
        const int last = bound - first - second - third;
        if (last <= third) break;
        for (int fourth = third + 1; fourth <= last; ++fourth) {
          const Speeds speeds{first, second, third, fourth};
          ++enumerated;
          if (has_grid_witness(speeds, masks)) {
            ++grid_rejected;
            continue;
          }
          if (std::gcd(std::gcd(first, second), std::gcd(third, fourth)) != 1) {
            ++nonprimitive;
            continue;
          }
          if (!pairwise_gcd_at_most_two(speeds)) {
            ++gcd_excluded;
            continue;
          }
          if (has_exact_first_band_witness(speeds)) {
            ++exact_rejected;
            continue;
          }
          ++first_band;
          const int rank = coefficient_two_relation_rank_at_least_two(speeds);
          std::cout << "SURVIVOR " << first << ',' << second << ',' << third << ','
                    << fourth << " rank=" << rank << '\n';
          if (rank < 2) {
            ++rank_failures;
            std::cout << "COUNTEREXAMPLE " << first << ',' << second << ',' << third
                      << ',' << fourth << " rank=" << rank << '\n';
          }
        }
      }
    }
  }

  std::cout << "VERIFIED bound=" << bound << " shard=" << shard << '/'
            << shard_count << " enumerated=" << enumerated
            << " grid_rejected=" << grid_rejected
            << " nonprimitive=" << nonprimitive << " gcd_excluded=" << gcd_excluded
            << " exact_rejected=" << exact_rejected << " first_band=" << first_band
            << " rank_failures=" << rank_failures << '\n';
  return rank_failures == 0 ? 0 : 1;
}
