import java.util.PriorityQueue;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map.Entry;


class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {0, 0};
        
        PriorityQueue<Integer> minpq = new PriorityQueue<>();
        PriorityQueue<Integer> maxpq = new PriorityQueue<>(Collections.reverseOrder());
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;
        
        for(String op:operations) {
            String[] ops = op.split(" ");
            char alpha = ops[0].charAt(0);
            int num = Integer.parseInt(ops[1]);

            if (alpha == 'I') { // inset
                minpq.add(num);
                maxpq.add(num);
                map.put(num, map.getOrDefault(num, 0)+1);
                count += 1;
            }
            else { // remove 
                if (count > 0) {
                    int value;
                    if (num == 1) { // get max value
                        value = maxpq.remove();
                        while (map.get(value) <= 0 ) { value = maxpq.remove(); } // min에서 지워진 것이 남아있을 수 있음
                    }
                    else { // get min value
                        value = minpq.remove();
                        while (map.get(value) <= 0 ) { value = minpq.remove(); } // max에서 지워진 것이 남아있을 수 있음
                    }
                    map.put(value, map.get(value)-1);
                    count -= 1;
                    
                    // count 가 0 이 되면 바로 지우기
                    if (count == 0) {
                        minpq.clear();
                        maxpq.clear();
                    }
                }
                
            }
        }
        
        if (count > 0) {
            answer[0] = maxpq.peek().intValue();
            answer[1] = minpq.peek().intValue();
        }
        
        return answer;
    }
}