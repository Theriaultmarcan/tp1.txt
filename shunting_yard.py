def tokenize(expression: str) -> list[str]:
    tokens = []
    token_courant = ""
    for i, char in enumerate(expression):
        if char.isspace():
            if token_courant:
                tokens.append(token_courant)
                token_courant = ""
        elif char in "+*/()":
            if token_courant:
                tokens.append(token_courant)
                token_courant = ""
            tokens.append(char)
        elif char == "-":
            if token_courant:
                tokens.append(token_courant)
                token_courant = ""
            if i == 0 or (tokens and tokens[-1] in "+-*/("):
                token_courant += char
            else:
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
        try :
            float(token)
            sortie.append(token)
        except ValueError:
            if token in priorite:
                while (pile_ope and pile_ope[-1] != "(" and
                       priorite[pile_ope[-1]] >= priorite[token]):
                    sortie.append(pile_ope.pop())
                pile_ope.append(token)
            elif token == "(":
                pile_ope.append(token)
            elif token == ")":
                while pile_ope and pile_ope[-1] != "(":
                    sortie.append(pile_ope.pop())
                if not pile_ope:
                    raise ValueError("parenthèses non appariées")
                pile_ope.pop()
            else:
                raise ValueError(f"token inconnu: {token}")
    while pile_ope:
        if pile_ope[-1] == "(":
            raise ValueError("parenthèses non appariées")
        sortie.append(pile_ope.pop())
    return sortie

def evaluate_postfix(tokens: list[str]) -> float:
    pile = []
    for token in tokens:
        try:
            pile.append(float(token))
        except ValueError:
            if len(pile) < 2:
                raise ValueError("expression invalide, opérateur sans suffisamment d'opérandes")
            b = pile.pop()
            a = pile.pop()
            if token == "+":
                pile.append(a + b)
            elif token == "-":
                pile.append(a - b)
            elif token == "*":
                pile.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ValueError("division par zéro")
                pile.append(a / b)
            else:
                raise ValueError(f"opérateur inconnu: {token}")
    if len(pile) != 1:
        raise ValueError("expression invalide, opérandes restants dans la pile")
    return pile[0]
