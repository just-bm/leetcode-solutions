class Solution {
    public int maxAscendingSum(int[] nums) {
        int sum = 0;
        int j = 0;
        int maxsum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] > nums[i - 1]) {
                sum += nums[i];
            } else {
                maxsum = Math.max(sum, maxsum);
                sum = nums[i];
            }
        }
        maxsum = Math.max(sum, maxsum);
        return maxsum;
    }
}
