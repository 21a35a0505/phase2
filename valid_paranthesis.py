'''
stack=[]
s=input('Enter a String')
for i in s:
    if i=='(':
        stack.append(i)
    elif i==')' and len(stack)!=0:
        stack.pop()
    else:
        print('invalid string')
if len(stack)==0:
    print('valid string')
else:
    print('invalid string')
'''
def valid_identifier(s):
    a=[]
    for i in s:
        if i not in ')]}':
            a.append(i)
        elif i in ')}]':
            for j in range(len(a)):
                b=a.pop()
                if b=='(' and i==')':
                    break
                elif b=='[' and i==']':
                    break
                elif b=='{' and i=='}':
                    break
                elif (b=='(' and i==']') or (b=='(' and i=='}')or(b=='[' and i=='}') or(b=='{' and i==']')or(b=='[' and i==')')or(b=='{' and i==')'):
                    return print('invalid identifier')
    if len(a)==0 and(s[0] not in '}])'):
        print('valid identifier')
    else:
        print('invalid identifier')
a=True
while(a):
    a=input()
    valid_identifier(input())

