# 04 — Funciones y flujo

## Estructura básica

```python
def nombre_funcion(parametro):
    instrucciones
    return resultado
```

### Parámetro vs argumento

```python
def doble(numero):
    return numero * 2
```

`numero` es el parámetro.

```python
doble(5)
```

`5` es el argumento.

---

## `return` vs `print()`

### `return`
Devuelve un valor para usar después.

```python
def doble(n):
    return n * 2

x = doble(5)
```

`x` vale `10`.

### `print()`
Muestra algo en pantalla.

```python
def doble(n):
    print(n * 2)

x = doble(5)
```

Se ve `10`, pero `x` vale `None`.

### Puede haber ambos

```python
def doble(n):
    resultado = n * 2
    print(resultado)
    return resultado
```

---

## `return` corta la función

```python
def ejemplo(x):
    return x * 2
    print("esto nunca se ejecuta")
```

---

## Función que reutiliza otra

```python
def sumar(a, b):
    return a + b


def doble_de_suma(a, b):
    resultado = sumar(a, b)
    return resultado * 2
```

La salida de una función puede ser la entrada de otra.

---

## Patrón tipo parcial

```python
def leer_datos(nombre_archivo):
    ...
    return datos


def analizar_datos(datos):
    ...
    return resumen


def generar_informe(nombre_archivo):
    datos = leer_datos(nombre_archivo)
    resumen = analizar_datos(datos)

    print(resumen)
```

Pensalo como una cadena:

```text
archivo
  ↓
leer_datos()
  ↓
lista/datos
  ↓
analizar_datos()
  ↓
resultado
  ↓
generar_informe()
  ↓
print
```

---

## Variables locales

Las variables creadas dentro de una función son, en general, locales a esa función.

```python
def ejemplo():
    x = 10
    return x
```

No dependas de variables externas si la consigna pide que la función reciba los datos como parámetros.

---

## Cómo pensar una función antes de programarla

Escribí primero:

```text
RECIBE:
DEVUELVE/IMPRIME:
RECORRE:
CONDICIÓN:
ESTRUCTURA QUE NECESITO CREAR:
OPERACIÓN:
```

Ejemplo:

```text
RECIBE: lista de ventas
DEVUELVE: ingreso total
RECORRE: cada venta
CONDICIÓN: ninguna
ESTRUCTURA: total = 0
OPERACIÓN: precio * cantidad
```

Después:

```python
def ingreso_total(ventas):
    total = 0

    for venta in ventas:
        total += venta["precio"] * venta["cantidad"]

    return total
```

---

## Señales de que la función está mal armada

- usa datos que no recibe ni crea;
- imprime cuando debía devolver;
- no tiene `return` y después querés guardar su resultado;
- tiene `return` dentro de un `for` sin querer cortar temprano;
- hace todo en una función gigante aunque la consigna pide reutilizar funciones anteriores;
- modifica variables innecesariamente en vez de construir un resultado claro.
