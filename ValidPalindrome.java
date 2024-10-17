class ValidPalindrome {

    public boolean isPalindrome(String s) {
        String[] tmp = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "").split("");
        String original = "";
        String reverse = "";

        for (int j = 0; j < tmp.length; j++) {
            original += tmp[j];

        }

        for (int i = tmp.length - 1; i >= 0; i--) {
            reverse += tmp[i];
        }

        System.out.println(reverse + " " + original);

        return original.equalsIgnoreCase(reverse) ? true : false;

    }
}