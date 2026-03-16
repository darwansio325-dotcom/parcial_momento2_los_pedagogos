def buscar_por_placa(gastos):
    print("\n--- BUSCAR GASTO POR PLACA ---")
    placa_buscada = input("Ingrese la placa a buscar: ")
    encontrado = False
    
    for gasto in gastos:
        if gasto["placa"].upper() == placa_buscada.upper():
            print(f"Placa: {gasto['placa']} | Concepto: {gasto['concepto']} | Valor: ${gasto['valor']}")
            encontrado = True
    
    if not encontrado:
        print(f"No se encontraron gastos para la placa: {placa_buscada}")