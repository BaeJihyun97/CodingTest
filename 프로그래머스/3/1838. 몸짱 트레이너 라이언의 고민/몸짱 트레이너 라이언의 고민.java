import java.util.Arrays;
import java.util.PriorityQueue;
import java.lang.Math;


class Solution {
    
    void fill(int n, int[][] possible, int i, int j, int depth, int min_distance) {
        for(int x = 0; x < min_distance; x++) {
            for(int y=0; y+x < min_distance; y++) {
                int[][] temp = {{i+x, j+y}, {i+x, j-y}, {i-x, j+y}, {i-x, j-y}};
                for(int[] c : temp) {
                    if (c[0] >= 0 && c[0] < n && c[1] >= 0 && c[1] < n && possible[c[0]][c[1]] == 0) {
                        possible[c[0]][c[1]] = depth;
                    }
                }
            }
        }
        return;
    }
    
    int calc(int n, int[] row, int min_distance) {
        int max = 0;
        int[][] visited = new int[n][n];
        for(int i= 0; i < n; i++) Arrays.fill(visited[i], 0);   // 선언, 초기화
        
        for(int i= 0; i < n; i++) { // 첫번째 행 
            if (row[i] == 1) {
                visited[0][i] = row[i];
                fill(n, visited, 0, i, 1, min_distance);
                max += 1;
            }
        }
        
        // 나머지 행 넣기
        for (int i=1; i < n; i++) {
            for (int j=0; j < n; j++) {
                if (visited[i][j] == 0) {
                    fill(n, visited, i, j, 1, min_distance);
                    max += 1;
                }
            }
        }
        
        return max;
    }
    
    // 크기 n 격자와 최소거리 d가 주어질 때 가장 많이 할당할 수 있는 라커 수 구하기.
    // 이것도 전체 격자의 모든 위치를 선택으로 두면 timeout
    // 탐색 범위를 줄이자-> 첫 행만 모든 경우의 수로 탐색 범위를 두면
    // 나머지 행들은 최대한 많이 넣기 위해서는 최소 거리를 두고 위치
    // 즉 이전 위치로 나머지 행들의 할당 위치가 결정될 수 있음. 이중에 정답 존재.
    int dfs(int n, int[] row, int depth, int min_distance, int prev) {
        if(depth >= n) {
            return calc(n, row, min_distance);
        }
        
        int not_selected = dfs(n, row, depth+1, min_distance, prev);
        int selected = 0;

        if (depth - prev >= min_distance) {
            row[depth] = 1;
            selected = dfs(n, row, depth+1, min_distance, depth);
            row[depth] = 0;
        }

        return Math.max(selected, not_selected);
    } 
    
    
    public int solution(int n, int m, int[][] timetable) {
        int answer = 0;
        
        // 최대 인원수 구하기
        // 겹치는 최대 구간 개수 구하는 문제
        Arrays.sort(timetable, (o1, o2) -> { return o1[0]!=o2[0] ? o1[0]-o2[0] : o1[1]-o2[1]; });
        int person = 0, max_people = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < m; i++) {
            person += 1;
            pq.add(timetable[i][1]);
            while (pq.size() > 0) {
                if (pq.peek() < timetable[i][0]) {
                    pq.poll();
                    person -= 1;
                }
                else {
                    break;
                }
            }
            max_people = Math.max(max_people, person);
            // System.out.printf("person: %d, max_people: %d, start: %d\n", person, max_people, timetable[i][0]);
        }
        
        // max_people명의 사람일 때 최대 거리 구하기
        if (max_people > 1) {
            int [][] possible = new int[n][n];
            int [][] visited = new int[n][n];
            for (int i = 0; i < n; i++) Arrays.fill(visited[i], 0);
            for (int i = 0; i < n; i++) Arrays.fill(possible[i], 0);
            
            for(int min_distance = 2*(n-1); min_distance > 0; min_distance--) {
                int[] row = new int[n];
                Arrays.fill(row, 0);
                
                if(dfs(n, row, 0, min_distance, -2*n) >= max_people) {
                    answer = min_distance;
                    break;
                }
            }
        }
        
            
        return answer;
    }
}