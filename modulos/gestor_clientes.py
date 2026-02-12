from modulos.excepciones import ClienteExistenteError, ClienteNoEncontradoError

class GestorClientes:

    # Clase encargada de gestionar los clientes

    def __init__(self):
        self._clientes = []

    # Aplicación del CRUD

    def agregar_cliente(self, cliente):
        if self.buscar_cliente(cliente.get_rut()):
            raise ClienteExistenteError("Ya existe un cliente con ese RUT.")

        self._clientes.append(cliente)

    def listar_clientes(self):
        if not self._clientes:
            print("No hay clientes registrados.")
            return

        for cliente in self._clientes:
            print(cliente)

    def buscar_cliente(self, rut):
        for cliente in self._clientes:
            if cliente.get_rut() == rut:
                return cliente
        return None

    def eliminar_cliente(self, rut):
        cliente = self.buscar_cliente(rut)

        if not cliente:
            raise ClienteNoEncontradoError("❌ Cliente no encontrado.")

        self._clientes.remove(cliente)
        # print("🗑 Cliente eliminado correctamente.")

    def actualizar_cliente(self, rut, nombre, email, telefono, direccion):
        cliente = self.buscar_cliente(rut)

        if not cliente:
            raise ClienteNoEncontradoError("❌ Cliente no encontrado.")

        cliente.set_nombre(nombre)
        cliente.set_email(email)
        cliente.set_telefono(telefono)
        cliente.set_direccion(direccion)
        print("🔄 Cliente actualizado correctamente.")

