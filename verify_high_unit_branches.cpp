#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

namespace {

constexpr int k = 8;
constexpr int max_p = 233;
constexpr int max_limit = (k + 1) * max_p / 2;
constexpr int mask_words = (max_limit + 63) / 64;
int selected_p = 47;
int selected_modulus = (k + 1) * selected_p;
int selected_limit = selected_modulus / 2;

struct Mask {
  std::array<std::uint64_t, mask_words> word{};

  bool empty() const {
    return std::all_of(word.begin(), word.end(), [](auto x) { return x == 0; });
  }
  int count() const {
    return std::accumulate(word.begin(), word.end(), 0,
                           [](int n, auto x) { return n + std::popcount(x); });
  }
};

Mask operator|(const Mask& left, const Mask& right) {
  Mask result;
  for (int i = 0; i < mask_words; ++i) result.word[i] = left.word[i] | right.word[i];
  return result;
}

Mask subtract(const Mask& left, const Mask& covered) {
  Mask result;
  for (int i = 0; i < mask_words; ++i) result.word[i] = left.word[i] & ~covered.word[i];
  return result;
}

bool subset_of(const Mask& part, const Mask& whole) {
  for (int i = 0; i < mask_words; ++i) {
    if ((part.word[i] & ~whole.word[i]) != 0) return false;
  }
  return true;
}

void set_bit(Mask& mask, int index) {
  mask.word[index / 64] |= std::uint64_t{1} << (index % 64);
}

bool covers(int speed, int time) {
  const int residue = static_cast<int>(
      (static_cast<std::int64_t>(time) * speed) % selected_modulus);
  const int distance = std::min(residue, selected_modulus - residue);
  return distance * (k + 1) < selected_modulus;
}

Mask coverage_mask(int speed) {
  Mask result;
  for (int time = 1; time <= selected_limit; ++time) {
    if (covers(speed, time)) set_bit(result, time - 1);
  }
  return result;
}

struct State {
  Mask residual;
  int slots;

  bool operator==(const State& other) const {
    return slots == other.slots && residual.word == other.residual.word;
  }
};

struct StateHash {
  std::size_t operator()(const State& state) const {
    std::size_t value = static_cast<std::size_t>(state.slots);
    for (auto word : state.residual.word) {
      value ^= std::hash<std::uint64_t>{}(word) + 0x9e3779b97f4a7c15ULL +
               (value << 6) + (value >> 2);
    }
    return value;
  }
};

class UnitCompletion {
 public:
  explicit UnitCompletion(std::vector<int> speeds) : speeds_(std::move(speeds)) {
    for (int speed : speeds_) masks_.push_back(coverage_mask(speed));
    coverers_.resize(selected_limit);
    for (int point = 0; point < selected_limit; ++point) {
      for (int index = 0; index < static_cast<int>(masks_.size()); ++index) {
        if ((masks_[index].word[point / 64] >> (point % 64)) & 1) {
          coverers_[point].push_back(index);
        }
      }
    }
    point_order_.resize(selected_limit);
    std::iota(point_order_.begin(), point_order_.end(), 0);
    std::sort(point_order_.begin(), point_order_.end(), [&](int left, int right) {
      return coverers_[left].size() < coverers_[right].size();
    });
  }

  bool can_cover(const Mask& residual, int slots) {
    failed_.clear();
    return search(residual, slots);
  }

  std::size_t failed_states() const { return failed_.size(); }

 private:
  bool search(const Mask& residual, int slots) {
    if (residual.empty()) return true;
    if (slots == 0) return false;
    State state{residual, slots};
    if (failed_.contains(state)) return false;

    int max_gain = 0;
    for (const auto& mask : masks_) {
      int gain = 0;
      for (int i = 0; i < mask_words; ++i) {
        gain += std::popcount(residual.word[i] & mask.word[i]);
      }
      max_gain = std::max(max_gain, gain);
    }
    if (max_gain == 0 || residual.count() > slots * max_gain) {
      failed_.insert(state);
      return false;
    }

    if (slots == 1) {
      for (const auto& mask : masks_) {
        if (subset_of(residual, mask)) return true;
      }
      failed_.insert(state);
      return false;
    }

    // A set can cover at most one point from a collection whose coverer sets
    // are pairwise disjoint. This greedy packing is a sound lower bound.
    std::array<std::uint64_t, mask_words> used_coverers{};
    int packed = 0;
    for (int point : point_order_) {
      if (((residual.word[point / 64] >> (point % 64)) & 1) == 0) continue;
      bool disjoint = true;
      for (int index : coverers_[point]) {
        if ((used_coverers[index / 64] >> (index % 64)) & 1) {
          disjoint = false;
          break;
        }
      }
      if (!disjoint) continue;
      ++packed;
      if (packed > slots) {
        failed_.insert(state);
        return false;
      }
      for (int index : coverers_[point]) {
        used_coverers[index / 64] |= std::uint64_t{1} << (index % 64);
      }
    }

    int pivot = -1;
    for (int point : point_order_) {
      if ((residual.word[point / 64] >> (point % 64)) & 1) {
        pivot = point;
        break;
      }
    }
    std::vector<std::pair<int, int>> choices;
    for (int index : coverers_[pivot]) {
      int gain = 0;
      for (int i = 0; i < mask_words; ++i) {
        gain += std::popcount(residual.word[i] & masks_[index].word[i]);
      }
      choices.emplace_back(-gain, index);
    }
    std::sort(choices.begin(), choices.end());
    for (const auto& [negative_gain, index] : choices) {
      (void)negative_gain;
      if (search(subtract(residual, masks_[index]), slots - 1)) return true;
    }
    failed_.insert(state);
    return false;
  }

  std::vector<int> speeds_;
  std::vector<Mask> masks_;
  std::vector<std::vector<int>> coverers_;
  std::vector<int> point_order_;
  std::unordered_set<State, StateHash> failed_;
};

}  // namespace

int main(int argc, char** argv) {
  if (argc < 3 || argc > 4) {
    std::cerr << "usage: verify_high_unit_branches <p> <4|5|6|7> [unit|g9]\n";
    return 2;
  }
  selected_p = std::stoi(argv[1]);
  selected_modulus = (k + 1) * selected_p;
  selected_limit = selected_modulus / 2;
  if (selected_p < 5 || selected_p > max_p || std::gcd(selected_p, 3) != 1) {
    std::cerr << "p must satisfy 5 <= p <= " << max_p << " and gcd(p,3)=1\n";
    return 2;
  }
  const int unit_count = std::stoi(argv[2]);
  if (unit_count < 4 || unit_count > 7) {
    std::cerr << "only branches 4 through 7 are supported\n";
    return 2;
  }
  const std::string normalization = argc == 4 ? argv[3] : "unit";
  if (normalization != "unit" && normalization != "g9") {
    std::cerr << "normalization must be unit or g9\n";
    return 2;
  }
  const bool normalize_g9 = normalization == "g9";

  std::vector<int> units;
  std::vector<int> nonunits;
  for (int speed = 1; speed <= selected_limit; ++speed) {
    if (speed % selected_p == 0) continue;
    if (std::gcd(speed, 9) == 1) {
      if (normalize_g9 || speed != 1) units.push_back(speed);
    } else {
      if (!normalize_g9 || speed != 9) nonunits.push_back(speed);
    }
  }

  Mask universe;
  for (int point = 0; point < selected_limit; ++point) set_bit(universe, point);
  const Mask base_coverage = coverage_mask(normalize_g9 ? 9 : 1);
  UnitCompletion completion(units);
  const int nonunit_count = (normalize_g9 ? 7 : 8) - unit_count;
  const int remaining_units = unit_count - (normalize_g9 ? 0 : 1);
  std::uint64_t checked = 0;

  std::vector<Mask> nonunit_masks;
  std::vector<Mask> active_fibers;
  for (int speed : nonunits) {
    nonunit_masks.push_back(coverage_mask(speed));
    Mask fibers;
    for (int residue = 1; residue < selected_p; ++residue) {
      bool active = false;
      for (int phase = 0; phase < 9; ++phase) {
        active = active || covers(speed, residue + phase * selected_p);
      }
      if (active) set_bit(fibers, residue - 1);
    }
    active_fibers.push_back(fibers);
  }
  Mask all_nonzero_fibers;
  for (int residue = 1; residue < selected_p; ++residue) {
    set_bit(all_nonzero_fibers, residue - 1);
  }
  Mask base_fibers;
  if (normalize_g9) {
    for (int residue = 1; residue < selected_p; ++residue) {
      bool active = false;
      for (int phase = 0; phase < 9; ++phase) {
        active = active || covers(9, residue + phase * selected_p);
      }
      if (active) set_bit(base_fibers, residue - 1);
    }
  }
  std::vector<int> chosen;
  bool found_counterexample = false;
  const std::uint64_t progress_interval = unit_count <= 5 ? 10000 : 100;

  std::function<void(int, int, bool, Mask, Mask)> enumerate =
      [&](int start, int left, bool has_g9, Mask covered,
          Mask fibers) {
        if (found_counterexample) return;
        if (left == 0) {
          if (!has_g9) return;
          // Four unit edges cannot cover nine phases unaided. Thus the u=4
          // branch needs some nonunit activity on every nonzero fiber.
          if (unit_count == 4 && fibers.word != all_nonzero_fibers.word) return;
          const Mask residual = subtract(universe, covered);
          ++checked;
          if (completion.can_cover(residual, remaining_units)) {
            std::cout << "COUNTEREXAMPLE branch=" << unit_count << " nonunit=";
            for (int index = 0; index < static_cast<int>(chosen.size()); ++index) {
              if (index) std::cout << ',';
              std::cout << nonunits[chosen[index]];
            }
            std::cout << '\n';
            found_counterexample = true;
            return;
          }
          if (checked % progress_interval == 0) {
            std::cout << "progress branch=" << unit_count << " checked=" << checked
                      << " failed_states=" << completion.failed_states() << '\n';
          }
          return;
        }
        const int final = static_cast<int>(nonunits.size()) - left;
        for (int index = start; index <= final; ++index) {
          chosen.push_back(index);
          enumerate(index + 1, left - 1,
                    has_g9 || std::gcd(nonunits[index], 9) == 9,
                    covered | nonunit_masks[index], fibers | active_fibers[index]);
          chosen.pop_back();
          if (found_counterexample) return;
        }
      };

  enumerate(0, nonunit_count, normalize_g9, base_coverage, base_fibers);
  if (found_counterexample) return 1;

  std::cout << "VERIFIED branch=" << unit_count << " checked=" << checked
            << " normalization=" << normalization << '\n';
  return 0;
}
