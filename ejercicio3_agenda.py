# ============================================================
# Ejercicio 3 — Agenda de Turnos con Nombres (sin listas)
# TP Integrador - Programación 1 - UTN
# SIN listas, sin diccionarios, sin tuplas, sin sets
# ============================================================

# 1. Pedir nombre del operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Nombre del operador: ")

print(f"\nBienvenido, {operador}!")

# Turnos del Lunes (4 cupos) — variables individuales
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Turnos del Martes (3 cupos) — variables individuales
martes1 = ""
martes2 = ""
martes3 = ""

# ── Helpers para leer/escribir los turnos sin listas ────────────────────────

def turno_lunes(n):
    if n == 1: return lunes1
    if n == 2: return lunes2
    if n == 3: return lunes3
    if n == 4: return lunes4
    return ""

def turno_martes(n):
    if n == 1: return martes1
    if n == 2: return martes2
    if n == 3: return martes3
    return ""

# ── Menú principal ──────────────────────────────────────────────────────────
continuar = True

while continuar:
    print("\n1) Reservar  2) Cancelar  3) Ver agenda del día  4) Resumen  5) Cerrar")
    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")
    while int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    # ── 1. RESERVAR ─────────────────────────────────────────────────────────
    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente: ")

        if dia == 1:
            # Verificar duplicado
            if (paciente.lower() == lunes1.lower() or
                paciente.lower() == lunes2.lower() or
                paciente.lower() == lunes3.lower() or
                paciente.lower() == lunes4.lower()):
                print(f"Error: {paciente} ya tiene turno el Lunes.")
            else:
                # Guardar en primer espacio libre
                if lunes1 == "":
                    lunes1 = paciente
                    print(f"Turno reservado: {paciente} - Lunes turno 1")
                elif lunes2 == "":
                    lunes2 = paciente
                    print(f"Turno reservado: {paciente} - Lunes turno 2")
                elif lunes3 == "":
                    lunes3 = paciente
                    print(f"Turno reservado: {paciente} - Lunes turno 3")
                elif lunes4 == "":
                    lunes4 = paciente
                    print(f"Turno reservado: {paciente} - Lunes turno 4")
                else:
                    print("No hay turnos disponibles el Lunes.")

        else:  # dia == 2, Martes
            if (paciente.lower() == martes1.lower() or
                paciente.lower() == martes2.lower() or
                paciente.lower() == martes3.lower()):
                print(f"Error: {paciente} ya tiene turno el Martes.")
            else:
                if martes1 == "":
                    martes1 = paciente
                    print(f"Turno reservado: {paciente} - Martes turno 1")
                elif martes2 == "":
                    martes2 = paciente
                    print(f"Turno reservado: {paciente} - Martes turno 2")
                elif martes3 == "":
                    martes3 = paciente
                    print(f"Turno reservado: {paciente} - Martes turno 3")
                else:
                    print("No hay turnos disponibles el Martes.")

    # ── 2. CANCELAR ─────────────────────────────────────────────────────────
    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        cancelado = False

        if dia == 1:
            if lunes1.lower() == paciente.lower():
                lunes1 = ""
                cancelado = True
            elif lunes2.lower() == paciente.lower():
                lunes2 = ""
                cancelado = True
            elif lunes3.lower() == paciente.lower():
                lunes3 = ""
                cancelado = True
            elif lunes4.lower() == paciente.lower():
                lunes4 = ""
                cancelado = True
        else:
            if martes1.lower() == paciente.lower():
                martes1 = ""
                cancelado = True
            elif martes2.lower() == paciente.lower():
                martes2 = ""
                cancelado = True
            elif martes3.lower() == paciente.lower():
                martes3 = ""
                cancelado = True

        if cancelado:
            print(f"Turno de {paciente} cancelado.")
        else:
            print(f"No se encontró a {paciente} en ese día.")

    # ── 3. VER AGENDA DEL DÍA ───────────────────────────────────────────────
    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        if dia == 1:
            print("\n--- Agenda del Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\n--- Agenda del Martes ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # ── 4. RESUMEN GENERAL ──────────────────────────────────────────────────
    elif opcion == 4:
        # Contar ocupados Lunes
        ocup_lunes = 0
        if lunes1 != "": ocup_lunes += 1
        if lunes2 != "": ocup_lunes += 1
        if lunes3 != "": ocup_lunes += 1
        if lunes4 != "": ocup_lunes += 1

        # Contar ocupados Martes
        ocup_martes = 0
        if martes1 != "": ocup_martes += 1
        if martes2 != "": ocup_martes += 1
        if martes3 != "": ocup_martes += 1

        print("\n--- Resumen General ---")
        print(f"Lunes:  {ocup_lunes} ocupados / {4 - ocup_lunes} disponibles")
        print(f"Martes: {ocup_martes} ocupados / {3 - ocup_martes} disponibles")

        if ocup_lunes > ocup_martes:
            print("Día con más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate: ambos días tienen la misma cantidad de turnos.")

    # ── 5. CERRAR ───────────────────────────────────────────────────────────
    elif opcion == 5:
        print("Sistema cerrado. ¡Hasta pronto!")
        continuar = False
