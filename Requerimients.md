# 🟩 Minecraft Server Launcher – Cliente de Escritorio (PyQt)

Este proyecto es una aplicación de escritorio desarrollada en **Python** usando **PyQt**, cuyo objetivo es permitir a cualquier usuario crear, configurar e iniciar un servidor de Minecraft fácilmente desde una interfaz gráfica.

## 🚀 Objetivo del Proyecto
Crear un **cliente gráfico en Python** para:
- Seleccionar tipo de servidor: `vanilla`, `forge`, `fabric`
- Elegir versión de Minecraft
- Elegir o generar mundo
- Iniciar el servidor local
- (Opcional) Descargar automáticamente los JARs si no existen

## 🧰 Tecnologías

- **Python 3.10+**
- **PyQt5** para la interfaz gráfica
- **requests** para descarga de archivos
- **json** para guardar configuración del servidor
- **subprocess** para ejecutar comandos del sistema

## 📦 Requisitos

Instala las dependencias con:

```bash
minecraft-launcher/
├── launcher.py          ← Cliente gráfico principal (Tkinter o PyQt)
├── core/
│   ├── server_manager.py ← Lógica para iniciar servidores
│   ├── downloader.py     ← Descarga de archivos JAR (opcional)
│   └── config.py         ← Rutas, versiones soportadas, etc.
├── assets/
│   └── icon.ico          ← Ícono para la ventana (opcional)
├── servers/
│   └── vanilla-1.20.1.jar (etc.)
├── worlds/
│   └── mi_mundo/
└── requirements.txt
```
## 🔒 Permisos necesarios

- Asegúrate de tener Java instalado (versión 8+) 
- El cliente debe tener permiso para escribir en disco y ejecutar procesos

## 🛣️ Roadmap
 - Cargar tipos y versiones de servidor
 - Descargar archivos según selección
 - Mostrar estado de progreso
 - Guardar configuraciones previas
 - Botón para iniciar el servidor
 - Logs y feedback visual

## 📄 Licencia
Este proyecto es de código abierto y se distribuye bajo la licencia MIT.