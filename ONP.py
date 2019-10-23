import re
def infixtopostfix(infix):
    priority = {
            "^": 3,
            "*": 2,
            "/": 2,
            "+":1,
            "-":1,
            "(":-1
            }
    stack = list()
    postfix = ""
    for c in infix:
        if re.match(r"[a-z]",c):
            postfix+=c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack[-1] == '(':
                stack.pop()
        else:
            while stack and priority[c] <= priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(c)
    
    while stack :
        postfix += stack.pop()
    return postfix

t = int(input())
while t:
    infix = input()
    print(infixtopostfix(infix))
    t-=1
        
            
            
        
    
        
        
    