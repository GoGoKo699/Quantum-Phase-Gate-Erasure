"""Exact finite checks for the phase-gate program and its charge profiles."""

from fractions import Fraction
from itertools import combinations, product
from math import comb
from unittest import TestCase


def convolve(left, right):
    counts = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            counts[i + j] += left_value * right_value
    return tuple(counts)


def block_weights(length, block_count):
    counts = (1,)
    for _ in range(block_count):
        counts = convolve(counts, (1,) * (length + 1))
    return tuple(Fraction(count, (length + 1) ** block_count) for count in counts)


def independent_probe_weights(probabilities):
    weights = (1,)
    for probability in probabilities:
        weights = convolve(weights, (1 - probability, probability))
    return weights


def window_overlap(weights, data_width):
    return sum(
        min(weights[start : start + data_width + 1])
        for start in range(len(weights) - data_width)
    )


def largest_window_mass(weights, width):
    if width >= len(weights):
        return sum(weights)
    return max(
        sum(weights[start : start + width])
        for start in range(len(weights) - width + 1)
    )


def translated_total_variation(weights, displacement):
    zeros = (0,) * displacement
    return Fraction(
        sum(abs(left - right) for left, right in zip(weights + zeros, zeros + weights)),
        2,
    )


def kept_block_count(blocks, erased_sites):
    return sum(block.isdisjoint(erased_sites) for block in blocks)


class ChargeProfileTests(TestCase):
    def test_convolved_uniform_profiles(self):
        for length, count in product(range(1, 11), range(1, 8)):
            weights = block_weights(length, count)
            self.assertEqual(sum(weights), 1)
            self.assertEqual(weights, weights[::-1])
            for width in range(1, len(weights) + 2):
                with self.subTest(length=length, count=count, width=width):
                    failure = 1 - window_overlap(weights, width)
                    self.assertEqual(failure, largest_window_mass(weights, width))
                    self.assertEqual(failure, translated_total_variation(weights, width))

    def test_gapped_profiles_only_guarantee_an_inequality(self):
        weights = (Fraction(2, 5), 0, Fraction(1, 5), 0, Fraction(2, 5))
        self.assertEqual(window_overlap(weights, 1), 0)
        self.assertEqual(largest_window_mass(weights, 1), Fraction(2, 5))
        for width in range(1, 7):
            failure = 1 - window_overlap(weights, width)
            variation = translated_total_variation(weights, width)
            self.assertGreaterEqual(failure, variation)
            self.assertGreaterEqual(variation, largest_window_mass(weights, width))

    def test_lossless_and_full_loss_endpoints(self):
        for query_count in range(1, 15):
            for width in range(1, query_count + 3):
                self.assertEqual(
                    window_overlap(block_weights(query_count, 1), width),
                    max(0, 1 - Fraction(width, query_count + 1)),
                )
        self.assertEqual(window_overlap((1,), 1), 0)

    def test_full_product_support_gives_positive_success_up_to_survivor_count(self):
        for survivors in range(13):
            weights = independent_probe_weights([Fraction(1, 2)] * survivors)
            for width in range(1, survivors + 3):
                self.assertEqual(window_overlap(weights, width) > 0, width <= survivors)


class DecoderTests(TestCase):
    def test_success_branches_preserve_joint_data_reference_coherence(self):
        # Omit the common program normalization. All branch amplitudes then
        # use rational numbers, and phase factors are tracked by their powers.
        program_amplitudes = (1, 2, 3, 2, 2, 1)
        total_weight = sum(amplitude**2 for amplitude in program_amplitudes)
        joint_data = {
            ("00", 0): 1,
            ("00", 1): 2,
            ("01", 1): -1,
            ("10", 0): 2,
            ("11", 0): 3,
            ("11", 1): -2,
        }
        data_basis = ("00", "01", "10", "11")
        width = 2
        column_norms = {}
        success_weight = 0

        for label in range(len(program_amplitudes) - width):
            minimum = min(program_amplitudes[label : label + width + 1])
            success_weight += minimum**2
            kraus_entries = {}
            for data in data_basis:
                charge = label + data.count("1")
                scale = Fraction(minimum, program_amplitudes[charge])
                column = (data, charge)
                kraus_entries[column] = (data, scale)
                column_norms[column] = column_norms.get(column, 0) + scale**2
            self.assertEqual(len({output for output, _ in kraus_entries.values()}), 4)

            actual = {}
            for (data, reference), data_amplitude in joint_data.items():
                for charge, program_amplitude in enumerate(program_amplitudes):
                    entry = kraus_entries.get((data, charge))
                    if entry is None:
                        continue
                    output_data, filter_amplitude = entry
                    actual[output_data, reference, charge] = (
                        data_amplitude * program_amplitude * filter_amplitude
                    )
            expected = {
                (data, reference, label + data.count("1")): minimum * amplitude
                for (data, reference), amplitude in joint_data.items()
            }
            self.assertEqual(actual, expected)

        self.assertTrue(all(norm <= 1 for norm in column_norms.values()))
        weights = tuple(Fraction(value**2, total_weight) for value in program_amplitudes)
        self.assertEqual(Fraction(success_weight, total_weight), window_overlap(weights, width))


class ErasedChargeConverseTests(TestCase):
    def test_hypergeometric_estimator_mean_squared_error(self):
        for query_count in range(2, 9):
            for erased_count in range(1, query_count + 1):
                masks = tuple(combinations(range(query_count), erased_count))
                for charge in range(query_count + 1):
                    squared_errors = []
                    for mask in masks:
                        erased_charge = sum(site < charge for site in mask)
                        estimate = Fraction(query_count * erased_charge, erased_count)
                        squared_errors.append((estimate - charge) ** 2)
                    expected = Fraction(
                        charge * (query_count - charge) * (query_count - erased_count),
                        erased_count * (query_count - 1),
                    )
                    self.assertEqual(sum(squared_errors) / len(masks), expected)

    def test_posterior_charge_variance_for_an_asymmetric_probe(self):
        strings = ("00000", "11000", "00001", "11101", "10110")
        probabilities = tuple(Fraction(weight, 15) for weight in (2, 1, 3, 5, 4))
        query_count = 5
        for erased_count in range(1, query_count + 1):
            masks = tuple(combinations(range(query_count), erased_count))
            posterior_variance = 0
            estimator_error = 0
            for mask in masks:
                groups = {}
                for string, probability in zip(strings, probabilities):
                    erased_bits = tuple(string[site] for site in mask)
                    groups.setdefault(erased_bits, []).append((string.count("1"), probability))
                for erased_bits, conditional_terms in groups.items():
                    mass = sum(probability for _, probability in conditional_terms)
                    posterior_mean = sum(
                        charge * probability for charge, probability in conditional_terms
                    ) / mass
                    estimate = Fraction(query_count * erased_bits.count("1"), erased_count)
                    posterior_variance += sum(
                        (charge - posterior_mean) ** 2 * probability
                        for charge, probability in conditional_terms
                    )
                    estimator_error += sum(
                        (charge - estimate) ** 2 * probability
                        for charge, probability in conditional_terms
                    )
            worst_input_bound = Fraction(
                query_count**2 * (query_count - erased_count),
                4 * erased_count * (query_count - 1),
            )
            self.assertLessEqual(posterior_variance, estimator_error)
            self.assertLessEqual(estimator_error / len(masks), worst_input_bound)


class FlaggedErasureTests(TestCase):
    def test_every_one_site_loss_in_the_ten_query_benchmark(self):
        blocks = (set(range(5)), set(range(5, 10)))
        for erased_site in range(10):
            with self.subTest(erased_site=erased_site):
                kept = kept_block_count(blocks, {erased_site})
                self.assertEqual(kept, 1)
                self.assertEqual(window_overlap(block_weights(5, kept), 2), Fraction(2, 3))

    def test_two_erased_sites_can_touch_at_most_two_blocks(self):
        blocks = tuple(set(range(start, start + 2)) for start in range(0, 10, 2))
        by_kept_count = {
            kept: window_overlap(block_weights(2, kept), 2) for kept in (3, 4, 5)
        }
        results = []
        for erased_sites in combinations(range(13), 2):
            kept = kept_block_count(blocks, erased_sites)
            self.assertGreaterEqual(kept, 3)
            results.append(by_kept_count[kept])
        self.assertEqual(min(results), 1 - Fraction(6 + 7, 27))

    def test_product_baseline_uses_the_fair_coin_fourier_bound(self):
        failure_bound = Fraction(comb(18, 9) + comb(18, 10), 4**9)
        self.assertEqual(1 - failure_bound, Fraction(84883, 131072))
        self.assertLess(1 - failure_bound, Fraction(2, 3))

        profiles = (
            [Fraction(1, 2)] * 9,
            [Fraction(i, 10) for i in range(1, 10)],
            [Fraction(1, 100)] * 9,
            [0, 1, Fraction(1, 3)] * 3,
        )
        for probabilities in profiles:
            weights = independent_probe_weights(probabilities)
            collision_term = sum(weight**2 for weight in weights)
            adjacent_term = sum(left * right for left, right in zip(weights, weights[1:]))
            self.assertGreaterEqual(collision_term + adjacent_term, failure_bound)
            self.assertGreaterEqual(largest_window_mass(weights, 2), collision_term + adjacent_term)
            self.assertLessEqual(window_overlap(weights, 2), 1 - failure_bound)
