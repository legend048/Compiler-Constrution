import keyword

def is_valid_identifier(identifier):    
    if not identifier.isidentifier():
        return False
    if keyword.iskeyword(identifier):
        return False
    
    return True

test = input("Enter an identifier to check if it's valid: ")
result = is_valid_identifier(test)
print(f"'{test}': {result}")