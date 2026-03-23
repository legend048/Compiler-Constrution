def infix_to_postfix(expression):
    p, s, o, t = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}, [], [], ''
    for c in expression + ' ':
        if c.isalnum(): t += c; continue
        if t: o.append(t); t = ''
        if c.isspace(): continue
        if c == '(': s.append(c)
        elif c == ')':
            while s and s[-1] != '(': o.append(s.pop())
            if s: s.pop()
        else:
            while s and s[-1] != '(' and (p[s[-1]] > p[c] if c == '^' else p[c] <= p[s[-1]]): o.append(s.pop())
            s.append(c)
    while s: o.append(s.pop())
    return " ".join(o)

user_input = input("Enter Infix Expression: ")
print("Postfix Expression: ", infix_to_postfix(user_input))