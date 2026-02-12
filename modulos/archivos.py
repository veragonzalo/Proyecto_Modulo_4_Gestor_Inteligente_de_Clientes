import csv
import os
import logging

from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo

# CONFIGURACIÓN DE LOGS

def configurar_logs():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

# EXPORTAR CSV

def exportar_clientes_csv(gestor, ruta="datos/clientes.csv"):
    os.makedirs("datos", exist_ok=True)

    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)

        writer.writerow(["tipo", "RUT", "nombre", "email", "telefono", "direccion", "empresa", "contacto"])

        for cliente in gestor._clientes:

            if isinstance(cliente, ClienteRegular):
                tipo = "regular"
                empresa = ""
                contacto = ""

            elif isinstance(cliente, ClientePremium):
                tipo = "premium"
                empresa = ""
                contacto = ""

            elif isinstance(cliente, ClienteCorporativo):
                tipo = "corporativo"
                empresa = cliente.get_empresa()
                contacto = cliente.get_contacto_empresa()

            writer.writerow([
                tipo,
                cliente.get_rut(),
                cliente.get_nombre(),
                cliente.get_email(),
                cliente.get_telefono(),
                cliente.get_direccion(),
                empresa,
                contacto
            ])

    logging.info("Clientes exportados correctamente a CSV.")


def importar_clientes_csv(gestor, ruta="datos/clientes_entrada.csv"):

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                tipo = fila["tipo"]

                if tipo == "regular":
                    cliente = ClienteRegular(
                        fila["Rut"],
                        fila["nombre"],
                        fila["email"],
                        fila["telefono"],
                        fila["direccion"]
                    )

                elif tipo == "premium":
                    cliente = ClientePremium(
                        fila["Rut"],
                        fila["nombre"],
                        fila["email"],
                        fila["telefono"],
                        fila["direccion"]
                    )

                elif tipo == "corporativo":
                    cliente = ClienteCorporativo(
                        fila["Rut"],
                        fila["nombre"],
                        fila["email"],
                        fila["telefono"],
                        fila["direccion"],
                        fila["empresa"],
                        fila["contacto"]
                    )

                else:
                    continue

                gestor._clientes.append(cliente)

        logging.info("Clientes importados correctamente desde CSV.")

    except FileNotFoundError:
        logging.error("Archivo de importación no encontrado.")
        print("❌ Archivo no encontrado.")


def generar_reporte(gestor, ruta="reportes/resumen.txt"):

    os.makedirs("reportes", exist_ok=True)

    total = len(gestor._clientes)
    regulares = 0
    premium = 0
    corporativos = 0

    for cliente in gestor._clientes:
        if isinstance(cliente, ClienteRegular):
            regulares += 1
        elif isinstance(cliente, ClientePremium):
            premium += 1
        elif isinstance(cliente, ClienteCorporativo):
            corporativos += 1

    with open(ruta, mode="w", encoding="utf-8") as archivo:
        archivo.write("===== REPORTE DE CLIENTES =====\n")
        archivo.write(f"Total clientes: {total}\n")
        archivo.write(f"Clientes regulares: {regulares}\n")
        archivo.write(f"Clientes premium: {premium}\n")
        archivo.write(f"Clientes corporativos: {corporativos}\n")

    logging.info("Reporte generado correctamente.")

