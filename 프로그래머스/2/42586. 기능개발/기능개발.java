import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        int jobLength = progresses.length;
        int[] jobDays = new int[jobLength];
        
        for (int i=0; i < jobLength; i++) {
            jobDays[i] = (100-progresses[i]+speeds[i]-1) / speeds[i];
        }
        
        int prev = 0, count = 0;
        if (jobLength > 0) { prev = jobDays[0];}
        for (int i=0; i < jobLength; i++) {
            if (prev >= jobDays[i]) {
                count += 1;
            }
            else {
                answer.add(count);
                count = 1;
                prev = jobDays[i];
            }
        }
        if (count > 0) {
            answer.add(count);
        }
        
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}