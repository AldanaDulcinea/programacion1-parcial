# Plantillas para adaptar durante el parcial
# ------------------------------------------------------------
# IMPORTANTE:
# No copies una plantilla a ciegas. Primero identificá:
# - qué recibe la función
# - qué tiene que devolver/imprimir
# - qué colección recorre
# - si cuenta, suma, guarda o agrupa


# 1) CONTAR ELEMENTOS QUE CUMPLEN UNA CONDICIÓN

def contar_si(datos):
    contador = 0

    for x in datos:
        if x >= 0:  # reemplazar por la condición real
            contador += 1

    return contador


# 2) SUMAR VALORES QUE CUMPLEN UNA CONDICIÓN

def sumar_si(datos):
    total = 0

    for x in datos:
        if x >= 0:  # reemplazar condición
            total += x

    return total


# 3) FILTRAR Y DEVOLVER UNA LISTA NUEVA

def filtrar(datos):
    resultado = []

    for x in datos:
        if x >= 0:  # reemplazar condición
            resultado.append(x)

    return resultado


# 4) TRANSFORMAR CADA ELEMENTO Y GUARDARLO

def transformar(datos):
    resultado = []

    for x in datos:
        nuevo = x * 2  # reemplazar transformación
        resultado.append(nuevo)

    return resultado


# 5) SUMAR UN CÁLCULO DESDE UNA LISTA DE DICCIONARIOS

def total_desde_diccionarios(registros):
    total = 0

    for registro in registros:
        total += registro["precio"] * registro["cantidad"]

    return total


# 6) EXTRAER UNA COLUMNA/CAMPO DE UNA LISTA DE DICCIONARIOS

def extraer_valores(registros, clave):
    valores = []

    for registro in registros:
        valores.append(registro[clave])

    return valores


# 7) PROMEDIO MANUAL

def promedio(valores):
    total = 0

    for valor in valores:
        total += valor

    if len(valores) == 0:
        return None

    return total / len(valores)


# 8) ACUMULAR POR CATEGORÍA EN UN DICCIONARIO

def acumular_por_categoria(registros):
    totales = {}

    for registro in registros:
        categoria = registro["categoria"]
        valor = registro["monto"]

        if categoria not in totales:
            totales[categoria] = 0

        totales[categoria] += valor

    return totales


# 9) BUSCAR EL MAYOR VALOR Y RECORDAR QUÉ ELEMENTO LO TENÍA

def elemento_con_mayor_valor(registros):
    mejor_elemento = None
    mayor_valor = None

    for registro in registros:
        valor = registro["valor"]

        if mayor_valor is None or valor > mayor_valor:
            mayor_valor = valor
            mejor_elemento = registro

    return mejor_elemento


# 10) LEER CSV CON DictReader -> LISTA DE DICCIONARIOS

import csv


def leer_csv(nombre_archivo):
    registros = []

    with open(nombre_archivo, "r") as archivo:
        filas = csv.DictReader(archivo)

        for fila in filas:
            registro = {
                "nombre": fila["nombre"],
                "precio": float(fila["precio"]),
                "cantidad": int(fila["cantidad"])
            }

            registros.append(registro)

    return registros


# 11) LEER CSV Y MANEJAR FileNotFoundError

def leer_csv_con_error(nombre_archivo):
    registros = []

    try:
        with open(nombre_archivo, "r") as archivo:
            filas = csv.DictReader(archivo)

            for fila in filas:
                registros.append(dict(fila))

    except FileNotFoundError:
        print("No se encontró el archivo")

    return registros


# 12) FUNCIÓN FINAL QUE REUTILIZA OTRAS FUNCIONES

def generar_informe(nombre_archivo):
    registros = leer_csv(nombre_archivo)
    # resumen = alguna_funcion(registros)
    # print(...)


# 13) RECORRER UN DICCIONARIO DE RESULTADOS

def imprimir_totales(totales):
    for categoria in totales:
        print(categoria, totales[categoria])


# 14) CONTAR APARICIONES MANUALMENTE

def contar_apariciones(datos):
    conteos = {}

    for x in datos:
        if x not in conteos:
            conteos[x] = 0

        conteos[x] += 1

    return conteos


# 15) CONTAR APARICIONES CON Counter
from collections import Counter


def contar_con_counter(datos):
    return Counter(datos)


# 16) SET: QUEDARSE CON VALORES ÚNICOS

def valores_unicos(datos):
    return set(datos)


# 17) WHILE: REPETIR MIENTRAS SE CUMPLA UNA CONDICIÓN

def ejemplo_while():
    x = 0

    while x < 5:
        print(x)
        x += 1


# 18) RANGE
# range(5) -> 0,1,2,3,4
# range(2, 6) -> 2,3,4,5
# range(0, 10, 2) -> 0,2,4,6,8


# 19) PRINT CON FORMATO

def mostrar_precio(nombre, precio):
    print(f"{nombre}: ${precio:.2f}")


# 20) DEPURACIÓN RÁPIDA

def depurar(datos):
    total = 0

    for x in datos:
        print("Estoy mirando:", x)
        total += x
        print("Total hasta ahora:", total)

    return total
