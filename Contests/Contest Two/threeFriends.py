def main():
    inps = eval(input())
    count = 0
    nums = []
    while(count!=inps):
        int_str = input().split()
        int_inp = [ int(j) for j in int_str]
        nums.append(int_inp)
        count+=1
        
    for i in nums:
        dist = None
        a = i[0]
        b = i[1]
        c = i[2]

        check = None
        
        while(check != "Done"):
            if(dist is None):
                dist = abs(i[0]-i[1])+abs(i[0]-i[2])+abs(i[1]-i[2])
            else:
                for x in range(-1, 2):
                    tempa = a + x
                    for y in range(-1, 2):
                        tempb = b + y
                        for z in range(-1, 2):
                            tempc = c + z
                            dist = compareDist(dist, tempa, tempb, tempc)
                check = "Done"
        check = None
        print(dist)
                        
            
            
def compareDist(dist, a, b, c):
    new_dist = abs(abs(a-b)+abs(a-c)+abs(b-c))
    if(dist>new_dist):
            dist = new_dist
    return dist
    
main() 
