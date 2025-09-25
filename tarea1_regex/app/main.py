import sys
from .alphabet import ALPHABET
from .parser import parse
from .thompson import thompson
from .converter import afnd_to_afd
from .matcher import find_matches
from .utils import collect_sigma

USAGE = "Uso: python -m app.main \"ER\"   (ej: python -m app.main \"a.b.c\")"

def main():
    if len(sys.argv) < 2:
        print(USAGE); return
    regex = sys.argv[1]
    try:
        ast = parse(regex)
    except Exception as e:
        print(f"Error al parsear ER: {e}"); return
    sigma_usado = collect_sigma(ast)
    afnd = thompson(ast, sigma_usado)
    print(afnd.to_pretty())
    afd = afnd_to_afd(afnd)
    print(afd.to_pretty())

    while True:
        try:
            s = input("Ingrese cadena a evaluar (@ para terminar): ")
        except EOFError:
            break
        if s == "@":
            print("\nFin!!."); break
        # validar alfabeto de la cadena
        bad = [ch for ch in s if ch not in ALPHABET]
        if bad:
            print(f"Error: símbolo(s) fuera del alfabeto: {''.join(bad)}"); continue
        matches = find_matches(afd, s)
        if matches:
            print("\nCoincidencias encontradas:\n")
            for pos, sub in matches:
                print(f"Posición {pos}: {sub}")
            print()
        else:
            print("\nSin coincidencias.\n")

if __name__ == '__main__':
    main()
