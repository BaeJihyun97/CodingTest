import java.util.Arrays;

class Solution {
    
    int getFisrt(int i) {
        return (i) % 5 + 1;
    }
    
    int getSecond(int i) {
        if (i % 2 == 0) return 2;
        else {
            if (((i+1) / 2) % 4 == 1) return 1;
            else {
                return ((i-1) / 2) % 4 + 2;
            }
        }
    }
    
    int getThird(int i) {
        int temp = (i / 2) % 5;
        int returnV = 0;
        switch(temp) {
            case 0: returnV = 3; break;
            case 1: returnV = 1; break;
            case 2: returnV = 2; break;
            case 3: returnV = 4; break;
            case 4: returnV = 5; break;   
        }
        return returnV;
    }
    
    
    public int[] solution(int[] answers) {
        int[] answer = {0, 0, 0};
        int a1 = 0, a2 = 0, a3 = 0;
        for (int i=0; i < answers.length; i++) {
            if (answers[i] == getFisrt(i)) a1 += 1;
            if (answers[i] == getSecond(i)) a2 += 1;
            if (answers[i] == getThird(i)) a3 += 1;
        }
        
        int maxV = Math.max(Math.max(a1, a2), a3);
        int [] temp = {a1, a2, a3}; 
        
        int count = 0;
        for (int i=0; i < 3; i++) {
            if (temp[i] == maxV) {
                answer[count] = i+1;
                count += 1;
            }
        }
        
        return Arrays.copyOfRange(answer, 0, count);
    }
}