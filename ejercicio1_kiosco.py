# ============================================================
# Ejercicio 1 — Caja del Kiosco
# TP Integrador - Programación 1 - UTN
# ============================================================

# 1. Pedir nombre del cliente (solo letras, no vacío)
nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: solo se permiten letras y no puede estar vacío.")
    nombre = input("Cliente: ")

# 2. Pedir cantidad de productos (entero positivo)
cantidad_str = input("Cantidad de productos: ")
while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: ingrese un número entero mayor a 0.")
    cantidad_str = input("Cantidad de productos: ")

cantidad = int(cantidad_str)

# 3. Variables acumuladoras
total_sin_descuento = 0
total_con_descuento = 0.0

# 4. Bucle por cada producto
for i in range(1, cantidad + 1):
    # Pedir precio (entero, validar con isdigit)
    precio_str = input(f"Producto {i} - Precio: ")
    while not precio_str.isdigit():
        print("Error: ingrese un número entero positivo.")
        precio_str = input(f"Producto {i} - Precio: ")
    precio = int(precio_str)

    # Pedir si tiene descuento S/N
    descuento_resp = input("Descuento (S/N): ")
    while descuento_resp.lower() != "s" and descuento_resp.lower() != "n":
        print("Error: ingrese S o N.")
        descuento_resp = input("Descuento (S/N): ")

    # Acumular totales
    total_sin_descuento += precio

    if descuento_resp.lower() == "s":
        precio_con_descuento = precio * 0.90  # 10% de descuento
    else:
        precio_con_descuento = precio

    total_con_descuento += precio_con_descuento

# 5. Calcular ahorro y promedio
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

# 6. Mostrar resultados
print(f"\nTotal sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
