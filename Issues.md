## 🟢 Estructura de rutas, controladores y servicios

**Peso:** 3

### 📋 Descripción Detallada

- Crear las carpetas `routes/`, `controllers/` y `services/` dentro de `src/` para organizar el código.
- Definir la estructura base para los endpoints REST, separando la lógica de rutas, controladores y servicios.
- Implementar un ejemplo de endpoint modularizado (por ejemplo, `/api/hello`).
- Documentar la estructura de carpetas y la responsabilidad de cada una en el README.

### 🎯 Objetivo

Garantizar un código limpio, escalable y fácil de mantener, siguiendo buenas prácticas de arquitectura en Node.js/Express.

---

## 🟢 Endpoint para selección y descarga de servidor Minecraft

**Peso:** 5

### 📋 Descripción Detallada

- Crear un endpoint que permita al usuario seleccionar el tipo de servidor (`vanilla`, `forge`, `fabric`) y la versión de Minecraft.
- Implementar la lógica para descargar el archivo JAR correspondiente desde internet.
- Almacenar el archivo JAR en Google Drive usando la API.
- Validar que la versión y el tipo de servidor sean compatibles antes de descargar.
- Manejar errores de descarga y notificar al usuario.

### 🎯 Objetivo

Automatizar la selección y descarga del servidor Minecraft, asegurando que los archivos estén disponibles en Google Drive para su posterior uso.

---

## 🟢 Gestión de configuración y mundos

**Peso:** 5

### 📋 Descripción Detallada

- Crear endpoints para:
  - Crear un nuevo mundo con configuración personalizada (nombre, semilla, modo, dificultad, etc.).
  - Listar los mundos existentes.
  - Eliminar mundos seleccionados.
  - Seleccionar un mundo activo.
- Guardar y leer las configuraciones de mundo en archivos JSON almacenados en Google Drive.
- Validar los datos de entrada y manejar errores.

### 🎯 Objetivo

Permitir a los usuarios gestionar múltiples mundos de Minecraft de forma sencilla y persistente, con almacenamiento seguro en Google Drive.

---

## 🟢 Integración con Google Drive

**Peso:** 8

### 📋 Descripción Detallada

- Implementar autenticación OAuth2 para acceder a Google Drive desde el backend.
- Crear funciones para subir, descargar, listar y eliminar archivos (JAR, mundos, configuraciones) en Google Drive.
- Manejar la renovación de tokens y errores de autenticación.
- Documentar el flujo de autenticación y permisos necesarios.

### 🎯 Objetivo

Asegurar que todos los archivos importantes del servidor Minecraft se gestionen y almacenen en Google Drive, igual que en el notebook de Colab.

---

## 🟢 Endpoint para aceptar EULA y archivos iniciales

**Peso:** 2

### 📋 Descripción Detallada

- Crear un endpoint que genere el archivo `eula.txt` con el contenido `eula=true` en Google Drive.
- Permitir la creación de otros archivos iniciales necesarios para el servidor (por ejemplo, carpetas de mods).
- Validar que el archivo se haya creado correctamente y notificar al usuario.

### 🎯 Objetivo

Automatizar la aceptación del EULA y la generación de archivos base para que el servidor pueda iniciarse sin intervención manual.

---

## 🟢 Iniciar y detener el servidor Minecraft

**Peso:** 8

### 📋 Descripción Detallada

- Crear endpoints para iniciar y detener el proceso del servidor Minecraft en el backend.
- Descargar los archivos necesarios desde Google Drive antes de iniciar.
- Monitorear el proceso y guardar logs.
- Asegurar que al detener el servidor, los mundos y configuraciones se sincronicen de vuelta a Google Drive.
- Manejar errores y estados del proceso.

### 🎯 Objetivo

Permitir el control total del ciclo de vida del servidor Minecraft desde la app web, con persistencia y seguridad.

---

## 🟢 Integración con túneles (playit.gg/ngrok)

**Peso:** 5

### 📋 Descripción Detallada

- Crear un endpoint para iniciar un túnel usando playit.gg o ngrok desde el backend.
- Obtener y devolver el enlace público generado al frontend.
- Monitorear el estado del túnel y reiniciarlo si es necesario.
- Documentar el uso y requisitos de los túneles.

### 🎯 Objetivo

Facilitar el acceso remoto al servidor Minecraft sin necesidad de abrir puertos manualmente, usando túneles seguros y automáticos.

---

## 🟢 Consola en tiempo real (Websockets)

**Peso:** 8

### 📋 Descripción Detallada

- Implementar un WebSocket en el backend para transmitir la salida de la consola del servidor Minecraft al frontend en tiempo real.
- Permitir enviar comandos desde el frontend al servidor a través del WebSocket.
- Manejar la reconexión y errores de comunicación.

### 🎯 Objetivo

Brindar una experiencia interactiva y en tiempo real para monitorear y controlar el servidor Minecraft desde la web.

---

## 🟢 Gestión de mods/plugins

**Peso:** 5

### 📋 Descripción Detallada

- Crear endpoints para subir, listar y eliminar mods/plugins en Google Drive.
- Validar los archivos subidos y su compatibilidad con el tipo de servidor.
- Sincronizar la carpeta de mods/plugins antes de iniciar el servidor.

### 🎯 Objetivo

Permitir a los usuarios personalizar su servidor Minecraft fácilmente, gestionando mods/plugins desde la app web.

---

## 🟢 Manejo de errores y validaciones

**Peso:** 3

### 📋 Descripción Detallada

- Implementar middlewares para manejo centralizado de errores en Express.
- Validar los datos de entrada en todos los endpoints.
- Devolver mensajes de error claros y útiles al frontend.

### 🎯 Objetivo

Aumentar la robustez y seguridad de la API, evitando errores inesperados y mejorando la experiencia de usuario.

---

## 🟢 Documentación de la API y despliegue

**Peso:** 3

### 📋 Descripción Detallada

- Documentar todos los endpoints de la API (puedes usar Swagger o README).
- Explicar el flujo de autenticación con Google Drive.
- Documentar el proceso de despliegue con Docker y variables de entorno necesarias.
- Incluir ejemplos de uso para desarrolladores y usuarios.

### 🎯 Objetivo

Facilitar el mantenimiento, la colaboración y el despliegue del backend, asegurando que cualquier desarrollador pueda entender y usar la API fácilmente.

---