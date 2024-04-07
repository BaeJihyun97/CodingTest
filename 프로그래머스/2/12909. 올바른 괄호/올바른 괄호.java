class Solution {
    boolean solution(String s) {
        boolean answer = true;

        int left = 0;
        for (char sc: s.toCharArray()) {
            if (sc == '(') {
                left += 1;
            }
            else {
                left -= 1;
            }
            
            if (left < 0) {
                answer = false;
                break;
            }
        }
        
        if (left != 0) answer = false;

        return answer;
    }
}