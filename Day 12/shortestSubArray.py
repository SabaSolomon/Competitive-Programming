def shortestSubArray(A, K):
    sum = 0
    for i in range(0, len(A)):
        sum += A[i]
        min = A[0]
        if(K <= sum and sum-min >= K):
            return i
        elif(K <= sum):
            return i+1
    return -1

print(shortestSubArray([2,-1,2], 3))


