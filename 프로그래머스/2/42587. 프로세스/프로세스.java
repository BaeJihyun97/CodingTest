import java.util.Arrays;
import java.util.Deque;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.ArrayDeque;




class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        int priorityMax = Arrays.stream(priorities).max().getAsInt();
        // Deque<Integer> que = new ArrayDeque<>(Arrays.stream(priorities).boxed().collect(Collectors.toList()));
        Deque<int[]> que = new ArrayDeque<>(IntStream.range(0, priorities.length)
                                            .mapToObj(i-> new int[]{i, priorities[i]})
                                            .collect(Collectors.toList()));
        while (!que.isEmpty()) {
            int[] curr = que.removeFirst();
            if (curr[1] >= priorityMax) {
                if (curr[0] == location) {
                    break;
                }
                else {
                    answer += 1;
                    priorityMax = que.stream().mapToInt(pair->pair[1]).max().getAsInt();
                }
            }
            else {
                que.addLast(curr);
            }
        }
        
        
        return answer;
    }
}