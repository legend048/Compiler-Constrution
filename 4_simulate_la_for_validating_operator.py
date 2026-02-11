def lexical_analyzer(input_string):
    results = []
    i = 0
    sym_ops = [
        '//=', '**=', '>>=', '<<=', '//', '**', '==', '!=', '<=', '>=',
        '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<', '>>',
        '+', '-', '*', '/', '%', '=', '<', '>', '&', '|', '^', '~', ':', ':='
    ]
    keywords = {
        'and', 'or', 'not', 'in', 'is', 'if', 'else', 'elif', 'return', 'yield'
    }
    sym_ops.sort(key=len, reverse=True)
    
    while i < len(input_string):
        if input_string[i].isspace(): i += 1; continue
        
        if input_string[i] in ('"', "'"):
            end = input_string.find(input_string[i], i + 1)
            end = len(input_string) if end == -1 else end + 1
            results.append(f"'{input_string[i:end]}' -> Not an Operator")
            i = end; continue
            
        for op in sym_ops:
            if input_string.startswith(op, i):
                results.append(f"'{op}' -> Valid Operator")
                i += len(op); break
        else:
            start = i
            while i < len(input_string) and (input_string[i].isalnum() or input_string[i] == '_'): i += 1
            if i == start: i += 1
            token = input_string[start:i]
            
            if token in keywords: results.append(f"'{token}' -> Valid Operator")
            elif token in sym_ops: results.append(f"'{token}' -> Valid Operator")
            
    return results

input_str = input("Enter Statement: ")
result = lexical_analyzer(input_str)
print("Analysis Results:")
print(*result, sep='\n')
