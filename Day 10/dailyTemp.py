def dailyTemperatures(T):
    for i in range(len(T)-1):
        count = 0
        found = False
        check = i+1
        while(check < len(T)):
            if(T[i]< T[check]):
                count += 1
                found = True
                break
            check += 1
            count += 1
        if(found):
            T[i] = count
        else:
            T[i] = 0
    T[len(T)-1] = 0
    return T

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
        
    
