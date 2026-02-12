class Cliente:

    # Encapsulamiento mediante atributos privados.

    def __init__(self, rut, nombre, email, telefono, direccion):
        self._rut = rut
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._direccion = direccion

    # Metodos Getters

    def get_rut(self):
        return self._rut

    def get_nombre(self):
        return self._nombre

    def get_email(self):
        return self._email

    def get_telefono(self):
        return self._telefono

    def get_direccion(self):
        return self._direccion


    # Metodos Setters

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_email(self, email):
        self._email = email

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_direccion(self, direccion):
        self._direccion = direccion


    # Métodos

    def mostrar_info(self):
        # Muestra información básica del cliente
        return f"ID: {self._rut} | Nombre: {self._nombre} | Email: {self._email}"

    def __str__(self):
        return self.mostrar_info()


