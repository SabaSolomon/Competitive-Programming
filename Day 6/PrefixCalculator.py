

def compute(input):
    stack = list(input)
    print(stack)
    operations = ['+','-','*','/']
    result = 0
    temp_stack = []
    while(len(stack)!=0):
        temp = stack.pop()
        if(temp not in operations):
            temp_stack.append(temp)
        elif(temp in operations):
            a = temp_stack.pop()
            b = temp_stack.pop()
            if(temp == "+"):
                result =  int(a) + int(b)
                temp_stack.append(result)
            elif(temp == "-"):
                result =  int(a) - int(b)
                temp_stack.append(result)
            if(temp == "*"):
                result =  int(a) * int(b)
                temp_stack.append(result)
            if(temp == "/"):
                result =  int(a) / int(b)
                temp_stack.append(result)
    return temp_stack.pop()    

print(compute("*4+34"))
