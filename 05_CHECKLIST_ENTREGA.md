# 05 — Checklist antes de entregar

Usá esta lista al terminar cada ejercicio.

## Función
- [ ] ¿El nombre de la función coincide exactamente con la consigna?
- [ ] ¿Recibe los parámetros pedidos?
- [ ] Si dice **devuelva**, ¿hay `return`?
- [ ] Si dice **imprima**, ¿hay `print()`?
- [ ] ¿El `return` está ubicado donde corresponde?

## Recorridos
- [ ] ¿El `for` recorre la colección correcta?
- [ ] ¿La variable del `for` representa lo que creo que representa?
- [ ] ¿Necesito recorrer todo antes de devolver?

## Contadores / acumuladores
- [ ] Si cuento, ¿inicialicé `contador = 0`?
- [ ] Si sumo, ¿inicialicé `total = 0`?
- [ ] Si guardo, ¿inicialicé `resultado = []`?
- [ ] Si agrupo, ¿inicialicé `resultado = {}`?

## Diccionarios
- [ ] ¿Las claves están bien escritas?
- [ ] ¿Estoy usando `diccionario[clave]` correctamente?
- [ ] Si acumulo por categoría, ¿creo la clave en 0 solo si no existe?
- [ ] ¿La suma queda fuera del `if` de inicialización?

## CSV
- [ ] ¿Hice `import csv`?
- [ ] ¿Abrí el archivo con `open()`?
- [ ] ¿Uso `csv.DictReader()` o `csv.reader()` según convenga?
- [ ] ¿Los encabezados coinciden con las claves usadas?
- [ ] ¿Convertí strings numéricos con `int()` / `float()`?
- [ ] Si la consigna lo pide, ¿manejo `FileNotFoundError`?

## Errores frecuentes
- [ ] ¿Confundí `=` con `==`?
- [ ] ¿Usé `+` cuando necesitaba `+=`?
- [ ] ¿El código tiene problemas de indentación?
- [ ] ¿La función devuelve `None` porque olvidé `return`?
- [ ] ¿Estoy cortando el recorrido demasiado pronto?

## Prueba rápida
Antes de entregar, probá con datos chicos.

Ejemplo:
```python
print(funcion([1, 2, 3]))
```

Si no entendés qué está pasando, agregá temporalmente:
```python
print("elemento:", elemento)
print("resultado:", resultado)
```

## Si la consigna usa funciones anteriores
- [ ] ¿Estoy llamando a la función anterior en vez de repetir todo el código?
- [ ] ¿Guardo lo que devuelve?
- [ ] ¿Le paso ese resultado a la siguiente función?

## Última mirada
- [ ] ¿Corre el archivo completo sin error?
- [ ] ¿El resultado tiene el tipo pedido (lista, diccionario, número, texto)?
- [ ] ¿La salida se parece al ejemplo de la consigna?
- [ ] ¿Dejé comentarios o nombres de variables razonables?
