# Proyecto: Expresiones Regulares y Autómatas

Este proyecto implementa un sistema para analizar expresiones regulares (ER), construir sus autómatas equivalentes y verificar cadenas de entrada en base a dichas ER.  
Se utilizan algoritmos clásicos como **Thompson** (para construir un AFND) y **construcción de subconjuntos** (para convertirlo en AFD).

---

## 📌 Diseño de la Solución

1. **Entrada**: el usuario proporciona una expresión regular en notación explícita (usando `.` para concatenación, `|` para unión, `*` para cerradura de Kleene, `ε` para vacío y `Φ` para conjunto vacío).
2. **Tokenización**: la expresión se divide en símbolos con el módulo `tokens.py`.
3. **Parser**: se convierte la ER a postfix con el algoritmo *Shunting-yard* y se construye un **Árbol de Sintaxis Abstracta (AST)** (`parser.py`).
4. **Construcción AFND**: se aplica el algoritmo de **Thompson** para obtener un AFND (`thompson.py`).
5. **Conversión a AFD**: el AFND se transforma en AFD mediante la **construcción de subconjuntos** (`converter.py`).
6. **Verificación**: el AFD se usa para recorrer cadenas ingresadas por el usuario y encontrar coincidencias (`matcher.py`).

---

## 🧩 Descripción de Módulos Principales

- **`alphabet.py`**: define el alfabeto válido y funciones de validación.  
- **`ast_nodes.py`**: nodos del AST (`Literal`, `Concat`, `Union`, `Star`, `Epsilon`, `EmptySet`).  
- **`tokens.py`**: clase `Token` y función `tokenize`.  
- **`parser.py`**: función `parse`, que construye el AST desde una ER.  
- **`thompson.py`**: algoritmo de Thompson para construir un AFND.  
- **`automata.py`**: definición de clases `AFND` y `AFD`.  
- **`converter.py`**: funciones para convertir AFND → AFD.  
- **`matcher.py`**: función `find_matches` para encontrar subcadenas que cumplen la ER.  
- **`utils.py`**: funciones auxiliares (`collect_sigma`, `set_to_str`).  
- **`main.py`**: punto de entrada del programa, que orquesta todo el flujo.  

---

## ⚙️ Instrucciones de Uso

1. **Requisitos previos**  
   - Python 3.10 o superior instalado.

2. **Ejecutar el programa**  
   En la consola:  
   ```
   python -m app.main "a.b*|c"
   ```
   Donde `"a.b*|c"` es la expresión regular a analizar.

3. **Verificación de cadenas**  
   - El programa pedirá ingresar cadenas.  
   - Para finalizar, ingresa `@`.  

   **Ejemplo:**  
   ```
   Ingrese cadena a evaluar (@ para terminar): abbb
   Coincidencias encontradas:
   Posición 0: abbb
   ```

---

## ✅ Proceso de Verificación

- Se valida que la cadena ingresada contenga únicamente símbolos del alfabeto definido.  
- El AFD recorre la cadena carácter por carácter.  
- Cada vez que se alcanza un estado de aceptación, se registra la posición y la subcadena coincidente.  
- Se muestran todas las coincidencias encontradas.  

---

## 📖 Referencia

Navarro, G. (2021). *Teoría de la Computación: Lenguajes formales, computabilidad y complejidad: Apuntes y ejercicios*. Universidad de Chile.  

---
