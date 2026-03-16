def mostrar_gasto_total(gastos):
    total_acumulado = 0
    
    if not gastos:
        print("\n[!] No hay datos registrados para realizar el cálculo.")
        return

    # recorre la lista de diccionarios
    for registro in gastos:
        total_acumulado += registro["Valor"]
    
    print("\n========================================")
    print(f" GASTO TOTAL ACUMULADO: ${total_acumulado}")
    print("========================================\n")