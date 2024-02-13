def solution(n):
    A = [0] * (100000+1)
    A_S = [0] * (100000+1)
    A_S3 = [0] * (100000+1)
    A[0:4] = [1, 1, 3, 10]
    A_S[0:4] = [1, 2, 5, 15]
    
    
    for index in range(4, n+1):
        if index >= 6:
            A_S3[index] = A[index-6] + A_S3[index-3]
            
        A[index] = ((A[index-1] + 2 * A[index-2] + 5 * A[index-3])
                    + (2 * A_S[index-4] + 2 * A_S3[index])
                   ) % 1000000007
        
        A_S[index] = A_S[index-1] + A[index]

    
    
    return A[n]