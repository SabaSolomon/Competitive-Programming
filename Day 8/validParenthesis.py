def isValid(s):
        """
        :type s: str
        :rtype: bool
        """

        
        s = s.replace(" ","")
        slist = list(s)
        stack = []

        for i in s:
            if(i == "{" or i=="(" or i=="["):
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False
                    
                if((i=="}" and stack[len(stack)-1]=="{") or
                   (i==")" and stack[len(stack)-1]=="(") or
                   (i=="]" and stack[len(stack)-1]=="[")):
                    stack.pop()
                else:
                    return False
                
        if(len(stack) == 0):
            return True
        else:
            return False
                
        
print(isValid("({})"))
