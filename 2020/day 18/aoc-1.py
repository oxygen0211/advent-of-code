import re
input =  '1 + (2 * 3) + (4 * (5 + 6))'

stack = []

def evaluate(stack):
    num1 = stack.pop()
    op = stack.pop()

    print('num: {}, op: {}, stack:{}'.format(num1, op, stack))
    if len(stack) == 1:
        num2 = stack[0]

    else:
        num2 = evaluate(stack)

    print('{} {} {}'.format(num1, op, num2))
    if op == '+':
        result = num1 + num2

    elif op == '*':
        result = num1 * num2

    return result

for char in input:

    if re.match('[0-9]', char):
        stack.append(int(char))

    elif re.match('[+*]', char):
        stack.append(char)

    elif re.match('[(]', char):
        

print('result: {}'.format(evaluate(stack)))
