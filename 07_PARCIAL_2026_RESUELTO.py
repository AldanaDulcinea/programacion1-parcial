import csv


# EJERCICIO 1

def leer_ventas(nombre_archivo):
    ventas = []

    try:
        with open(nombre_archivo, "r") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)

            for fila in lector:
                venta = dict(zip(encabezado, fila))
                venta["precio"] = float(venta["precio"])
                venta["cantidad"] = int(venta["cantidad"])
                ventas.append(venta)

    except FileNotFoundError:
        print("No se encontró el archivo.")
        return []

    except ValueError:
        print("Hay un valor incorrecto en los datos.")
        return []

    return ventas


# EJERCICIO 2.1

def platos_distintos(ventas):
    platos = set()

    for venta in ventas:
        platos.add(venta["plato"])

    return platos


# EJERCICIO 2.2

def ingresos_por_categoria(ventas):
    ingresos = {}

    for venta in ventas:
        categoria = venta["categoria"]
        ingreso = venta["precio"] * venta["cantidad"]

        if categoria not in ingresos:
            ingresos[categoria] = 0

        ingresos[categoria] += ingreso

    return ingresos


# EJERCICIO 2.3

def plato_mas_vendido(ventas):
    cantidades = {}

    for venta in ventas:
        plato = venta["plato"]
        cantidad = venta["cantidad"]

        if plato not in cantidades:
            cantidades[plato] = 0

        cantidades[plato] += cantidad

    plato_max = None
    cantidad_max = -1

    for plato in cantidades:
        if cantidades[plato] > cantidad_max:
            plato_max = plato
            cantidad_max = cantidades[plato]

    return (plato_max, cantidad_max)


# EJERCICIO 3

def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo)

    if not ventas:
        return

    platos = platos_distintos(ventas)
    ingresos = ingresos_por_categoria(ventas)
    plato, cantidad = plato_mas_vendido(ventas)

    print("Platos distintos vendidos:", len(platos))
    print(f"Plato más vendido: {plato} ({cantidad} unidades)")
    print("Ingresos por categoría:")

    for categoria in ingresos:
        print(f"{categoria}: ${ingresos[categoria]:.2f}")

    ingreso_total = sum(ingresos.values())
    print(f"Ingreso total: ${ingreso_total:.2f}")
