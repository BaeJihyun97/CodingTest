class Solution {
    
    static int count;
    
    boolean purmute(char[] chars, StringBuffer sb, String answer, boolean flag, int depth) {
        if (flag || answer.equals(sb.toString())) {
            return true;
        }
        else if (depth >= 5) {
            return false;
        }
        
        
        for (char c:chars) {
            sb.append(c);
            count += 1;
            if (answer.equals(sb.toString())) {
                flag = true;
                return true;
            }
            else {
                if(purmute(chars, sb, answer, flag, depth+1)) {
                    flag = true;
                    return true;
                }
            }
            sb.deleteCharAt(sb.length() -1);
        }
        
        return false;
    }
    
    public int solution(String word) {
        int answer = 0;
        count = 0;
        purmute(new char[] {'A', 'E', 'I', 'O', 'U'}, new StringBuffer(), word, false, 0);
        return count;
    }
}