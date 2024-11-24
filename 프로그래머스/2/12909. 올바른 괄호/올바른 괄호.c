#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer = true;
    int count = 0, s_len = strlen(s);
    char* ptr = s;
     
    
    for (int i=0; i < s_len; i++, ptr++) {
        count += *ptr == '('?1:-1;
        
        if (count < 0) {
            answer = false;
            break;
        }
        
    }
    
    answer = count==0?true:false;
    return answer;
}