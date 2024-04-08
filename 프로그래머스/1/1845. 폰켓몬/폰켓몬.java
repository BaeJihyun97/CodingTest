import java.util.HashSet;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] nums) {
        int answer = 0, maxV = nums.length / 2;
        
        // Integer [] temp = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        HashSet<Integer> set = new HashSet<>(Arrays.stream(nums).boxed().collect(Collectors.toList()));
        
        answer = set.size();
        if (maxV < answer) {
            answer = maxV;
        }
        
        return answer;
    }
}