import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int passingWeight = 0, time = 0;
        Deque<int[]> que = new ArrayDeque<>(); // time, weight
        
        for(int truck:truck_weights) { 
            if (passingWeight + truck <= weight) {
                que.addLast(new int[] {time, truck});
                passingWeight += truck;
            }
            else {
                while (passingWeight+truck > weight) {
                    int[] curr = que.getFirst();
                    if (time - curr[0] >= bridge_length) {
                        que.removeFirst();
                        passingWeight -= curr[1];
                    }
                    else {
                        time += 1;
                    }
                }
                que.addLast(new int[] {time, truck});
                passingWeight += truck;
            }
            time += 1;
        }
        answer = time+bridge_length;
        return answer;
    }
}