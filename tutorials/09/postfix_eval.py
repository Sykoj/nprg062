stack = []
postfix_expression = "4 3 *"
#"4 5 + 3 *"

for value in postfix_expression.split():
    if value.isdecimal():
        stack.append(int(value))
    else:
        o1 = stack.pop()
        o2 = stack.pop()

        if value == '+':
            stack.append(o1 + o2)
        elif value == '*':
            stack.append(o1 * o2)

print(stack[0])
