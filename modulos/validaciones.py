import re
from modulos.excepciones import EmailInvalidoError, TelefonoInvalidoError

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron, email):
        raise EmailInvalidoError("El email ingresado no es válido.")


def validar_telefono(telefono):
    patron = r'^\+?\d{8,15}$'
    if not re.match(patron, telefono):
        raise TelefonoInvalidoError("El teléfono debe contener solo números (8-15 dígitos).")
