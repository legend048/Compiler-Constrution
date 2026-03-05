def recognize_regex(input_string):
    matched_patterns = []
    if all(c == 'A' for c in input_string):
        matched_patterns.append("A*")
    remainder = input_string.lstrip('A')
    if remainder and all(c == 'B' for c in remainder):
        matched_patterns.append("A*B+")
    return matched_patterns

user_input = input("Enter String: ")
matches = recognize_regex(user_input)
if matches:
    print(f"'{user_input}' matches: {', '.join(matches)}")
else:
    print(f"'{user_input}' matches: None")
