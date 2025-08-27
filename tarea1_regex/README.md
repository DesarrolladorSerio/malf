# Tarea 1 — Máquinas Abstractas y Lenguajes Formales (Python, modular)

Implementa:

1) Parser de ER (alfabeto validado)  
2) Construcción AFND (Thompson)  
3) Conversión AFND → AFD (conjunto de estados)  
4) Búsqueda de coincidencias en cadena (índices base 0, como en el ejemplo)  

## Estructura

```
tarea1_regex/
├─ app/
│  ├─ __init__.py
│  ├─ main.py                 # CLI
│  ├─ alphabet.py             # Alfabeto permitido y validación
│  ├─ tokens.py               # Tokenizador
│  ├─ ast_nodes.py            # Nodos del AST
│  ├─ parser.py               # Parser a AST (precedencia: * > . > |)
│  ├─ automata.py             # Clases AFND/AFD + pretty print
│  ├─ thompson.py             # Construcción AFND (Thompson)
│  ├─ converter.py            # AFND → AFD (subset construction)
│  ├─ matcher.py              # Búsqueda de coincidencias con el AFD
│  └─ utils.py                # Utilidades (e.g., sets ordenados)
└─ README.md
```

## Uso

```bash
python -m app.main "a.b.c"
```

Luego ingresa cadenas; `@` cierra el programa.
