ALPHABET = set(
    [chr(c) for c in range(ord('a'), ord('z')+1)] +
    [chr(c) for c in range(ord('A'), ord('Z')+1)] +
    [chr(c) for c in range(ord('0'), ord('9')+1)] +
    ['?', '@']
)

# Operadores de ER
OPS = {'|', '.', '*', '(', ')', 'ε', 'Φ'}

def validate_regex_chars(regex: str):
    """
    Verifica que la ER solo contenga símbolos del alfabeto permitido
    y operadores válidos.
    """
    for ch in regex:
        if ch.isspace():
            continue
        if ch in OPS or ch in ALPHABET:
            continue
        raise ValueError(f"Símbolo inválido en ER: {repr(ch)}")

def pretty_sigma():
    return "{" + ",".join(sorted(ALPHABET)) + "}"
