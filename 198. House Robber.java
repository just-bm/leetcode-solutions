class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n <= 2) {
            return Math.max(nums[0], n > 1 ? nums[1] : 0);
        }
        int[] dp = new int[n];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[1], nums[(0)]);
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i - 1], nums[(i)] + dp[i - 2]);
        }
        // System.out.println(Arrays.toString(dp));
        return Math.max(dp[n - 1], dp[n - 2]);
    }
}
