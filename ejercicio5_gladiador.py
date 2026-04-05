# ============================================================
# Ejercicio 5 — Escape Room: La Arena del Gladiador
# TP Integrador - Programación 1 - UTN
# ============================================================

print("--- BIENVENIDO A LA ARENA ---")

# ── Paso 1: Nombre del Gladiador ─────────────────────────────────────────────
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# ── Paso 2: Variables iniciales (sin preguntar al usuario) ───────────────────
vida_jugador = 100          # int
vida_enemigo = 100          # int
pociones = 3                # int
danio_pesado = 15           # int
danio_enemigo = 12          # int
turno_gladiador = True      # boolean — True = turno del jugador

print(f"\n=== INICIO DEL COMBATE ===")

# ── Paso 3: Ciclo de combate ─────────────────────────────────────────────────
while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # Validar opción del menú
    opcion = input("Opción: ")
    while not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")
    while int(opcion) < 1 or int(opcion) > 3:
        print("Error: Opción debe ser 1, 2 o 3.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    # ── Acción A: Ataque Pesado ───────────────────────────────────────────────
    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = float(danio_pesado) * 1.5   # Golpe crítico (float)
            print(f"¡GOLPE CRÍTICO! x1.5 de daño.")
        else:
            danio_final = float(danio_pesado)

        vida_enemigo -= int(danio_final)
        if vida_enemigo < 0:
            vida_enemigo = 0
        print(f"¡Atacaste al enemigo por {danio_final:.0f} puntos de daño!")

    # ── Acción B: Ráfaga Veloz ───────────────────────────────────────────────
    elif opcion == 2:
        print(f">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            if vida_enemigo < 0:
                vida_enemigo = 0
            print(f"> Golpe conectado por 5 de daño")

    # ── Acción C: Curar ──────────────────────────────────────────────────────
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print(f"Usaste una poción. HP: {vida_jugador} | Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")

    # ── Turno del Enemigo (siempre ataca después del jugador) ─────────────────
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        if vida_jugador < 0:
            vida_jugador = 0
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

    # Mostrar separador si el combate sigue
    if vida_jugador > 0 and vida_enemigo > 0:
        print(f"=== NUEVO TURNO ===")

# ── Paso 4: Resultado final ──────────────────────────────────────────────────
print("\n" + "="*40)
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("="*40)
