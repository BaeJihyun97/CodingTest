import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.PriorityQueue;



class Solution {
    
    long calculate(long totalTime, int[] times, int n) {
        long possible = 0;
        
        for(int t:times) {
            possible += totalTime / (long)t;
            if (possible > (long)n) break;
        }
        
        return possible;
    }
    
    public long solution(int n, int[] times) {
        
        Arrays.sort(times);
        
        long answer = 0L;
        long minimum = (long)times[0], maximum = (long) n * times[0];
        long n2 = 0L;
        
        while(minimum <= maximum) {
            answer = (minimum + maximum) / 2;
            n2 = calculate(answer, times, n);
            
            if (n2 < (long)n) minimum = answer + 1;
            else if (n2 > (long)n) maximum = answer - 1;
            else break;
            
        }
        
        while (calculate(answer-1, times, n) == n) answer -= 1;
        
        
        return answer;
    }
}


// priority queue 시간 초과

// class Immigration implements Comparable<Immigration> {
    
//     int time; // 입국심사관이 걸리는 시간
//     long endTime; // 기다리는 사람이(분배 대상자) 해당 입국심사관을 고르면 끝날 시간
    
//     Immigration(int time, int endTime) {
//         this.time = time; this.endTime = (long) endTime;
//     }
    
//     @Override
//     public int compareTo(Immigration other) {
//         if (this.endTime > other.endTime ) return 1;
//         else if (this.endTime == other.endTime) return 0;
//         else return -1;
//     }
    
// } 


//         Arrays.sort(times);
//         PriorityQueue<Immigration> timesCurr = new PriorityQueue<>(Arrays.stream(times)
//                                                            .mapToObj(i-> new Immigration(i, i))
//                                                            .collect(Collectors.toList())); 
        
//         for (long i=0; i<n-1; i++) {
//             Immigration imm = timesCurr.remove();
//             imm.endTime += imm.time;
//             timesCurr.add(imm);
//         }
        
//         answer = timesCurr.peek().endTime;