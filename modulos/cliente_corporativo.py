from modulos.cliente import Cliente

class ClienteCorporativo(Cliente):

    # Representa a un cliente corporativo (empresa)

    def __init__(self, rut, nombre, email, telefono, direccion, empresa, contacto_empresa):
        super().__init__(rut, nombre, email, telefono, direccion)
        self._empresa = empresa
        self._contacto_empresa = contacto_empresa

    def get_empresa(self):
        return self._empresa

    def get_contacto_empresa(self):
        return self._contacto_empresa

    def mostrar_info(self):
        return f"[Cliente CORPORATIVO 🏢] {super().mostrar_info()} | Empresa: {self._empresa}"
