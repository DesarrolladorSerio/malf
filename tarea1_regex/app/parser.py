from .tokens import tokenize, Token
from .ast_nodes import Literal, Epsilon, EmptySet, Concat, Union, Star, RegexNode
from .alphabet import validate_regex_chars

# Precedencias: STAR > CONCAT > UNION
PREC = {
    'STAR': 3,
    'CONCAT': 2,
    'UNION': 1,
}

def parse(regex: str) -> RegexNode:
    """
    Shunting-yard a postfix y luego construcción de AST.
    ER explícita (concatenación con '.').
    """
    validate_regex_chars(regex)
    tokens = tokenize(regex)
    # a postfix
    output = []
    opstack = []
    for t in tokens:
        if t.kind in ('LITERAL', 'EPSILON', 'EMPTYSET'):
            output.append(t)
        elif t.kind in ('UNION', 'CONCAT', 'STAR'):
            if t.kind == 'STAR':
                # STAR unario posfijo
                while opstack and opstack[-1].kind == 'STAR' and PREC['STAR'] <= PREC['STAR']:
                    output.append(opstack.pop())
                opstack.append(t)
            else:
                while opstack and opstack[-1].kind in PREC and PREC[opstack[-1].kind] >= PREC[t.kind]:
                    output.append(opstack.pop())
                opstack.append(t)
        elif t.kind == 'LPAREN':
            opstack.append(t)
        elif t.kind == 'RPAREN':
            while opstack and opstack[-1].kind != 'LPAREN':
                output.append(opstack.pop())
            if not opstack:
                raise ValueError("Paréntesis desbalanceados")
            opstack.pop()
        else:
            raise ValueError(f"Token inesperado: {t}")
    while opstack:
        if opstack[-1].kind in ('LPAREN', 'RPAREN'):
            raise ValueError("Paréntesis desbalanceados al finalizar")
        output.append(opstack.pop())

    # Construcción AST desde postfix
    stack = []
    for t in output:
        if t.kind == 'LITERAL':
            stack.append(Literal(t.value))
        elif t.kind == 'EPSILON':
            stack.append(Epsilon())
        elif t.kind == 'EMPTYSET':
            stack.append(EmptySet())
        elif t.kind == 'STAR':
            if not stack:
                raise ValueError("Operador * sin operando")
            n = stack.pop()
            stack.append(Star(n))
        elif t.kind in ('UNION', 'CONCAT'):
            if len(stack) < 2:
                raise ValueError(f"Operador {t.value} con operandos insuficientes")
            b = stack.pop()
            a = stack.pop()
            if t.kind == 'UNION':
                stack.append(Union(a, b))
            else:
                stack.append(Concat(a, b))
        else:
            raise ValueError(f"Token inesperado en postfix: {t}")
    if len(stack) != 1:
        raise ValueError("ER mal formada (sobran operandos u operadores)")
    return stack[0]
