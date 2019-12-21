def dailyTemperatures(T):
    stack = []
    result = [0 for i in T]
    for i in range(len(T)):
        if(len(stack)==0):
            stack.append([i, 0])
        else:
            l = len(stack)-1
            while(True):
                if(len(stack)==0):
                    stack.append([i, 0])
                    break
                if(T[stack[len(stack)-1][0]] < T[i]):
                    l -= 1
                    element = stack.pop()
                    result[element[0]] = element[1] + 1
                    
                elif(T[stack[len(stack)-1][0]] >= T[i]):
                    for n in stack:
                        n[1] += 1
                    stack.append([i, 0])
                    break
                        
                   

                   
                        
    return result

##        count = 0
##        found = False
##        check = i+1
##        while(check < len(T)):
##            if(T[i]< T[check]):
##                count += 1
##                found = True
##                break
##            check += 1
##            count += 1
##        if(found):
##            T[i] = count
##        else:
##            T[i] = 0
##    T[len(T)-1] = 0
    return T

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
        
    
