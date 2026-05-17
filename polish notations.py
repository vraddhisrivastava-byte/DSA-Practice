"""
def infix_to_postfix(exp):
    stack=[]
    output=[]
    priority={'**':3,'*':2,'/':2,'+':1,'-':1 ,'^':3}
    for char in exp:
        if char.isalnum():
            output.append(char)
        elif char=="(" :
            stack.append(char)
        elif char==")" :
            while stack and stack[-1]!="(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1]!="(" and priority[char]<=priority[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

exp="(a+b)*c-d"
print(infix_to_postfix(exp))
"""
"""
def post_exp_eval(exp):
    stack=[]
    for char in exp:
        if char.isdigit():
            stack.append(int(char))
        else:
            top_el=stack.pop()
            next_el=stack.pop()
            if char=='+':
                stack.append(top_el+next_el)
            elif char=='-':
                stack.append(top_el-next_el)
            elif char=='*':
                stack.append(top_el*next_el)
            elif char=='/':
                stack.append(top_el/next_el)
    return stack.pop()

exp="236*+4+8-"
print(post_exp_eval(exp))
"""