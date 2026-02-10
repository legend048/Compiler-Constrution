def is_operator(token):
    operators = [
        '+', '-', '*', '/', '//', '%', '**',
        '==', '!=', '<', '>', '<=', '>=',
        '=', '+=', '-=', '*=', '/=', '//=', '%=', '**=',
        '&=', '|=', '^=', '>>=', '<<=',
        'and', 'or', 'not',
        '&', '|', '^', '~', '<<', '>>',
        'in', 'not in',
        'is', 'is not',
        'if', 'else',
        ':='
    ]
    return token in operators

def lexical_analyzer(input_string):
    results = []
    i = 0
    operators = [
        '//=', '**=', '>>=', '<<=', '//', '**', '==', '!=', '<=', '>=',
        '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<', '>>',
        '+', '-', '*', '/', '%', '=', '<', '>', '&', '|', '^', '~', ':'
    ]
    operators.sort(key=len, reverse=True)
    while i < len(input_string):
        char = input_string[i]
        if char.isspace():
            i += 1
            continue
        matched = False
        for op in operators:
            if input_string[i:i+len(op)] == op:
                results.append(f"'{op}' -> Valid Operator")
                i += len(op)
                matched = True
                break
        if not matched:
            token = ''
            while i < len(input_string) and (input_string[i].isalnum() or input_string[i] == '_'):
                token += input_string[i]
                i += 1            
            if token:
                if is_operator(token):
                    results.append(f"'{token}' -> Valid Operator")
                else:
                    results.append(f"'{token}' -> Not an Operator")
            else:
                results.append(f"'{input_string[i]}' -> Not an Operator")
                i += 1    
    return results

input_str = input("Enter tokens separated by spaces: ")
result = lexical_analyzer(input_str)
print("Analysis Results:")
print(*result, sep='\n')
