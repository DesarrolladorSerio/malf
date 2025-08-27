from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Token:
    kind: str  # LITERAL, UNION, CONCAT, STAR, LPAREN, RPAREN, EPSILON, EMPTYSET
    value: str

def tokenize(regex: str) -> List[Token]:
    tokens = []
    i = 0
    while i < len(regex):
        ch = regex[i]
        if ch.isspace():
            i += 1
            continue
        if ch == '|':
            tokens.append(Token('UNION', ch))
        elif ch == '.':
            tokens.append(Token('CONCAT', ch))
        elif ch == '*':
            tokens.append(Token('STAR', ch))
        elif ch == '(':
            tokens.append(Token('LPAREN', ch))
        elif ch == ')':
            tokens.append(Token('RPAREN', ch))
        elif ch == 'ε':
            tokens.append(Token('EPSILON', ch))
        elif ch == 'Φ':
            tokens.append(Token('EMPTYSET', ch))
        else:
            tokens.append(Token('LITERAL', ch))
        i += 1
    return tokens
