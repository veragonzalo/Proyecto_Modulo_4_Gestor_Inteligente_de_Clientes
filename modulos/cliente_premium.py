from modulos.cliente import Cliente

class ClientePremium(Cliente):

    # Cliente premium que tiene beneficios adicionales

    def __init__(self, rut, nombre, email, telefono, direccion):
        super().__init__(rut, nombre, email, telefono, direccion)

    def descuento_especial(self):
        return "Descuento del 20% en todos los servicios."

    def mostrar_info(self):
        return f"[Cliente PREMIUM ⭐] {super().mostrar_info()}"
