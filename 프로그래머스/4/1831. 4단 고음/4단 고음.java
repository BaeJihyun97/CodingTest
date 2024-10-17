// 알고리즘: DFS + 점화식
// 자료구조: Integer
// 주의: 반대로 가는 것이 더 탐색 범위가 작을 수 있음. 항상 상황이 symetric 한건 아님!
//      최소 '**...*++++...++' = 3^n + (2*n)
//      최대 '*++*++......*++' = 2*(3^n) - 1 (b(i+1) = 3b(i) + 2 점화식 일반항)
//      여기서 n은 별의 개수
//      *(/) 를 많이 하는 건 경우의 수가 많이 없음. 3^18 ~= 2^31이고 나눠 떨어지고, + 가 2 이상이어야 하니까
//      +(-) 를 많이 하는 것은 가지치기 해야함. 
//          계산하면서 있어야 할 *의 수 = plusC /2
//          계산하고 남은 수에서 최대학 많이 가질수 있는 *의 수 = log_(3)(currN) == log(currN) / log(3)
//          위의 최소 최대 식에서 계산해 보면 가능한 고음수(N)의 별의 개수(n)는 log_3(N) 
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