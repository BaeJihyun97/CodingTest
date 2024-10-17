import java.util.Arrays;

class Solution {
    int DFS(int currN, int plusC) {
        // 탐색 끝
        if (currN < 3) return 0;
        else if (currN == 3 ){
            if (plusC == 2) return 1; // 첫 시작은 무조건 *
            else return 0;
        }
        else if (Math.log(currN)/Math.log(3) < plusC/2) { // +를 남발한 경우
            return 0;
        }

        
        
        int answer = 0;
        // 탐색 진행
        if (currN > 0) {
            answer += DFS(currN-1, plusC+1);
        }
        if (currN % 3 == 0 && plusC >= 2) {
            answer += DFS(currN/3, plusC-2);
        }
        
        return answer;
    }
    
    
    public int solution(int n) {
        int answer = 0;
        
        answer = DFS(n-2, 2);
        
        return answer;
        
    }
}