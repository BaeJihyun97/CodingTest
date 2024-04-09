class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        int row = 1, col = 1, maxV = Math.max(brown, yellow);
        boolean flag = false;
        
        for (int i=1; i <= maxV; i++ ) {
            for (int j=1; j <= maxV; j++) {
                if (((j-2) * (i-2) == yellow) && (i*2 + j*2 - 4 == brown)) {
                    row = i;
                    col = j;
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }
        
        if (row < col) {
            int temp = row;
            row = col;
            col = temp;
        }
        
        answer[0] = row;
        answer[1] = col;
        
        return answer;
    }
}