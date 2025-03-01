class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length - 1;
        int i = 0;
        while (i < n) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
            i++;
        }
        int[] res = new int[n + 1];
        int j = 0;
        for (i = 0; i <= n; i++) {
            if (nums[i] != 0) {
                res[j] = nums[i];
                j++;
            }
        }
        return res;
    }
}
