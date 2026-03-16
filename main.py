from db.db import init_db
from models.cliente import Cliente
from models.cuentas import Cuenta
from models.auth import Auth


def menu():

    while True:

        print("\n==============================")
        print("      SISTEMA BANCARIO")
        print("==============================")

        print("\n--- AUTENTICACIÓN ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")

        rut = input("Introduzca su Rut: ")
        password = input("Ingrese su Contraseña: ")

        Auth.login(rut, password)

        



        print("\n--- CLIENTES (CRUD) ---")
        print("3. Registrar cliente")
        print("4. Listar clientes")
        print("5. Actualizar cliente")
        print("6. Eliminar cliente")

        print("\n--- CUENTAS ---")
        print("7. Crear cuenta")
        print("8. Consultar saldo")

        print("\n--- TRANSACCIONES ---")
        print("9. Depositar dinero")
        print("10. Retirar dinero")
        print("11. Transferencia entre cuentas")

        print("\n0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("Función en desarrollo...") 
        
        elif opcion == "2":
            print("Función en desarrollo...")

        elif opcion == "3":
            Cliente.registrar_cliente()

        elif opcion == "4":
            clientes = Cliente.listar_clientes()
            for c in clientes:
                print(c)

        elif opcion == "5":
            print("Función de actualización en desarrollo...")

        elif opcion == "6":
            print("Función de eliminación en desarrollo...")

        elif opcion == "7":
            Cuenta.crear_cuenta() 

        elif opcion == "8":
            Cuenta.consultar_saldo()

        elif opcion == "9":
            print("Depósito en desarrollo...")

        elif opcion == "10":
            print("Retiro en desarrollo...")

        elif opcion == "11":
            print("Transferencia en desarrollo...")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

init_db()
menu()

#ola