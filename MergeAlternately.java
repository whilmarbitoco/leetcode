import java.util.Arrays;;

class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        char[] w1 = word1.toCharArray();
        char[] w2 = word2.toCharArray();

        int i = 0;
        int j = 0;

        while (j < w1.length && j < w2.length) {

            sb.append(w1[i]);
            sb.append(w2[j]);

            i++;
            j++;
        }

        sb.append(copy(w1, i));

        sb.append(copy(w2, j));

        return sb.toString();
    }

    public String copy(char[] w1, int i) {
        StringBuilder res = new StringBuilder();

        w1 = Arrays.copyOfRange(w1, i, w1.length);

        for (int j = 0; j < w1.length; j++) {
            res.append(w1[j]);
        }

        return res.toString();
    }
}