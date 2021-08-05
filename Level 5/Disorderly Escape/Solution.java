import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

public class Solution {

	public static String solution(int w, int h, int s) {
		// We start by calculating the single cycles indexes.
		List<CycleIndexMonomial> cycleIndexW = buildCycleIndex(w);
		List<CycleIndexMonomial> cycleIndexH = buildCycleIndex(h);

		// Now we can calculate the cycle index product.
		List<CycleIndexMonomial> cycleIndexProduct = new ArrayList<>();
		for (CycleIndexMonomial a : cycleIndexW) {
			for (CycleIndexMonomial b : cycleIndexH) {
				cycleIndexProduct.add(a.multiply(b));
			}
		}

		// Finally we can apply Burnside's theorem.
		BigInteger gCardinality = factorial(BigInteger.valueOf(w)).multiply(factorial(BigInteger.valueOf(h)));
		BigInteger phi = cycleIndexProduct.stream().map(m -> m.solve(BigInteger.valueOf(s))).reduce(BigInteger.ZERO,
				BigInteger::add);
		return phi.divide(gCardinality).toString();
	}

	// Builds the cycle index from the partitions of a given n
	// (https://en.wikipedia.org/wiki/Cycle_index).
	private static List<CycleIndexMonomial> buildCycleIndex(int n) {
		List<CycleIndexMonomial> cycleIndex = new ArrayList<>();

		// Starts by building a list of integer partitions.
		List<List<Integer>> partitions = new ArrayList<>();
		fillIntegerPartitions(n, n, new ArrayList<Integer>(), partitions);

		// We get the exponents and the coefficient for each partition and we add it to
		// the cycle index.
		for (List<Integer> currentPartition : partitions) {
			int[] partitionExponents = partitionExponents(currentPartition, n);
			BigInteger coefficient = partitionCoefficient(currentPartition, partitionExponents, n);
			cycleIndex.add(new CycleIndexMonomial(coefficient, partitionExponents));
		}

		return cycleIndex;
	}

	private static BigInteger partitionCoefficient(List<Integer> partition, int[] partitionExponents,
			int partitionedInteger) {
		// First, gets the number of circular (e.g. equivalent) dispositions available
		// for each element of the given partition. We want to get the product since
		// we're considering all the available combinations of elements.
		BigInteger coefficient = BigInteger.ONE;
		for (Integer cycleSize : partition) {
			coefficient = coefficient.multiply(
					countCircularDispositions(BigInteger.valueOf(partitionedInteger), BigInteger.valueOf(cycleSize)));

			// For the next cycle, we'll consider only the elements not already used in
			// this one.
			partitionedInteger -= cycleSize;
		}

		// Finally, we want to divide our coefficient by the product of the factorial
		// exponents. This is to remove the combinations that contains the same cycles
		// but in different order (which are the same), for example (1)(2)(3)(4) and
		// (1)(3)(4)(2).
		BigInteger exponentsFactorialProduct = IntStream.of(partitionExponents).mapToObj(BigInteger::valueOf)
				.map(Solution::factorial).reduce(BigInteger.ONE, BigInteger::multiply);
		return coefficient.divide(exponentsFactorialProduct);
	}

	// This formula is derived from circular permutations
	// (https://en.wikipedia.org/wiki/Permutation#Circular_permutations). Since
	// permutations are a special case of dispositions with k == n, we simply divide
	// the total dispositions by k.
	private static BigInteger countCircularDispositions(BigInteger n, BigInteger k) {
		return factorial(n).divide(factorial(n.subtract(k))).divide(k);
	}

	private static BigInteger factorial(BigInteger n) {
		if (n.compareTo(BigInteger.ONE) < 1) {
			return BigInteger.ONE;
		}
		return n.multiply(factorial(n.subtract(BigInteger.ONE)));
	}

	// Returns all the integer partitions of a number n.
	private static void fillIntegerPartitions(int n, int max, List<Integer> currentPartition,
			List<List<Integer>> allPartitions) {
		// Partition is done, add it to the list.
		if (n == 0) {
			allPartitions.add(currentPartition);
			return;
		}

		// Recursively computes all the partitions.
		for (int i = Math.min(max, n); i >= 1; i--) {
			List<Integer> clonedCurrentPartition = new ArrayList<>(currentPartition);
			clonedCurrentPartition.add(i);
			fillIntegerPartitions(n - i, i, clonedCurrentPartition, allPartitions);
		}
	}

	// Returns an array of exponents for the given partition.
	private static int[] partitionExponents(List<Integer> partitions, int partitionedInteger) {
		return IntStream.range(0, partitionedInteger).map(i -> Collections.frequency(partitions, i + 1)).toArray();
	}

	private static class CycleIndexMonomial {
		private BigInteger coefficient;
		private int[] powers;

		private CycleIndexMonomial(BigInteger coefficient, int[] powers) {
			this.coefficient = coefficient;
			this.powers = powers;
		}

		// Replaces the variables with the given value and returns the result.
		public BigInteger solve(BigInteger value) {
			int powersSum = IntStream.of(powers).sum();
			return coefficient.multiply(value.pow(powersSum));
		}

		// Taken from here:
		// https://www.sciencedirect.com/science/article/pii/0012365X9390015L
		public CycleIndexMonomial multiply(CycleIndexMonomial other) {
			int u = powers.length;
			int v = other.powers.length;
			CycleIndexMonomial result = new CycleIndexMonomial(coefficient.multiply(other.coefficient), new int[u * v]);
			for (int l = 0; l < u; l++) {
				for (int m = 0; m < v; m++) {
					result.powers[lcm(l + 1, m + 1) - 1] += powers[l] * other.powers[m] * gcd(l + 1, m + 1);
				}
			}
			return result;
		}

		// Greatest common divisor
		private int gcd(int a, int b) {
			if (b == 0)
				return Math.abs(a);
			return gcd(b, a % b);
		}

		// Least common multiplier
		private int lcm(int a, int b) {
			return a * b / (gcd(a, b));
		}
	}

	public static void main(String... args) {
		int wOne = 2, hOne = 3, sOne = 4;
		String outputOne = "430";
		int wTwo = 2, hTwo = 2, sTwo = 2;
		String outputTwo = "7";

		assert solution(wOne, hOne, sOne).equals(outputOne);
		assert solution(wTwo, hTwo, sTwo).equals(outputTwo);
	}
}