class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> mp = new HashMap<>();
        HashSet<Integer> s = new HashSet<>();

        // Count occurrences of each number
        for (int i : arr) {
            mp.put(i, mp.getOrDefault(i, 0) + 1);
        }

        // Check if occurrences are unique
        for (int freq : mp.values()) {
            if (!s.add(freq)) { // If frequency is already in the set, return false
                return false;
            }
        }
        
        return true;
    }
}
