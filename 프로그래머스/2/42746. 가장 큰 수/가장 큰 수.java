import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.Collections;

class Number implements Comparable<Number>{
    
    String original = "";
    
    Number(int num) {
        this.original = Integer.toString(num);
    }
    
    @Override
    public int compareTo(Number other) {
        String to = this.original + other.original;
        String ot =  other.original + this.original;
        
        return to.compareTo(ot);
    }
}

class Solution {
    public String solution(int[] numbers) {
        StringBuffer bf = new StringBuffer();
        ArrayList<Number> numberList = new ArrayList<>(Arrays.stream(numbers)
                                                       .mapToObj(num -> new Number(num))
                                                       .collect(Collectors.toList()));
        
        Collections.sort(numberList, Collections.reverseOrder());
        
        for (Number num:numberList) {
            bf.append(num.original);
        }
        
        String answer = bf.toString();
        if (answer.charAt(0) == '0') {
            answer = "0";
        }
        
        
        return answer;
    }
}