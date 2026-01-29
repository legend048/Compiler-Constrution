def is_comment(statement: str) -> bool:
    stripped = statement.strip()
    if stripped.startswith('#') or stripped.startswith('//'):
        return True    
    if stripped.startswith('"""') or stripped.startswith("'''"):
        return True
    return False

statement = input("Enter a statement for checking for comment: ")

result = "Comment" if is_comment(statement) else "Not a comment"
print(f"{statement:40} -> {result}")
