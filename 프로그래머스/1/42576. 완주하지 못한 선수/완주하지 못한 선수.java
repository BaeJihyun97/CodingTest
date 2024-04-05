import java.util.HashMap;
import java.util.Map.Entry;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for(String part:participant) {
            if (map.get(part) == null) {
                map.put(part, 1);
            }
            else {
                map.put(part, map.get(part)+1);
            }
        }
        
        for(String com: completion) {
            map.put(com, map.get(com)-1);
        }
        
        for(Entry<String, Integer> entry: map.entrySet()){
            if (entry.getValue() == 1) {
                answer = entry.getKey();
            }
        }
        
        return answer;
    }
}