def main():
    inps = input()
    str = input()
    keys = input()
    keys  = list(keys)
    subs = []
    s = ""
    slist = list(str)
    for i in range(len(slist)):
        if(slist[i] not in keys):
            if(s!=""):
                subs.append(s)
                s=""
        else:
            s+=slist[i]
    if(s!=""):
        subs.append(s)
    sum = 0
    for j in subs:
        l = len(list(j))
        possibleStr = (l*(l+1))/2
        sum += possibleStr
    print(int(sum))

main()
    
            
    
    
    
    
        
