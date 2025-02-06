class Solution {
    public int trap(int[] height) {
        int vol = 0;
        int leftmax = height[0], rightmax = height[height.length - 1];
        int left = 0, right = height.length - 1;

        while (left < right) {
            if (height[left] <= height[right]) {
                if (height[left] <= leftmax) {
                    vol += (leftmax - height[left]);
                } else {
                    leftmax = height[left];
                }
                left++;
            } else {
                if (height[right] <= rightmax) {
                    vol += (rightmax - height[right]);
                } else {
                    rightmax = height[right];
                }
                right--;
            }
        }

        return vol;
    }
}
