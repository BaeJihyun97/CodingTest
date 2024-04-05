import java.util.HashMap;
import java.util.Map.Entry;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 0;
        
        HashMap<String, Integer> map = new HashMap<>();
        for(String[] cloth: clothes) {
            map.put(cloth[1], map.getOrDefault(cloth[1], 0)+1);
        }
        
        for(Entry<String, Integer> entry: map.entrySet()) {
            System.out.printf("key: %s, value: %d\n", entry.getKey(), entry.getValue());
        }
        
        return answer;
    }
}