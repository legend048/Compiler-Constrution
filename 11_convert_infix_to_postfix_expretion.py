def infix_to_postfix(expression):
    p, s, o, i = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}, [], [], 0
    while i < len(expression):
        c = expression[i]
        if c.isspace(): i += 1; continue
        if c.isalnum():
            j = i
            while j < len(expression) and expression[j].isalnum(): j += 1
            o.append(expression[i:j]); i = j; continue
        if c == ')':
            while s and s[-1] != '(': o.append(s.pop())
            if s: s.pop()
        elif c == '(': s.append(c)
        else:
            while s and s[-1] != '(' and (p[s[-1]] > p[c] if c == '^' else p[c] <= p[s[-1]]): o.append(s.pop())
            s.append(c)
        i += 1
    while s: o.append(s.pop())
    return " ".join(o)

user_input = input("Enter Infix Expression: ")
print("Postfix Expression: ", infix_to_postfix(user_input))