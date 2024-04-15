import java.util.HashSet;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        HashSet<Integer> lostSet = new HashSet<>(Arrays.stream(lost).boxed().collect(Collectors.toList()));
        HashSet<Integer> reserveSet = new HashSet<>(Arrays.stream(reserve).boxed().collect(Collectors.toList()));
        
        // 본인 체육복 먼저 챙기기
        for (int i=1; i <= n; i++) {
            if (lostSet.contains(i) && reserveSet.contains(i)) {
                reserveSet.remove(i);
                lostSet.remove(i);
            }
        }
        
        int[] temp = lostSet.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(temp);
        answer = temp.length;
        
        // 빌려주기
        for (int l: temp) {
            if (reserveSet.contains(l-1)) {
                answer -= 1;
                reserveSet.remove(l-1);
            }
            else if (reserveSet.contains(l+1)) {
                answer -= 1;
                reserveSet.remove(l+1);
            }
        }
        
        
        return n - Math.max(answer, 0);
    }
}
    
    
    