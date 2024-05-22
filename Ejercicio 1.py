tipo_uva = input("Ingrese el tipo de uva (A o B): ")
tamaño_uva = int(input("Ingrese el tamaño de la uva (1 o 2): "))
kilos_producidos = float(input("Ingrese la cantidad de kilos producidos: "))
precio_kilo = float(input("Ingrese el precio por kilo: "))

def calcular_ganancia(tipo, tamaño, kilos, precio_por_kilo):
   
    if tipo == 'A':
        recargo = 0.20 if tamaño == 1 else 0.30
    elif tipo == 'B':
        recargo = -0.30 if tamaño == 1 else -0.50
    else:
        print("Tipo de uva no válido. Debe ser 'A' o 'B'.")
        return None
    print(f"EL precio es de ${precio_por_kilo:.2f}")
    
    precio_final = precio_por_kilo + recargo
    print(f"Recarga ${recargo:.2f}")
    print(f"Precio final ${precio_final:.2f}")
   
    ganancia_total = kilos * precio_final
    
    return ganancia_total


ganancia = calcular_ganancia(tipo_uva, tamaño_uva, kilos_producidos, precio_kilo)

if ganancia is not None:
    print(f"La ganancia total es de ${ganancia:.2f}")
