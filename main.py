from db.db import init_db
from models.auth import Auth
from models.menu import Menu


def menu():

    while True:

        print("\n==============================")
        print("      SISTEMA BANCARIO")
        print("==============================")

        print("\n--- AUTENTICACIÓN ---")
        # print("1. Iniciar sesión")
        # print("2. Registrar usuario")

        rut = input("Introduzca su Rut: ")
        password = input("Ingrese su Contraseña: ")

        usuario = Auth.login(rut, password)

        if not usuario:
            print("❌ RUT o contraseña incorrectos")
            continue

        rol = usuario["rol"]

        if rol == "cliente":
            Menu.menu_cliente()
        elif rol == "empleado":
            Menu.menu_empleado()
        
        # elif rol == "gerente":
        #     Menu.menu_gerente()

init_db()
menu()

#ola