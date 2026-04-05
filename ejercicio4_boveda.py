# ============================================================
# Ejercicio 4 — Escape Room: La Bóveda
# TP Integrador - Programación 1 - UTN
# ============================================================

# Variables iniciales (NO se piden por teclado)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Contador de veces seguidas que se eligió "Forzar" (regla anti-spam)
forzar_seguidas = 0

# Pedir nombre del agente
nombre = input("Nombre del agente: ")
while not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Nombre del agente: ")

print(f"\nBienvenido, agente {nombre}.")
print("Objetivo: abrir las 3 cerraduras antes de quedarte sin energía o tiempo.\n")

# ── Ciclo principal del juego ────────────────────────────────────────────────
juego_activo = True

while juego_activo:

    # Condición de derrota por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n¡SISTEMA BLOQUEADO! La alarma activó el cierre de seguridad.")
        print("DERROTA (bloqueo por alarma).")
        juego_activo = False
        break

    # Mostrar estado actual
    print(f"\n{'='*45}")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Código parcial: '{codigo_parcial}' | Alarma: {'¡ACTIVA!' if alarma else 'Off'}")
    print(f"{'='*45}")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")

    opcion = input("Acción: ")
    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Acción: ")
    while int(opcion) < 1 or int(opcion) > 3:
        print("Error: opción fuera de rango (1-3).")
        opcion = input("Acción: ")
    opcion = int(opcion)

    # ── OPCIÓN 1: Forzar cerradura ───────────────────────────────────────────
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        print(f"\n[Forzando cerradura...] Energía: -{20} | Tiempo: -{2}")

        # Regla anti-spam: 3ra vez seguida → alarma, no abre
        if forzar_seguidas >= 3:
            print("¡La cerradura se trabó! Alarma activada automáticamente.")
            alarma = True
            forzar_seguidas = 0  # reiniciar contador

        else:
            # Si energía < 40 hay riesgo de alarma
            if energia < 40:
                print("⚠ Energía baja — riesgo de alarma. Elegí un número del 1 al 3:")
                riesgo = input("Número (1-3): ")
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error: ingrese 1, 2 o 3.")
                    riesgo = input("Número (1-3): ")
                if int(riesgo) == 3:
                    print("¡Elegiste el 3! Alarma activada.")
                    alarma = True
                else:
                    cerraduras_abiertas += 1
                    print(f"Cerradura abierta. Total: {cerraduras_abiertas}/3")
            else:
                # Sin alarma, abre cerradura normalmente
                cerraduras_abiertas += 1
                print(f"Cerradura abierta. Total: {cerraduras_abiertas}/3")

    # ── OPCIÓN 2: Hackear panel ──────────────────────────────────────────────
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0  # corta la racha de forzar

        print("\n[Hackeando panel...]")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"  Paso {paso}/4 → código: '{codigo_parcial}'")

        print(f"Energía: -{10} | Tiempo: -{3}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"¡Código suficiente! Cerradura abierta automáticamente. Total: {cerraduras_abiertas}/3")

    # ── OPCIÓN 3: Descansar ──────────────────────────────────────────────────
    elif opcion == 3:
        forzar_seguidas = 0  # corta la racha de forzar
        tiempo -= 1
        energia_ganada = 15

        if alarma:
            energia_ganada -= 10  # penalización si alarma activa
            print("⚠ La alarma genera estrés. Recuperación reducida.")

        energia += energia_ganada
        if energia > 100:
            energia = 100

        print(f"[Descansando...] Energía: +{energia_ganada} (máx 100) | Tiempo: -{1}")

    # ── Verificar condiciones de fin ─────────────────────────────────────────
    if cerraduras_abiertas == 3:
        print("\n" + "="*45)
        print(f"¡VICTORIA! Agente {nombre} abrió las 3 cerraduras.")
        print(f"Energía restante: {energia} | Tiempo restante: {tiempo}")
        print("="*45)
        juego_activo = False

    elif energia <= 0:
        print("\n¡Sin energía! No podés continuar.")
        print("DERROTA.")
        juego_activo = False

    elif tiempo <= 0:
        print("\n¡Se acabó el tiempo!")
        print("DERROTA.")
        juego_activo = False
