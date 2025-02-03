 #java_solution_for_11_container_with_most_water
class Solution {

    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int maxArea = 0;
        int maxLen = 0;
        while(left<right){
            maxLen = Math.min(height[left], height[right])*(right-left);
            maxArea=Math.max(maxArea,maxLen);
            if(height[left]<height[right]) left++;
            else right--;
        }

        return maxArea;


    }
}
