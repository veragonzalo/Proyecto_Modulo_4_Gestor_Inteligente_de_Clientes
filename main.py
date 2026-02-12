from modulos.gestor_clientes import GestorClientes
from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo
from modulos.validaciones import validar_email, validar_telefono
from modulos.excepciones import (
    EmailInvalidoError,
    TelefonoInvalidoError,
    ClienteExistenteError,
    ClienteNoEncontradoError
)
from modulos.archivos import (
    configurar_logs,
    exportar_clientes_csv,
    importar_clientes_csv,
    generar_reporte
)

configurar_logs()

def mostrar_menu():
    print("\n===== GESTOR INTELIGENTE DE CLIENTES =====")
    print("1. Agregar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente")
    print("4. Eliminar cliente")
    print("5. Actualizar cliente")
    print("6. Exportar clientes a CSV")
    print("7. Importar clientes desde CSV")
    print("8. Generar reporte")
    print("9. Salir")


def main():
    gestor = GestorClientes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            try:
                print("Seleccione tipo de cliente:")
                print("1. Regular")
                print("2. Premium")
                print("3. Corporativo")

                tipo = input("Tipo: ")

                rut = input("RUT: ")
                nombre = input("Nombre: ")
                email = input("Email: ")
                telefono = input("Teléfono: ")
                direccion = input("Dirección: ")

                # VALIDACIONES
                validar_email(email)
                validar_telefono(telefono)

                if tipo == "1":
                    cliente = ClienteRegular(rut, nombre, email, telefono, direccion)

                elif tipo == "2":
                    cliente = ClientePremium(rut, nombre, email, telefono, direccion)

                elif tipo == "3":
                    empresa = input("Empresa: ")
                    contacto_empresa = input("Contacto empresa: ")
                    cliente = ClienteCorporativo(
                        rut, nombre, email, telefono, direccion, empresa, contacto_empresa
                    )
                else:
                    print("Tipo inválido.")
                    continue

                gestor.agregar_cliente(cliente)
                print("✅ Cliente agregado correctamente.")

            except EmailInvalidoError as e:
                print(f"❌ Error: {e}")

            except TelefonoInvalidoError as e:
                print(f"❌ Error: {e}")

            except ClienteExistenteError as e:
                print(f"⚠️ Error: {e}")

            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == "2":
            gestor.listar_clientes()

        elif opcion == "3":
            rut = input("Ingrese RUT a buscar: ")
            cliente = gestor.buscar_cliente(rut)
            if cliente:
                print(cliente)
            else:
                print("❌ Cliente no encontrado.")


        elif opcion == "4":

            try:

                rut = input("Ingrese RUT a eliminar: ")

                gestor.eliminar_cliente(rut)

                print("🗑 Cliente eliminado correctamente.")


            except ClienteNoEncontradoError as e:

                print(f"❌ Error: {e}")


        elif opcion == "5":
            rut = input("Ingrese RUT a actualizar: ")
            nombre = input("Nuevo nombre: ")
            email = input("Nuevo email: ")
            telefono = input("Nuevo teléfono: ")
            direccion = input("Nueva dirección: ")

            gestor.actualizar_cliente(rut, nombre, email, telefono, direccion)

        elif opcion == "6":
            exportar_clientes_csv(gestor)
            print("📁 Clientes exportados correctamente.")

        elif opcion == "7":
            importar_clientes_csv(gestor)
            print("📥 Clientes importados correctamente.")

        elif opcion == "8":
            generar_reporte(gestor)
            print("📊 Reporte generado correctamente.")

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    main()
