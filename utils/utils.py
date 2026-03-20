import re
# ======================================

def validar_rut(titulo = "Ingrese rut: "):
    """
    Normaliza y valida un RUT chileno.
    Retorna el RUT en formato 12345678-K
    """

    while True:
        rut = input(titulo)

        if not rut:
            print("❌ El RUT no puede estar vacío")
            continue

        # limpiar
        rut = rut.strip().replace(".", "").replace(" ", "").upper()

        # agregar guion si no existe
        if "-" not in rut and len(rut) > 1:
            rut = rut[:-1] + "-" + rut[-1]

        # validar formato (números + guion + dígito o K)
        if not re.match(r"^\d{7,8}-[\dK]$", rut):
            print("❌ Formato de RUT inválido. Ej: 12345678-K")
            continue

        return rut
# ======================================

def generar_numero_cuenta():
    pass