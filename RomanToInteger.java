public class Solution {

    public int romanToInt(String roman) {
        HashMap<Character, Integer> pairs = new HashMap<>();
        pairs.put('I', 1);
        pairs.put('V', 5);
        pairs.put('X', 10);
        pairs.put('L', 50);
        pairs.put('C', 100);
        pairs.put('D', 500);
        pairs.put('M', 1000);

        int result = 0;

        char[] romanChar = roman.toCharArray();

        for (int i = 0; i < romanChar.length; i++) {
          int value = pairs.get(romanChar[i]);
            if (i + 1 < romanChar.length && value < pairs.get(romanChar[i + 1])) {
                result -= value;
            } else {
                result += value;
            }
        }
        return result;
    }


}