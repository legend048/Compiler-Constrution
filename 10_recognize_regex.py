import re

def recognize_regex(input_string):
    patterns = {
        "A*": r"^A*$",
        "A*B+": r"^A*B+$"
    }
    matched_patterns = []
    for name, regex in patterns.items():
        if re.fullmatch(regex, input_string):
            matched_patterns.append(name)            
    return matched_patterns

user_input = input("Enter String: ")
matches = recognize_regex(user_input)
if matches:
    print(f"'{user_input}' matches: {', '.join(matches)}")
else:
    print(f"'{user_input}' matches: None")
