import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Arrays.fill(answer, 0);
        ArrayList<int[]> list = new ArrayList<>(); // index, value
        
        for(int i=0; i < prices.length; i++) {
            list.add(new int[]{i, prices[i]});
            int j = 0;
            while (j < list.size()) {
                int [] curr = list.get(j);
                if (curr[1] > prices[i]) {
                    answer[curr[0]] = i - curr[0];
                    list.remove(j);
                }
                else {
                    j += 1;
                }
            }
        }
        
        int maxLength = prices.length;
        for(int [] curr: list) {
            answer[curr[0]] = maxLength - curr[0] -1;
        }
        
        
        return answer;
    }
}