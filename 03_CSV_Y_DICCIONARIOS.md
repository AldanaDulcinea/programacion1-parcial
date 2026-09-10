# 03 — CSV y diccionarios

Esta es una de las partes más importantes para el primer parcial.

## Idea general

Un archivo CSV puede transformarse en una **lista de diccionarios**.

Ejemplo de CSV:

```text
titulo,genero,precio,cantidad
Rayuela,Ficción,20,3
El Aleph,Clásico,15,2
```

Queremos terminar con algo conceptualmente así:

```python
ventas = [
    {"titulo": "Rayuela", "genero": "Ficción", "precio": 20.0, "cantidad": 3},
    {"titulo": "El Aleph", "genero": "Clásico", "precio": 15.0, "cantidad": 2}
]
```

---

## Leer con `csv.DictReader`

```python
import csv

with open("ventas.csv", "r") as archivo:
    filas = csv.DictReader(archivo)
```

`DictReader` usa la primera fila del CSV como claves.

Por eso una fila se comporta como:

```python
{
    "titulo": "Rayuela",
    "genero": "Ficción",
    "precio": "20",
    "cantidad": "3"
}
```

---

## Convertir tipos

Los valores del CSV suelen llegar como strings.

```python
precio = float(fila["precio"])
cantidad = int(fila["cantidad"])
```

---

## Patrón completo: CSV → lista de diccionarios

```python
import csv


def leer_ventas(nombre_archivo):
    ventas = []

    with open(nombre_archivo, "r") as archivo:
        filas = csv.DictReader(archivo)

        for fila in filas:
            venta = {
                "titulo": fila["titulo"],
                "genero": fila["genero"],
                "precio": float(fila["precio"]),
                "cantidad": int(fila["cantidad"])
            }

            ventas.append(venta)

    return ventas
```

### Qué mirar si no funciona
- ¿Importaste `csv`?
- ¿El archivo está en la ruta correcta?
- ¿Las claves coinciden exactamente con los encabezados?
- ¿Los números necesitan `int()` o `float()`?
- ¿El `return` quedó afuera del `for`?

---

## Recorrer una lista de diccionarios

```python
for venta in ventas:
    print(venta["titulo"])
```

En cada vuelta, `venta` es un diccionario distinto.

---

## Calcular un total

```python
def ingreso_total(ventas):
    total = 0

    for venta in ventas:
        total += venta["precio"] * venta["cantidad"]

    return total
```

---

## Acumular por género/categoría

```python
def ingresos_por_genero(ventas):
    ingresos = {}

    for venta in ventas:
        genero = venta["genero"]
        ingreso = venta["precio"] * venta["cantidad"]

        if genero not in ingresos:
            ingresos[genero] = 0

        ingresos[genero] += ingreso

    return ingresos
```

### Cómo leerlo mentalmente

```text
ventas   = lista que ya existe
ingresos = diccionario nuevo que voy construyendo
venta    = un diccionario de la lista en cada vuelta
genero   = clave de agrupación
ingreso  = valor que acumulo
```

---

## Extraer todos los valores de una clave

```python
def obtener_temperaturas(registros, ciudad):
    temperaturas = []

    for registro in registros:
        temperaturas.append(registro[ciudad])

    return temperaturas
```

Este patrón sirve cuando la consigna pide devolver una lista con todos los valores de un campo.

---

## Promedio manual

```python
def promedio(valores):
    total = 0

    for valor in valores:
        total += valor

    return total / len(valores)
```

Si puede haber lista vacía:

```python
if len(valores) == 0:
    return None
```

---

## Buscar el último valor que cumple una condición

```python
def ultimo_menor_o_igual(registros, clave_valor, limite, clave_anio):
    ultimo = None

    for registro in registros:
        if registro[clave_valor] <= limite:
            ultimo = registro[clave_anio]

    return ultimo
```

Si los registros están ordenados cronológicamente, `ultimo` se va reemplazando cada vez que encuentra una coincidencia y al final conserva la última.

---

## `try/except` al leer archivos

```python
def leer_ventas(nombre_archivo):
    ventas = []

    try:
        with open(nombre_archivo, "r") as archivo:
            filas = csv.DictReader(archivo)

            for fila in filas:
                ventas.append(dict(fila))

    except FileNotFoundError:
        print("No se encontró el archivo")

    return ventas
```

---

## `csv.reader` vs `csv.DictReader`

### `csv.reader`
Devuelve filas como listas.

```python
lector = csv.reader(archivo)
for fila in lector:
    print(fila[0])
```

### `csv.DictReader`
Devuelve filas asociadas a nombres de columnas.

```python
lector = csv.DictReader(archivo)
for fila in lector:
    print(fila["precio"])
```

Para parciales donde piden **lista de diccionarios**, `DictReader` suele ser especialmente cómodo.
