from modulos.cliente import Cliente

class ClienteRegular(Cliente):

    def __init__(self, rut, nombre, email, telefono, direccion):
        super().__init__(rut, nombre, email, telefono, direccion)

    def beneficio_exclusivo(self):
        return "Acceso a promociones estándar."

    def mostrar_info(self):
        return f"[Cliente REGULAR] {super().mostrar_info()}"
