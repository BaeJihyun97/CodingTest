import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    
    ArrayList<Integer> primes = new ArrayList<>();
    
    void findPrimes(int maxV) {
        for (int i=2; i <= maxV; i++) {
            primes.add(i);
        }
        
        for (int i=2; i <= maxV; i++) {
            if (primes.contains(i)) {
                for (int j=i*2; j<= maxV; j+=i) {
                    if (primes.indexOf(j) >= 0) {
                        primes.remove(primes.indexOf(j));
                    }
                }
            }
        }
    }
    
    public int solution(String numbers) {
        int answer = 0;
        int [] numberArray = numbers.chars().map(i->i-'0').toArray();
        Arrays.sort(numberArray);
        
        int maxNum = 0;
        for(int i=numberArray.length-1; i >= 0 ; i--) {
            maxNum *= 10;
            maxNum += numberArray[i];
        }
        
        findPrimes(maxNum);
        
        return answer;
    }
}