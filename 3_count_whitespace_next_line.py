def count_whitespace_and_newlines(input_string):
    lines = input_string.split('\n')    
    indent_count = 0
    whitespace_count = 0
    newline_count = 0
    for line in lines:
        leading_whitespace = len(line) - len(line.lstrip())
        indent_count += leading_whitespace
    
        cleaned_line = line.lstrip()
        for char in cleaned_line:
            if char == ' ' or char == '\t':
                whitespace_count += 1    
    newline_count = input_string.count('\n')
    return indent_count, whitespace_count, newline_count

with open("3_count_whitespace_next_line.py", "r") as file:
    input_string = file.read()

indent_count, whitespace_count, newline_count = count_whitespace_and_newlines(input_string)

print(f"No. of indentation chars: {indent_count}")
print(f"No. of whitespace chars (non-indent): {whitespace_count}")
print(f"No. of newline chars: {newline_count}")