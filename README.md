# Programación 1 — Machete para el primer parcial

Este repositorio está pensado para **consultar durante el parcial a cuaderno abierto**. No intenta resumir todo Python: prioriza los patrones que aparecen en los **primeros parciales reales** y en las **Unidades 1 a 4** de Programación 1.

## Cómo usarlo durante el parcial

Si te trabás, no leas todo. Entrá al archivo según tu duda:

- **[`00_MACHETE_RAPIDO.md`](00_MACHETE_RAPIDO.md)** → “¿cómo era la sintaxis de...?”
- **[`01_PLANTILLAS_PARCIAL.py`](01_PLANTILLAS_PARCIAL.py)** → plantillas copiables/adaptables.
- **[`02_ERRORES_Y_DEBUG.md`](02_ERRORES_Y_DEBUG.md)** → si el código corre mal, devuelve algo raro o se frena antes.
- **[`03_CSV_Y_DICCIONARIOS.md`](03_CSV_Y_DICCIONARIOS.md)** → CSV, `DictReader`, listas de diccionarios y acumulación por categoría.
- **[`04_FUNCIONES_Y_FLUJO.md`](04_FUNCIONES_Y_FLUJO.md)** → `def`, parámetros, `return`, `print`, funciones que llaman a otras.
- **[`05_CHECKLIST_ENTREGA.md`](05_CHECKLIST_ENTREGA.md)** → revisión final antes de entregar.
- **[`06_EJEMPLO_INTEGRADOR.py`](06_EJEMPLO_INTEGRADOR.py)** → ejemplo completo del tipo de arquitectura que puede aparecer.

---

## Qué aparece en el material de U1–U4

### U1 — Introducción a Python
- variables y asignaciones
- condicionales
- ciclos
- números enteros y flotantes
- strings
- listas
- ejecución y debugging básico
- línea de comandos

### U2 — Estructuras y funciones
- lectura de archivos
- funciones
- listas
- tuplas
- conjuntos (`set`)
- diccionarios

### U3 — Contenedores y errores
- elegir entre lista, diccionario y conjunto
- bugs y debugging
- ejecución desde consola
- parámetros desde línea de comandos

### U4 — Trabajando con datos
- lectura de CSV
- secuencias
- `collections.Counter`
- impresión con formato
- integración de funciones + estructuras de datos

---

## Qué muestran los primeros parciales reales

### P1 2025 — patrón central

El examen se organiza como un programa encadenado:

1. Leer `ventas.csv`.
2. Construir una **lista de diccionarios**.
3. Manejar un error frecuente como `FileNotFoundError`.
4. Calcular `precio * cantidad`.
5. Acumular ingresos **por género** en un diccionario.
6. Hacer una función final que use las anteriores e imprima un informe.
7. Poder ejecutar el programa desde el sistema operativo.

### P1 2024 — patrón central

También parte de un CSV y pide:

1. Leer datos como lista de diccionarios.
2. Extraer valores de una categoría/ciudad.
3. Calcular un promedio.
4. Aplicar una condición sobre los datos.
5. Reutilizar funciones anteriores para generar un reporte.
6. Había además un ejercicio de gráfico con `matplotlib`.

### Conclusión práctica

El núcleo que más conviene dominar es:

```text
CSV
 ↓
lista de diccionarios
 ↓
for
 ↓
if / cálculo
 ↓
contador, acumulador, lista nueva o diccionario acumulador
 ↓
return
 ↓
otra función usa ese resultado
 ↓
print / informe
```

---

# Mapa de emergencia: si la consigna dice...

| La consigna dice... | Pensá en... |
|---|---|
| “reciba...” | parámetro de una función |
| “devuelva...” | `return` |
| “imprima / muestre...” | `print()` |
| “recorra...” | `for` |
| “si...” | `if` |
| “cuántos...” | contador: `contador += 1` |
| “total / suma...” | acumulador: `total += valor` |
| “guardar los que cumplen...” | lista vacía + `.append()` |
| “por género / categoría / tipo...” | diccionario acumulador |
| “leer CSV...” | `open()` + `csv.DictReader()` |
| “archivo no encontrado” | `try` / `except FileNotFoundError` |
| “usar las funciones anteriores” | composición de funciones |
| “valores únicos” | `set` |
| “contar apariciones” | contador manual o `Counter` |

---

## Los errores que más fácil pueden hacer perder puntos

1. Poner `return` adentro del `for` cuando necesitás recorrer toda la colección.
2. Usar la variable que recorre el `for` como contador.
3. Confundir `+` con `+=`.
4. Usar `print()` cuando la consigna dice **devuelva**.
5. Indentar la acumulación dentro de un `if` y sumar solo la primera aparición de cada categoría.
6. Olvidar que los datos de un CSV suelen llegar como strings y después intentar multiplicar/sumar sin convertir.
7. Confundir `=` con `==`.
8. Usar una clave de diccionario que no coincide exactamente con el encabezado del CSV.
9. No inicializar antes un contador (`0`), una lista (`[]`) o un diccionario (`{}`).
10. Hacer una función gigante cuando la consigna pide reutilizar funciones anteriores.

---

## Prioridad si quedan pocos minutos para repasar

**Muy alta:** funciones, `for`, `if`, `return`, listas, diccionarios, listas de diccionarios, acumuladores, CSV, `DictReader`, conversiones `int/float`, `try/except`.

**Alta:** `.append()`, recorrer diccionarios, composición de funciones, impresión con formato, debugging.

**Media:** strings, `range`, `while`, tuplas, sets, `Counter`, consola.

**Baja salvo que la consigna lo pida:** gráficos con `matplotlib` (apareció en P1 2024, pero no en el patrón principal del P1 2025).

---

## Regla final

Antes de programar, traducí la consigna a una mini receta:

```text
¿Qué recibe?
¿Qué tiene que devolver o imprimir?
¿Qué tengo que recorrer?
¿Necesito if?
¿Estoy contando, sumando, guardando o agrupando?
¿Qué estructura necesito crear antes?
¿Los datos vienen como texto?
¿Tengo que reutilizar otra función?
```

Si respondés esas preguntas, después la sintaxis suele salir mucho más fácil.
