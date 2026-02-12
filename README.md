# 📌 Gestor Inteligente de Clientes (GIC)

Sistema de gestión de clientes desarrollado en **Python 3**, aplicando **Programación Orientada a Objetos (POO)**, validaciones avanzadas, manejo de excepciones personalizadas, exportación/importación de archivos y generación de reportes.

Proyecto desarrollado para la **Evaluación del Módulo 4**.

---

## 🚀 Objetivo del Proyecto

Desarrollar una plataforma por consola que permita:

- Registrar clientes
- Consultar clientes
- Actualizar información
- Eliminar clientes
- Diferenciar tipos de clientes mediante herencia
- Aplicar validaciones y manejo de errores
- Exportar e importar datos en formato CSV
- Generar reportes en TXT
- Registrar acciones en logs

---

## 🧠 Conceptos Aplicados

- Programación Orientada a Objetos
- Encapsulación
- Herencia
- Polimorfismo
- Excepciones personalizadas
- Validaciones con expresiones regulares (Regex)
- Manejo de archivos (CSV y TXT)
- Logging profesional
- Modularización del código

---

## 🏗 Arquitectura del Proyecto

Proyecto Modulo 4/
│
├── main.py
│
├── modulos/
│ ├── cliente.py
│ ├── cliente_regular.py
│ ├── cliente_premium.py
│ ├── cliente_corporativo.py
│ ├── gestor_clientes.py
│ ├── validaciones.py
│ ├── excepciones.py
│ ├── archivos.py
│
├── datos/
│ ├── clientes.csv
│ ├── clientes_entrada.csv
│
├── reportes/
│ └── resumen.txt
│
├── logs/
│ └── app.log
│
└── README.md


---

## 👥 Tipos de Clientes

El sistema implementa herencia a partir de la clase base `Cliente`:

- ClienteRegular
- ClientePremium
- ClienteCorporativo

Cada subclase redefine el método `mostrar_info()` aplicando **polimorfismo**.

---

## 🔍 Funcionalidades Principales

### CRUD Completo

- Agregar cliente
- Listar clientes
- Buscar cliente
- Actualizar cliente
- Eliminar cliente

### Validaciones

- Email válido (regex)
- Teléfono válido
- Control de clientes duplicados

### Manejo de Excepciones

- EmailInvalidoError
- TelefonoInvalidoError
- ClienteExistenteError
- ClienteNoEncontradoError

### Manejo de Archivos

- Exportación a `datos/clientes.csv`
- Importación desde `clientes_entrada.csv`
- Generación de reporte en `reportes/resumen.txt`
- Registro de actividad en `logs/app.log`
