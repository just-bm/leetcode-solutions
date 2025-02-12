class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        int ln = flowerbed.length;

        for (int i = 0; i < ln; i++) {
            if (flowerbed[i] == 0) {
                boolean left = (i == 0 || flowerbed[i - 1] == 0);
                boolean right = (i == ln - 1 || flowerbed[i + 1] == 0);

                if (left && right) {
                    flowerbed[i] = 1;
                    count++;
                    if (count >= n) {
                        return true;
                    }
                }
            }
        }

        return count >= n;
    }
}
