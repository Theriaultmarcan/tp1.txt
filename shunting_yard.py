def tokenize(expression: str) -> list[str]:
    tokens = []
    token_courant = ""
    for char in expression:
        if char.isspace():
            if token_courant:
                tokens.append(token_courant)
                token_courant = ""
        elif char in "+-*/()":
            if token_courant:
                tokens.append(token_courant)
                token_courant = ""
            tokens.append(char)
        else:
            token_courant += char
    if token_courant:
        tokens.append(token_courant)
    return tokens

def infix_to_postfix(tokens: list[str]) -> list[str]:
    priorite = {"+": 1, "-": 1, "*": 2, "/": 2}
    sortie = []
    pile_ope = []
    for token in tokens:
        if token.isdigit():
            sortie.append(token)
        elif token in priorite:
            while (pile_ope and pile_ope[-1] != "(" and
                   priorite[pile_ope[-1]] >= priorite[token]):
                sortie.append(pile_ope.pop())
            pile_ope.append(token)
        elif token == "(":
            pile_ope.append(token)
        elif token == ")":
            while pile_ope and pile_ope[-1] != "(":
                sortie.append(pile_ope.pop())
            if pile_ope:
                pile_ope.pop() 
    while pile_ope:
        sortie.append(pile_ope.pop())
    return sortie

def evaluate_postfix(tokens: list[str]) -> float:
    pile = []
    for token in tokens:
        if token.isdigit():
            pile.append(float(token))
        else:
            b = pile.pop()
            a = pile.pop()
            if token == "+":
                pile.append(a + b)
            elif token == "-":
                pile.append(a - b)
            elif token == "*":
                pile.append(a * b)
            elif token == "/":
                pile.append(a / b)
    return pile[0]