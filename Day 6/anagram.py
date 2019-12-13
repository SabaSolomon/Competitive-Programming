def isAnagram(s, t):
    s = list(s)
    t = list(t)
    if(len(s)!= len(t)):
        return False
    
        
    return sortString(s) == sortString(t)
    
print(isAnagram("anagram", "nagarom"))





def sortString(str):
    MAX_CHAR = 26
    charCount = [0 for i in range(MAX_CHAR)]     
    for i in range(0, len(str)): 
        charCount[ord(str[i]) - ord('a')] += 1   # 'a'-'a' will be 0, 'b'-'a' will be 1,
    str = ""
    for i in range(0, MAX_CHAR): 
        for j in range(0, charCount[i]): 
            str += chr(ord('a') + i)
    return str

print(sortString("anagram"))
