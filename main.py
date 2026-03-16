import calculos
import módulobusqueda

gastos = []
# --- Funcion de Sofia Rodriguez ---
def registrar_gasto():
    print("\n--- REGISTRAR NUEVO GASTO ---")
    placa = input("Ingrese la placa: ")
    concepto = input("Concepto (Gasolina/Peaje): ")
    valor = float(input("Ingrese el valor: "))
    
    
    gasto = {"placa": placa, "concepto": concepto, "valor": valor}
    gastos.append(gasto)
    print("Gasto registrado con exito.")
def menu():
    print("\n--- MENU DE OPCIONES ---")
    print("1. Registrar gasto")
    print("2. Mostrar total")
    print("3. Buscar por placa")
    print("4. Salir")

def main():
    while True:
        menu()
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            registrar_gasto()
            
            
        elif opcion == "2":
            calculos.mostrar_total(gastos) 

        elif opcion == "3":
            módulobusqueda.buscar_por_placa(gastos) 
            
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion incorrecta")

if __name__ == "__main__":
    main()