class TwoSum {
    public int[] twoSum(int[] list, int target) {
        for (int j = 0; j < list.length - 1; j++) {
            for (int k = list.length - 1; k >= 0; k--) {
                int value = list[j] + list[k];

                if (value == target && j != k) {
                    return new int[] { k, j };
                }

            }

        }

        return null;
    }
}