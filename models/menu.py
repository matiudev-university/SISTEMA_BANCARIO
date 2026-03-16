from models.cliente import Cliente
from models.cuentas import Cuenta
class Menu:

    @staticmethod
    def menu_empleado():
        while True:
            print("\n--- MENU EMPLEADO ---")
            print("1. Registrar Cliente")
            print("2. Crear Cuenta")
            print("3. Consultar Saldo")
            print("4. Depositar")
            print("5. Retirar")
            print("6. Transferencia")
            print("7. Listar Clientes")
            print("0. Cerrar Sesión")

            opcion = input("\nSeleccione una opción: ")

            match opcion:
                case "1":
                    Cliente.registrar_cliente()
                case "2":
                    Cuenta.crear_cuenta()
                case "3":
                    Cuenta.consultar_saldo()
                case "4":
                    print("Función en desarrollo...")
                case "5":
                    print("Función en desarrollo...")
                case "6":
                    print("Función en desarrollo...")
                case "7":
                    clientes = Cliente.listar_clientes()
                    for cliente in clientes:
                        print(cliente)
                case "0":
                    return
                case _:
                    print("❌ Opcion Invalida")

    @staticmethod
    def menu_cliente():
        while True:
            print("\n--- MENU CLIENTE ---")
            print("1. Consultar Saldo")
            print("2. Ver Historial de movimientos")
            print("3. Transferir a otras cuentas")
            print("0. Cerrar Sesión")

            opcion = input("\nSeleccione una opción: ")

            match opcion:
                case "1":
                    print("Función en desarrollo...")
                case "2":
                    print("Función en desarrollo...")
                case "3":
                    print("Función en desarrollo...")
                case "0":
                    return
                case _:
                    print("❌ Opcion Invalida")

