import java.util.Arrays;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        Arrays.sort(rocks);
        int[] distances = new int[rocks.length+1];
        
        distances[0] = rocks[0];
        for(int i=0; i < rocks.length-1; i++) {
            distances[i + 1] = rocks[i + 1] - rocks[i];
        }
        distances[rocks.length] = distance - rocks[rocks.length-1];
        
        
        // 최솟값 찾기. **주의** array 찾기가 아니라 거리의 최솟값 찾기. => [0, distance] 사이의 값
        int left = 0, mid = 0, right = distance;
        while(left <= right) {
            mid = (left + right) / 2;
            
            // 거리 최솟값이 mid 라면, 파괴된 돌 찾기
            int count = 0, prev = 0;
            for(int i=0; i < distances.length; i++) {
                if (prev + distances[i] < mid) {
                    count += 1;
                    prev += distances[i];
                }
                else {
                    prev = 0;
                }
            }
            
            // binary search
            if (count <= n) {
                answer = Math.max(answer, mid);
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }

            
        }
        
        return answer;
    }
}