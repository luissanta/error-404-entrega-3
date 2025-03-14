# Microservicio de inicio de sesión

Microservicio que contiene la lógica y arquitectura para el inicio de sesión de un usuario en el sistam SaludTech de los Alpes.

## Justificaciones de diseño

1. Event Stream Versioning: Se usa para el manejo del versionamiento de los esquemas y comandos para tener diferentes versiones de autenticación para los diferentes tipos de llamados que se pueden realizar dada una versión de request especifica para el artefacto que quiera consumir el servicio.
2. Avro: Para mejorar el rendimiento y la latencia en el envio de mensajes al broker de eventos.

## Estructura del proyecto

- **src/sta/api**: La carpeta contiene los endpoints para el inicio de sesión el cual ejecuta el evento `CreatedSession` y el comando `CreateSessionCommand`.
- **src/sta/authentication/aplicacion**: En el módulo se maneja todo lo relacionado con la construcción de los comandos necesarios para el inicio de sesión.
- **src/sta/authentication/infrastructure**: En esta estructura de carpeta se maneja el directorio de versionamiento haciendo uso de Event Stream Versioning de los esquemas y comandos que se usen en la autenticación del usuario.

## SaludTech de los Alpes
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/sta/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
python[3] -m flask --app src/sta/api run --port 8000
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build -t ms-1 .
```

### Pruebas del microservicio

Endpoint: `/authentication/login`
Método: GET
Cuerpo de la solicitud:
```json
{
    "username" : "user_1"
    , "password" : "12345"
}
```
