def tokenize(expression: str) -> list[str]:
    tokens = []
    current_token = ""
    for char in expression:
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif char in "+-*/()":
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
    return tokens