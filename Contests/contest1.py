def main():
    inps = eval(input())
    count = 0
    strings = []
    while(count!=inps):
        strs = input()
        strings.append(strs)
        count+=1

    for i in strings:
        counta = 0
        countb = 0
        countc = 0
        for j in list(i):
            if(j=="a"):
                counta+=1
                countb = 0
                countc = 0
            elif(j=="b"):
                countb+=1
                counta = 0
                countc = 0
            elif(j=="c"):
                countc+=1
                counta = 0
                countb = 0
            elif(j=="?"):
                counta = 0
                countb = 0
                countc = 0
            if(counta == 2 or countb == 2 or countc == 2):
                print(-1)
                i = ""
                break
        if(len(i)==0):
            continue
        strlist = list(i)
        prev = strlist[0]
        if(prev == "?" and len(strlist)!= 1):
            if(strlist[1]=="a"):
                strlist[0] = "b"
                prev = strlist[0]
            else:
                strlist[0] = "a"
                prev = strlist[0]
        elif(prev == "?" and len(strlist)== 1):
            print("b")
            continue
        for j in range(1, len(strlist)):
            if(strlist[j] == "?"):
                if(j == len(strlist)-1):
                    if(prev =="a"):
                        strlist[j] = "b"
                    else:
                        strlist[j] = "a"
                elif(prev =="a"):
                    if(strlist[j+1] != "b"):
                        strlist[j] = "b"
                        prev = "b"
                    else:
                        strlist[j] = "c"
                        prev = "c"
                elif(prev == "c"):
                    if(strlist[j+1] != "b"):
                        strlist[j] = "b"
                        prev = "b"
                    else:
                        strlist[j] = "a"
                        prev = "a"
                elif(prev == "b"):
                    if(strlist[j+1] != "a"):
                        strlist[j] = "a"
                        prev = "a"
                    else:
                        strlist[j] = "c"
                        prev = "c"
            else:
                prev = strlist[j]
            
        print(''.join(strlist))            
                    
main()                
    
    
