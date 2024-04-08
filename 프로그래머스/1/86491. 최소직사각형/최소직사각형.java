class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int largeMax = 0, smallMax = 0;
        
        for (int i=0; i < sizes.length; i++) {
            int large = sizes[i][0], small = sizes[i][1];
            if (large < small) {
                int temp = large;
                large = small;
                small = temp;
            }
            
            if (largeMax < large) {largeMax = large;}
            if (smallMax < small) {smallMax = small;}
        }

        answer = largeMax * smallMax;
        return answer;
    }
}