import java.util.Arrays;

class Solution {
    
    int dfs(int[][] dungeons, boolean[] visited, int depth, int r, int count, int k) {
        if (depth == r) {
            return count;
        }
        
        int maxCount = count;
        for (int i=0; i < dungeons.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                
                if (k >= dungeons[i][0]) {
                    count += 1;
                    k -= dungeons[i][1];
                    maxCount = Math.max(dfs(dungeons, visited, depth+1, r, count, k), maxCount);
                    k += dungeons[i][1];
                    count -= 1;
                }
                else {
                    dfs(dungeons, visited, depth+1, r, count, k);
                }
                
                visited[i] = false;
            }
        }
        
        return maxCount;
    }
    
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        Arrays.fill(visited, false);
        int answer = dfs(dungeons, visited, 0, dungeons.length, 0, k);
        return answer;
    }
}