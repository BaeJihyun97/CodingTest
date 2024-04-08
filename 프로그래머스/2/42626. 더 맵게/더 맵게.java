import java.util.PriorityQueue;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Arrays.stream(scoville).boxed().collect(Collectors.toList()));
        
        while (pq.size() > 1) {
            if (pq.peek() >= K) {
                break;
            }
            
            int first = pq.remove(), second = pq.remove();
            pq.add(first + second + second);
            answer += 1;
        }
        
        if (pq.peek() < K) answer = -1;
        return answer;
    }
}