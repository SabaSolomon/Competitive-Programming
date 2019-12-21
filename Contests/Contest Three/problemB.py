def main():
    inps = eval(input())
    count = 0
    arrs = []
    while(count!=inps):
        inp = input().split()
        int_inp = [ int(i) for i in inp]
        arrs.append(int_inp)
        count += 1
    for i in arrs:
        counter = 0
        a = i[0]
        b = i[1]
        if(a == b):
            print(counter)
            continue
        else:
            indexa = 1
            indexb = 1
            while(a != b):
                if(a>b):
                    b+=indexb
                    indexb +=1
                elif(b>a):
                    a+=indexa
                    indexa +=1
                if(indexa==4):
                    indexa = 1
                
                counter +=1
            print(counter)
main()
