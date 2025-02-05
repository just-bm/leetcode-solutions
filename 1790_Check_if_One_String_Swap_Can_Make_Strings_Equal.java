class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if (s1.equals(s2)) {
            return true;
        }

        int n = s1.length();
        Stack<Integer> stk = new Stack<>();
        for (int i = 0; i < n; i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                stk.push(i);
            }
            if (stk.size() > 2) {
                return false;
            }
        }
        if (stk.size() == 2) {
            int first = stk.pop();
            int second = stk.pop();
            return s1.charAt(first) == s2.charAt(second) && s1.charAt(second) == s2.charAt(first);
        }

        return false;

    }
}
