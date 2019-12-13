def evalRPN(tokens):
    operations = ["+","-","*","/"]
    temp_stack = []
    while(len(tokens)!=0):
        temp = tokens.pop(0)
        if(temp not in operations):
            temp_stack.append(temp)
        else:
            a2 = int(temp_stack.pop())
            a1 = int(temp_stack.pop())
            if(temp == "+"):
                result = a1 + a2
            elif(temp == "-"):
                result = a1 - a2
            elif(temp == "*"):
                result = a1 * a2
            elif(temp == "/"):
                result = a1 / a2
            temp_stack.append(int(result))

    return temp_stack.pop()

    
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
))
