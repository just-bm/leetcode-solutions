class Solution {
    public String reverseVowels(String s) {
        List<Character> vowel = new ArrayList<>();
        char[] check = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        
        for (char i : s.toCharArray()) {
            for (char c : check) {
                if (i == c) {
                    vowel.add(i);
                    break;
                }
            }
        }
        
        StringBuilder res = new StringBuilder();
        
        for (char i : s.toCharArray()) {
            boolean isVowel = false;
            for (char c : check) {
                if (i == c) {
                    isVowel = true;
                    break;
                }
            }
            if (isVowel && vowel.size() > 0) {
                res.append(vowel.remove(vowel.size() - 1));
                continue;
            }
            res.append(i);
        }
        return res.toString();
    }
}
