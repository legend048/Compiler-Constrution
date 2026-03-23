def infix_to_postfix(expression):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack, output = [], []
    for char in expression:
        if char.isalnum(): output.append(char)
        elif char == '(': stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(': output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and (prec.get(stack[-1], 0) > prec.get(char, 0)
            if char == '^' else prec.get(char, 0) <= prec.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(char)
    while stack: output.append(stack.pop())
    return "".join(output)

user_input = input("Enter Infix Expression: ")
print("Postfix Expression: ", infix_to_postfix(user_input))