class Solution {
    public int maxSum(int[] nums) {
         HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        int[] uniqueNums = new int[set.size()];
        int index = 0;
        for (int num : set) {
            uniqueNums[index++] = num;
        }

        int[] greater = new int[uniqueNums.length];
        int[] lesser = new int[uniqueNums.length];
        int greaterCount = 0;
        int lesserCount = 0;

        for (int i : uniqueNums) {
            if (i <= 0) {
                lesser[lesserCount++] = i;
            } else {
                greater[greaterCount++] = i;
            }
        }

        int sumGreater = 0;
        for (int i = 0; i < greaterCount; i++) {
            sumGreater += greater[i];
        }

        if (sumGreater == 0) {
            int maxLesser = lesser[0];
            for (int i = 1; i < lesserCount; i++) {
                if (lesser[i] > maxLesser) {
                    maxLesser = lesser[i];
                }
            }
            return maxLesser;
        } else {
            return sumGreater;
        }
    }
}
