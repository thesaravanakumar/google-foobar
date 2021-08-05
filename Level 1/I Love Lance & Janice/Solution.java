import java.util.Objects;
import java.util.stream.Collectors;

public class Solution {

    public static String solution(String encryptedText) {
        return encryptedText.chars()
            // Decodes the current character.
            .map(c -> (c >= 'a' && c <= 'z') ? ('a' + 'z' - c) : c)
            // Converts the mapped character from an integer.
            .mapToObj(c -> (char) c)
            .map(Objects::toString)
            .collect(Collectors.joining());
    }

    public static void main(String... args) {
        String inputOne = "wrw blf hvv ozhg mrtsg’h vkrhlwv?";
        String inputTwo = "Yvzs! I xzm’g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!";
        String outputOne = "did you see last night’s episode?";
        String outputTwo = "Yeah! I can’t believe Lance lost his job at the colony!!";

        assert solution(inputOne).equals(outputOne);
        assert solution(inputTwo).equals(outputTwo);
    }

}