import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int n = citations.length, h;
        for(int i=n-1; i >= 0; i--) {
            h = citations[i];
            if (h <= n - i) {
                answer = Math.max(h, answer);
                break;
            }
            else {
                answer = n - i;
            }

        }
        return answer;
    }
}