def mostrar_total(gastos):
    print("\n--- TOTAL DE GASTOS ---")
    if not gastos:
        print("No hay gastos registrados.")
    else:
        total = sum(g["valor"] for g in gastos)
        print(f"El gasto total acumulado es: ${total}")