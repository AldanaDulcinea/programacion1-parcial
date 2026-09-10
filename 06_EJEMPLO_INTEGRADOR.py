# Ejemplo integrador tipo primer parcial
# --------------------------------------
# Archivo esperado: ventas.csv
# columnas: titulo,genero,precio,cantidad

import csv


def leer_ventas(nombre_archivo):
    ventas = []

    try:
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

    except FileNotFoundError:
        print("No se encontró el archivo")

    return ventas


def ingresos_por_genero(ventas):
    ingresos = {}

    for venta in ventas:
        genero = venta["genero"]
        ingreso = venta["precio"] * venta["cantidad"]

        if genero not in ingresos:
            ingresos[genero] = 0

        ingresos[genero] += ingreso

    return ingresos


def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo)
    ingresos = ingresos_por_genero(ventas)

    total = 0

    print("Ingresos por género:")

    for genero in ingresos:
        print(f"{genero}: ${ingresos[genero]:.2f}")
        total += ingresos[genero]

    print(f"Ingreso total: ${total:.2f}")


# Ejemplo de ejecución:
# generar_informe("ventas.csv")


# Qué revisar si algo falla:
# 1. ¿Existe el archivo?
# 2. ¿Los encabezados coinciden exactamente?
# 3. ¿precio y cantidad se convirtieron a número?
# 4. ¿return ventas está fuera del for?
# 5. ¿la suma por género queda fuera del if de inicialización?
# 6. ¿generar_informe usa las funciones anteriores?
