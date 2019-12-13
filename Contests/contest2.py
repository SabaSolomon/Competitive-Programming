def main():
    inps = eval(input())
    count = 0
    lengths = []
    arrs = []
    while(count!=inps):
        l = eval(input())
        inp = input().split()
        int_inp = [ int(i) for i in inp]
        arrs.append(int_inp)
        lengths.append(l)
        count+=1
    index = 0
    for i in arrs:
        str = ["0" for x in range(lengths[index])]
        str[0] = "1"
        min = i.index(1)
        max = i.index(1)
        for j in range(2, lengths[index]+1):
            if(max < i.index(j)):
                max = i.index(j)
            elif(min > i.index(j)):
                min = i.index(j)
            if((max - min) + 1 == j):
                str[j-1] = "1"
            else:
                str[j-1] = "0"
            
       
        print(''.join(str))
        index +=1
            
main()

