class Solution {
    public String clearDigits(String s) {
        Stack<Character> stk = new Stack<>();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (Character.isDigit(s.charAt(i)) && stk.size() >= 1) {
                stk.pop();
                continue;
            } else {
                stk.push(s.charAt(i));
            }
            System.out.println(stk);
        }
        StringBuilder res = new StringBuilder();
        while (!stk.isEmpty()) {
            res.insert(0, stk.pop());
        }
        return res.toString();
    }
}
