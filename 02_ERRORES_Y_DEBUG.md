# 02 — Errores frecuentes y debugging

Esta hoja está pensada para cuando el código **no hace lo que esperabas**.

## 1. `return` adentro del `for`

### Síntoma
La función se frena en la primera coincidencia.

### MAL
```python
for edad in edades:
    if edad >= 18:
        contador += 1
        return contador
```

### BIEN
```python
for edad in edades:
    if edad >= 18:
        contador += 1

return contador
```

**Idea:** si necesitás recorrer toda la colección, el `return` suele ir después del `for`.

---

## 2. Usar el elemento recorrido como contador

### MAL
```python
for edad in edades:
    if edad >= 18:
        edad += 1
```

Esto modifica `edad`; no cuenta personas.

### BIEN
```python
contador = 0

for edad in edades:
    if edad >= 18:
        contador += 1
```

---

## 3. `+` versus `+=`

```python
total + valor
```
Calcula, pero no guarda el resultado.

```python
total += valor
```
Equivale a:
```python
total = total + valor
```

---

## 4. `print()` no reemplaza a `return`

```python
def doble(n):
    print(n * 2)

x = doble(5)
```

En pantalla aparece `10`, pero `x` vale `None`.

Si la consigna dice **devuelva**:
```python
def doble(n):
    return n * 2
```

---

## 5. Indentación incorrecta en acumulación por categoría

### MAL
```python
if categoria not in gastos:
    gastos[categoria] = 0
    gastos[categoria] += gasto
```

Así se suma solo la primera aparición.

### BIEN
```python
if categoria not in gastos:
    gastos[categoria] = 0

gastos[categoria] += gasto
```

---

## 6. Olvidar inicializar

Antes de usar:

```python
contador += 1
```

debe existir:
```python
contador = 0
```

Antes de:
```python
resultado.append(x)
```

debe existir:
```python
resultado = []
```

Antes de:
```python
totales[categoria] = ...
```

debe existir:
```python
totales = {}
```

---

## 7. Datos numéricos del CSV como strings

Si `fila["precio"]` contiene `"150"`, esto puede romper cálculos o producir resultados inesperados.

Convertir:
```python
precio = float(fila["precio"])
cantidad = int(fila["cantidad"])
```

---

## 8. Clave equivocada de un diccionario

Si el CSV tiene:
```text
titulo,genero,precio
```

esto funciona:
```python
fila["genero"]
```

esto no:
```python
fila["género"]
```

Las claves deben coincidir exactamente.

---

## 9. `=` versus `==`

```python
x = 5
```
Asigna.

```python
x == 5
```
Compara.

En un `if` normalmente querés comparar:
```python
if x == 5:
```

---

## 10. Función devuelve `None`

Si ves `None`, revisá si la función tiene `return`.

```python
def sumar(a, b):
    resultado = a + b
```

No devuelve explícitamente nada → `None`.

Correcto:
```python
def sumar(a, b):
    resultado = a + b
    return resultado
```

---

# Debugging rápido durante el parcial

Agregá temporalmente `print()` para mirar el estado del programa.

```python
for venta in ventas:
    print("VENTA:", venta)

    genero = venta["genero"]
    print("GENERO:", genero)

    ingreso = venta["precio"] * venta["cantidad"]
    print("INGRESO:", ingreso)
```

Para acumuladores:
```python
print("ANTES:", total)
total += valor
print("DESPUÉS:", total)
```

Para diccionarios:
```python
print("DICCIONARIO AHORA:", ingresos)
```

Cuando encuentres el error, podés sacar esos `print()`.

---

# Cómo leer un traceback

No hace falta entender todo. Buscá:

1. **la última línea** → tipo de error;
2. **la línea de tu archivo** donde ocurrió;
3. qué variable u operación aparece ahí.

Ejemplos frecuentes:

```text
FileNotFoundError
```
→ no encontró el archivo.

```text
KeyError: 'precio'
```
→ esa clave no existe en el diccionario.

```text
ValueError
```
→ una conversión, por ejemplo `int("hola")`, no pudo hacerse.

```text
TypeError
```
→ estás combinando tipos de forma inválida.

```text
IndentationError
```
→ problema de sangría/indentación.

```text
NameError
```
→ usaste un nombre de variable que Python no conoce.

---

# Estrategia si algo da mal

- Probá con 2 o 3 datos pequeños.
- Imprimí la variable del `for`.
- Imprimí el acumulador antes y después.
- Verificá dónde está indentado el `return`.
- Revisá si la consigna pide contar, sumar, guardar o agrupar.
- Revisá tipos (`str`, `int`, `float`).
- Revisá nombres exactos de claves.
