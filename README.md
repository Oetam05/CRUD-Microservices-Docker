# APLICACIÓN GESTIÓN DE DATOS PERSONALES

Esta aplicación es un sistema para la gestión de datos personales que permite a los usuarios realizar operaciones CRUD básicas, así como consultar los registros de transacciones.

## Funcionalidades

- **Crear Personas**: Permite añadir una nueva persona al sistema.
- **Modificar Datos Personales**: Actualizar la información de las personas existentes en el sistema.
- **Consultar Datos Personales**: Consultar la información de las personas basado en el documento.
- **Borrar Personas**: Eliminar personas del sistema.
- **Consultar Log**: Verificar el registro de transacciones, con búsqueda por tipo y documento, y por fecha de transacción.

## Arquitectura

La aplicación está desplegada en contenedores Docker, asegurando un aislamiento adecuado y una fácil portabilidad:

- Cada opción del menú principal es manejada por un microservicio independiente.
- La base de datos también está en un contenedor independiente.

## Tecnologías Utilizadas

- **Docker y Docker Compose**: Se utilizan para la contenerización y la orquestación de los servicios. Esto garantiza la coherencia entre los entornos de desarrollo, prueba y producción, facilitando la implementación y la escalabilidad.
- **Django REST Framework**: Cada microservicio es un proyecto independiente creado con Django REST Framework, que es un potente y flexible toolkit para construir APIs web. Esto facilita la creación de APIs RESTful bien diseñadas y permite una rápida iteración de desarrollo.
- **PostgreSQL**: Seleccionada como sistema de gestión de base de datos, conocida por su robustez y su soporte para características avanzadas. Es utilizada para la persistencia de datos, asegurando la integridad y la fiabilidad de los registros.
- **Kong**: Utilizado como API Gateway, que actúa como intermediario para las solicitudes de los clientes, proporcionando una capa adicional de abstracción y control para asegurar, gestionar y extender las APIs.

## Requisitos

- Docker

## Instalación y Ejecución

Para ejecutar la aplicación, sigue estos pasos:

1. Clonar el repositorio:
```bash
git clone https://github.com/Oetam05/CRUD-Microservices-Docker.git
```
2. Navegar al directorio del proyecto:
```bash
cd [Nombre del directorio del proyecto]
```
3. Ejecutar Docker Compose para construir e iniciar los contenedores:
```bash
docker-compose up
```
## Uso

Una vez que la aplicación esté en ejecución, puedes interactuar con ella mediante peticiones HTTP a la dirección `localhost:8000` la API Gateway está configurada para redirigir las peticiones adecuadamente a cada microservicio dependiendo del tipo de peticion:

### Funciones CRUD

- **Crear Persona (POST)**: `/app/`
- **Modificar Datos Personales (PUT)**: `/app/[tipo_doc]/[num_doc]/`
- **Consultar todas las Personas (GET)**: `/app/`
- **Consultar Persona Específica (GET)**: `/app/[tipo_doc]/[num_doc]/`
- **Eliminar Persona (DELETE)**: `/app/[tipo_doc]/[num_doc]/`

Donde `[tipo_doc]` es el tipo de documento y `[num_doc]` es el número del documento de la persona.

### Consultas de Logs
- **Consultar Logs por Documento (GET)**: `/log/[tipo_doc]/[num_doc]/`
- **Consultar Logs por Fecha (GET)**: `/log/[fecha]/`

La fecha debe estar en el formato `AAAA-MM-DD`.
### Ejemplos de Uso
Para obtener la informacion de todas las personas o de una persona especifica: 
```bash 
http://localhost:8000/app/
http://localhost:8000/app/CC/12345/
```
Para obtener los logs de una persona:
```bash 
http://localhost:8000/log/CC/12345/
```
Para obtener los logs de todas las personas en cierta fecha:
```bash 
http://localhost:8000/log/2024-03-17/
```

