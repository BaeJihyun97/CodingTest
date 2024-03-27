import java.util.Map;
import java.util.HashMap;

class Solution {
    
    private final int NUMBER_MEMBER = 8;
    static int count = 0;
    
    public int solution(int n, String[] data) {
        // 전역변수 초기화
        count = 0;
        
        int answer = 0;
        int eight_fac = 1;
        for (int i = 2; i <= NUMBER_MEMBER; i++) {eight_fac = eight_fac * i;}
        int data_new[][] = new int[NUMBER_MEMBER][4];
        int[][] permutations = new int[eight_fac][NUMBER_MEMBER];
        
        make_permutatation(new int[] {0, 1, 2, 3, 4, 5, 6, 7}, new int[NUMBER_MEMBER], permutations, 0, new boolean[NUMBER_MEMBER], NUMBER_MEMBER);  
        
        
        Map<Character, Integer> ht = new HashMap<Character, Integer>();
        char[] names = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T', '=', '>', '<'};
        for(int i=0; i < NUMBER_MEMBER+3; i++) {
            ht.put(names[i], i);
        }
        
        // data 형식 바꾸기
        for(int i=0; i < data.length; i++) {
            // Integer.parseInt(str)
            String condition = data[i];
            data_new[i][0] = ht.get(condition.charAt(0));
            data_new[i][1] = ht.get(condition.charAt(2));
            data_new[i][2] = ht.get(condition.charAt(3));
            data_new[i][3] = Character.getNumericValue(condition.charAt(4));   
        }
        
        
        for(int i=0; i < eight_fac; i++) {
            if (check(data_new, permutations[i])) {
                answer += 1;
            }
        }
        return answer;
        
    }
    
    public static void make_permutatation(int[] nums, int[] out, int[][] permutations, int depth, boolean[] visited, int r) {
        if (depth == r) {
            permutations[count++] = out.clone();
            return;
        }
        
        for(int i=0; i<nums.length; i++){
            if(!visited[i]){
                visited[i] = true;
                out[depth] = nums[i];
                make_permutatation(nums, out, permutations, depth+1, visited, r);
                visited[i] = false;
            }
        }
        
        return;
    } 
    
    boolean check(int[][] data, int[] order) {
        for(int i=0; i < data.length; i++) {
            int[] condition = data[i];
            int f1 = condition[0], f2 = condition[1], equ = condition[2], dist = condition[3];
            
            int dist_order = Math.abs(order[f1]-order[f2])-1;
            if (equ == 8) {
                if (dist_order != dist) {
                    return false;
                }
            }
            else if (equ == 9) {
                if (dist_order <= dist) {
                    return false;
                }
            }
            else{
                if (dist_order >= dist) {
                    return false;
                }
            }
        }
        return true;
    }
}
