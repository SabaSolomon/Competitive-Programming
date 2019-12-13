def sortColors(nums):
    zeros = 0
    ones = 0
    twos = 0
    for i in range (len(nums)):
        if(nums[i] == 0):
            zeros += 1
        elif(nums[i] == 1):
            ones += 1
        else:
            twos += 1
    

    count = 0
    for i in range (zeros):
        nums[count] = 0
        count += 1
    for j in range (ones):
        nums[count] = 1
        count +=1 
    for k in range (twos):
        nums[count] = 2
        count +=1


    
def sortOnePass(nums):
    maxIndex = len(nums) - 1
    minIndex = 0
    for i in range (len(nums)):
        if(nums[i] == 0 and i > minIndex):
            if(nums[minIndex] == 0 ):
                minIndex += 1
            if(nums[minIndex] == 2 and i != maxIndex):
                nums[minIndex], nums[maxIndex] = nums[maxIndex], nums[minIndex]
                maxIndex -= 1
            elif(nums[minIndex] == 2 and i == maxIndex):
                maxIndex -= 1
            nums[minIndex], nums[i] = nums[i], nums[minIndex]
            minIndex += 1
        elif(nums[i] == 0 and i == minIndex):
            minIndex += 1
        elif(nums[i] == 2 and i < maxIndex):
            if(nums[maxIndex] == 2):
                maxIndex -= 1
            if(nums[maxIndex] == 0 and i != minIndex):
                nums[minIndex], nums[maxIndex] = nums[maxIndex], nums[minIndex]
                minIndex += 1
            elif(nums[maxIndex] == 0 and i == minIndex):
                minIndex += 1
            print(nums[maxIndex], nums[i],i)
            nums[maxIndex], nums[i] = nums[i], nums[maxIndex]
            
            maxIndex -= 1
        elif(nums[i] == 2 and i == maxIndex):
            maxIndex -= 1

            
nums = [2,2,1,2,1,1,1,0,0,2,1,0,2,1,2,2,1,1,1,1,1,0,2,0,2,0,2,2,1,0,2,1,0,2,1,2,0,0,0,0,2,1,1,2,0,1,2,2,0,0,2,2,0,1,0,1,0,0,1,1,1,0,0,2,2,2,1,0,0,2,1,0,1,0,2,2,1,2,1,1,2,1,1,0,0,2,1,0,0]
     
sortOnePass(nums)
print(nums)
