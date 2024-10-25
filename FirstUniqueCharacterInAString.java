import java.util.LinkedHashMap;
import java.util.Map;

class Solution {
    public static int firstUniqChar(String s) {

        Map<Character, Integer> pairs = new LinkedHashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (pairs.containsKey(s.charAt(i))) {
                pairs.put(s.charAt(i), pairs.get(s.charAt(i)) + 1);
            } else {
                pairs.put(s.charAt(i), 1);
            }
        }

        for (int i = 0; i < s.length(); i++) {
            if (pairs.get(s.charAt(i)) == 1) {
                return i;
            }
        }

        return -1;
    }

}