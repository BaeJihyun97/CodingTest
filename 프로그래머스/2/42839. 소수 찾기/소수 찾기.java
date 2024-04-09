import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

class Solution {
    
    boolean check(String num) {
        int number = Integer.parseInt(num);
        int numMax = (int) Math.sqrt(number);
        
        if (number < 2) {
            return false;
        }
        
        for (int i=2; i <= numMax; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    void dfs(char[] numberArray, HashSet<Integer> set, boolean[] visited, int depth, int r, StringBuffer curr) {
        if (depth == r) {
            return;
        }
        
        for (int i=0;i<numberArray.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                curr.append(numberArray[i]);
                
                if (check(curr.toString())) {
                    set.add(Integer.parseInt(curr.toString()));
                }

                dfs(numberArray, set, visited, depth+1, r, curr);
                
                curr.deleteCharAt(curr.length() - 1);
                visited[i] = false;
            }
        }
        return;
    }
    
    public int solution(String numbers) {
        int answer = 0;
        char [] numberArray = numbers.toCharArray();
        HashSet<Integer> set = new HashSet<>();
        boolean[] visited = new boolean[numberArray.length];
        
        Arrays.fill(visited, false);
        Arrays.sort(numberArray);
        
        dfs(numberArray, set, visited, 0, numberArray.length, new StringBuffer());
        
        answer = set.size();
        return answer;
    }
}