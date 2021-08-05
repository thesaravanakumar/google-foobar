import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class Solution {

    private static int solution(String n, int b) {
        int k = getK(n);
        List<String> visitedNumbers = new ArrayList<>();
        // Simply iterates through the values.
        while (!visitedNumbers.contains(n)) {
            visitedNumbers.add(n);
            String x = getX(n, k);
            String y = getY(x);
            Integer z = Integer.valueOf(x, b) - Integer.valueOf(y, b);

            // Continues with the next value.
            n = zeroPad(z, b, k);
        }

        // The ending cycle length is equal to the number of values computed minus the first occurrence of the value found twice.
        return visitedNumbers.size() - visitedNumbers.indexOf(n);
    }

    private static int getK(String n) {
        // K is the length of the number n.
        return n.length();
    }

    private static String getX(String n, int k) {
        // X is the number n with it's digits sorted in descending order.
        return n.chars()
            .mapToObj(c -> (char) c)
            .sorted(Comparator.reverseOrder())
            .map(Objects::toString)
            .collect(Collectors.joining());
    }

    private static String getY(String x) {
        // Y is the x number in reverse order.
        return new StringBuilder(x).reverse()
            .toString();
    }

    // Add leading 0 to the given n number of base b until it reaches the desired length.
    private static String zeroPad(int n, int b, int length) {
        String nToString = Integer.toString(n, b);
        return String.format("%" + length + "s", nToString)
            .replace(' ', '0');
    }

    public static void main(String... args) {
        int bOne = 10, outputOne = 1;
        String nOne = "1211";
        int bTwo = 3, outputTwo = 3;
        String nTwo = "210022";

        assert solution(nOne, bOne) == outputOne;
        assert solution(nTwo, bTwo) == outputTwo;
    }

}