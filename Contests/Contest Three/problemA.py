def main():
    inps = eval(input())
    count = 0
    passwords = []
    hashs = []
    while(count!=inps):
        strs = input()
        hashStr = input()
        passwords.append(strs)
        hashs.append(hashStr)
        count+=1
    for i in range(inps):
        indexs=[]
        ids = []
        hlist = list(hashs[i])
        passList = list(passwords[i])
        ind = 0
        for j in hlist:
            if(j not in passList):
                hlist[ind] = ""
            ind += 1
        passwordHash = ''.join(hlist)
        if (passwords[i] in passwordHash):
            print("YES")
        elif (''.join(sorted(passwords[i])) in ''.join(sorted(passwordHash)) and len(passList)==len(passwordHash)):
            print("YES")
        else:
            print("NO")
        
        
main()
    
