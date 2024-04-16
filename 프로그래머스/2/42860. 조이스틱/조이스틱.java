import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(String name) {
        int answer = 0;
        char[] nameChar = name.toCharArray(); 
        boolean[] As = new boolean[name.length()];
        
        
        for (int i=0; i < name.length(); i++) {
            As[i] = nameChar[i] == 'A' ;
            answer += Math.min(nameChar[i] - 'A', 26 - (nameChar[i] - 'A'));
        }
        
        // 가장 긴 A 열 찾기
        int count = 0, start = 0, end = 0, currs = 0, curre = 0, firste=0, lasts=name.length();
        boolean flag = false, flag2=true;
        for (int i=0; i < name.length(); i++) {
            if (As[i]) {
                if (!flag) {
                    flag = true;
                    currs = i; curre = i;
                }
                else {curre += 1;}
                
            }
            else if (flag) {
                if (count < curre - currs + 1) {
                    start = currs; end = curre;
                }
                flag = false;
                count = Math.max(count, curre - currs + 1);
            }
        }
        if (flag && count < curre - currs + 1) { // 마지막 정리
            start = currs; end = curre;
            count = curre - currs + 1;
            
        }
        
        // 만일 처음과 끝이 모두 A 일 경우
        if (As[0] && As[As.length-1]) {
            firste = 0;
            while (firste+1 < As.length && As[firste+1]) firste++;
            
            lasts=name.length()-1;
            while (lasts-1 > 0 && As[lasts-1]) lasts--;
        }
        
        
        // System.out.printf("%d, %d, ", count, answer);
        
        //A가 없으면
        if (count == 0) {
            answer += name.length() - 1;
        }
        else if (count < name.length()) {
            int rleft = Math.max(0, (start - 1))*2 + (name.length() - end - 1); // -> <-
            int lright = (name.length() - end - 1)*2 + Math.max(0, (start - 1)); // <- ->
            int right = Math.max(0, lasts-1); // ->
            int left = name.length() - firste - 1; // <-
            
            // System.out.printf("%d, %d", left, right);
            
            answer += Collections.min(Arrays.asList(rleft, lright, right, left, name.length() - 1));
        }
        
        
        return answer;
    }
}