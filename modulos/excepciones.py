class EmailInvalidoError(Exception):
    """Se lanza cuando el email no cumple el formato válido."""
    pass


class TelefonoInvalidoError(Exception):
    """Se lanza cuando el teléfono no cumple el formato válido."""
    pass


class ClienteExistenteError(Exception):
    """Se lanza cuando se intenta registrar un cliente con ID duplicado."""
    pass


class ClienteNoEncontradoError(Exception):
    """Se lanza cuando no se encuentra un cliente."""
    pass
