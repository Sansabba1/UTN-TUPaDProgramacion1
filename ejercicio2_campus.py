# ============================================================
# Ejercicio 2 — Acceso al Campus y Menú Seguro
# TP Integrador - Programación 1 - UTN
# ============================================================

USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

# 1. Login con máximo 3 intentos
intentos = 0
acceso = False

while intentos < 3 and not acceso:
    intentos += 1
    print(f"\nIntento {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
        acceso = True
    else:
        print("Error: credenciales inválidas.")

# 2. Si falló 3 veces, bloquear
if not acceso:
    print("Cuenta bloqueada.")
else:
    print("Acceso concedido.")

    clave_actual = CLAVE_CORRECTA  # para poder cambiarla en la sesión

    # 3. Menú repetitivo
    continuar = True
    while continuar:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        # Validar que sea número
        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        # Validar que esté entre 1 y 4
        while int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion == 1:
            print("Estado: Inscripto")

        elif opcion == 2:
            # Cambio de clave: mínimo 6 caracteres, debe coincidir
            nueva = input("Nueva clave: ")
            while len(nueva) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva = input("Nueva clave: ")

            confirmacion = input("Confirmar clave: ")
            while confirmacion != nueva:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirmar clave: ")

            clave_actual = nueva
            print("Clave actualizada correctamente.")

        elif opcion == 3:
            print("¡El aprendizaje es un proceso, no un destino. Seguí adelante!")

        elif opcion == 4:
            print("Cerrando sesión. ¡Hasta pronto!")
            continuar = False
