import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        int length = phone_book.length;
        Arrays.sort(phone_book); 
        
        int prev_length = phone_book[0].length(), cur_length = 0;
        for(int i=1; i<length; i++) {    
            cur_length = phone_book[i].length();
            if (prev_length < cur_length && phone_book[i-1].equals(phone_book[i].substring(0, prev_length))) {
                answer = false;
                break;
            }
            prev_length = cur_length;
        }
        
        
        return answer;
    }
}