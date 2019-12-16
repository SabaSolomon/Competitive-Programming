def main():
    inps = eval(input())
    count = 0
    strs = []
    while(count!=inps):
        str = input()
        strs.append(str)
        count+=1
    for i in strs:
        str_arr = list(i)
        l=[]
        r=[]
        u=[]
        b=[]
        res = ""
        for j in str_arr:
            if(j=="L"):
                l.append("L")
            elif(j=="R"):
                r.append("R")
            elif(j=="U"):
                u.append("U")
            elif(j=="D"):
                b.append("D")
        longerH = l
        shorterH = r
        if(len(l)<len(r)):
            longerH = r
            shorterH = l
        longerV = u
        shorterV = b
        if(len(u)<len(b)):
            longerV = b                          
            shorterV = u
            
        longerH = [longerH[i] for i in range(len(shorterH))]
        longerV = [longerV[i] for i in range(len(shorterV))]

        if(len(longerH)>0 and len(longerV)==0):
            res+="LR"
        elif(len(longerV)>0 and len(longerH)==0):
            res+="UD"
        else:
            for i in longerV:
                res+=i
            for l in shorterH:
                res+=l
            for j in shorterV:
                res+=j
            for k in longerH:
                res+=k
        print(len(list(res)))
        print(res)
        
                
            


                
main()
