# 00 — Machete rápido

## Sintaxis mínima

```python
x = 5          # asignación
x == 5         # comparación
x += 1         # x = x + 1
```

```python
if condicion:
    ...
elif otra_condicion:
    ...
else:
    ...
```

```python
for elemento in coleccion:
    ...
```

```python
def funcion(parametro):
    ...
    return resultado
```

---

## `print()` vs `return`

```python
def doble(n):
    print(n * 2)
```

Muestra el valor, pero la función devuelve `None`.

```python
def doble(n):
    return n * 2
```

No necesariamente muestra nada, pero devuelve el valor para poder usarlo.

**Consigna dice “devuelva” → `return`.**

**Consigna dice “imprima” → `print()`.**

`return` además termina la función inmediatamente.

---

## Contar, sumar o guardar

### Contar cuántos

```python
contador = 0

for x in datos:
    if condicion:
        contador += 1
```

### Sumar valores

```python
total = 0

for x in datos:
    if condicion:
        total += x
```

### Guardar elementos

```python
resultado = []

for x in datos:
    if condicion:
        resultado.append(x)
```

### Guardar elementos transformados

```python
resultado = []

for x in datos:
    resultado.append(x * 2)
```

---

## Listas

```python
numeros = [10, 20, 30]
```

```python
numeros[0]   # 10
numeros[1]   # 20
```

```python
numeros.append(40)
```

---

## Diccionarios

```python
persona = {
    "nombre": "Ana",
    "edad": 25
}
```

Acceder:

```python
persona["nombre"]
persona["edad"]
```

Agregar/modificar:

```python
persona["edad"] = 26
persona["ciudad"] = "Buenos Aires"
```

---

## Lista de diccionarios

```python
ventas = [
    {"titulo": "Rayuela", "precio": 20, "cantidad": 3},
    {"titulo": "El Aleph", "precio": 15, "cantidad": 2}
]
```

Acceso:

```python
ventas[0]
ventas[0]["precio"]
```

Recorrer:

```python
for venta in ventas:
    print(venta["titulo"])
```

---

## Acumular un total desde lista de diccionarios

```python
def ingreso_total(ventas):
    total = 0

    for venta in ventas:
        total += venta["precio"] * venta["cantidad"]

    return total
```

---

## Acumular por categoría

```python
def gastos_por_categoria(compras):
    gastos = {}

    for compra in compras:
        categoria = compra["categoria"]
        monto = compra["monto"]

        if categoria not in gastos:
            gastos[categoria] = 0

        gastos[categoria] += monto

    return gastos
```

**Clave:** inicializás en cero solo si la categoría es nueva, pero sumás siempre.

---

## CSV con `DictReader`

```python
import csv

with open(nombre_archivo, "r") as archivo:
    filas = csv.DictReader(archivo)

    for fila in filas:
        print(fila)
```

`DictReader` usa la primera fila del CSV como claves.

Si el CSV tiene:

```text
producto,categoria,precio
Pan,Comida,150
```

una fila se comporta aproximadamente como:

```python
{
    "producto": "Pan",
    "categoria": "Comida",
    "precio": "150"
}
```

---

## Convertir strings del CSV

```python
int(fila["cantidad"])
float(fila["precio"])
```

```python
"3"    -> int(...)   -> 3
"20"   -> float(...) -> 20.0
```

---

## CSV → lista de diccionarios

```python
import csv


def leer_productos(nombre_archivo):
    productos = []

    with open(nombre_archivo, "r") as archivo:
        filas = csv.DictReader(archivo)

        for fila in filas:
            producto = {
                "producto": fila["producto"],
                "categoria": fila["categoria"],
                "precio": float(fila["precio"])
            }

            productos.append(producto)

    return productos
```

---

## Manejar archivo inexistente

```python
try:
    with open(nombre_archivo, "r") as archivo:
        ...
except FileNotFoundError:
    print("No se encontró el archivo")
```

---

## Recorrer un diccionario

```python
ingresos = {
    "Ficción": 180,
    "Clásico": 30
}

for genero in ingresos:
    print(genero, ingresos[genero])
```

---

## Función que usa otra función

```python
def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo)
    ingresos = ingresos_por_genero(ventas)

    print(ingresos)
```

---

## Errores típicos

### `return` demasiado adentro

MAL si hay que recorrer todo:

```python
for x in datos:
    if condicion:
        contador += 1
        return contador
```

BIEN:

```python
for x in datos:
    if condicion:
        contador += 1

return contador
```

### Confundir elemento recorrido con contador

MAL:

```python
for edad in edades:
    if edad >= 18:
        edad += 1
```

BIEN:

```python
contador = 0

for edad in edades:
    if edad >= 18:
        contador += 1
```

### `+` no guarda

```python
total + valor      # calcula pero no actualiza total
```

```python
total += valor     # actualiza total
```

---

## Si te bloqueás

Traducí la consigna:

```text
¿qué recibe?
¿qué debe devolver o imprimir?
¿qué tengo que recorrer?
¿hay condición?
¿cuento, sumo, guardo o agrupo?
¿necesito lista, diccionario o número?
¿el CSV trae strings que debo convertir?
¿necesito usar otra función?
```
