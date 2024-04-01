import java.util.Arrays;
import java.util.Queue;
import java.util.LinkedList;

// Queue<int[]> que 이렇게 해도 GC가 포인터 + 잡고 있는 영역 모두 free?

class Solution {
    
    private int bfs(int[][] picture, boolean[][] visited, int i, int j) {
        int color = picture[i][j];
        Queue<int[]> que  = new LinkedList<int[]>();
        que.add(new int[] {i, j});
        int [][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int count = 0;
        
        while (!que.isEmpty()) {
            int[] curr = que.poll();
            int x = curr[0], y = curr[1];
            
            if (!visited[x][y]) {
                count += 1;
                visited[x][y] = true;

                for(int k=0; k < 4; k++) {
                    int next_x = x + directions[k][0], next_y = y + directions[k][1];
                    if (picture[next_x][next_y] == color && !visited[next_x][next_y]) {
                        que.add(new int[] {next_x, next_y});
                    }
                }
            }
            
            
            
        }
        
        return count;
        
    }
        
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        int[][] picture_new = new int[m+2][n+2];
        for(int i=0; i < m+2; i++){
            for(int j=0; j < n+2; j++){
                if (i == 0 || i == m+1 || j == 0 || j == n+1){
                    picture_new[i][j] = 0;
                }
                else {
                    picture_new[i][j] = picture[i-1][j-1];
                }
            }
        }
        
        boolean [][] visited = new boolean[m+2][n+2];
        for (int i=0; i < m+2; i++) {
            Arrays.fill(visited[i], false);
        }
        

        for(int i=1; i < m+1; i++) {
            for(int j=1; j < n+1; j++) {
                if (!visited[i][j] && picture_new[i][j] != 0) {
                    int temp = bfs(picture_new, visited, i, j);
                    numberOfArea += 1;
                    if (temp > maxSizeOfOneArea ){
                        maxSizeOfOneArea = temp;
                    }
                }
            }
        }
        
        
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}