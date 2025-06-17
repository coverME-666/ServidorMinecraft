# 🟩 Minecraft Server Launcher – App Web y Google Colab

Este proyecto tiene **dos versiones** para facilitar la creación y gestión de servidores de Minecraft:

---

## 🌐 Versión 1: App Web

Permite a cualquier usuario crear, configurar e iniciar un servidor de Minecraft desde una interfaz web sencilla, con soporte para túnel (playit.gg) y almacenamiento de archivos persistente.

### 🚀 Objetivo del Proyecto Web

- Crear y gestionar servidores Minecraft desde cualquier navegador.
- Seleccionar tipo de servidor: `vanilla`, `forge`, `fabric`.
- Elegir versión de Minecraft.
- Configurar y crear mundos personalizados.
- Iniciar y detener el servidor desde la web.
- Ver la consola y el estado del servidor en tiempo real.
- Mostrar y copiar el enlace del túnel (playit.gg).
- (Opcional) Subir y gestionar mods/plugins.

### 🧰 Tecnologías Web

- **Backend:** Python (FastAPI/Flask) o Node.js (Express)
- **Frontend:** HTML, CSS, JS (Bootstrap, React, Vue, etc.)
- **Websockets:** Para consola en tiempo real
- **Base de datos:** SQLite/PostgreSQL/MySQL (según necesidad)
- **Almacenamiento:** Local, Google Drive, o S3 (según despliegue)
- **Infraestructura:** VPS propio o nube (Railway, Oracle Cloud, etc.)

---

## ☁️ Versión 2: Google Colab Mejorado

Notebook interactivo para lanzar servidores Minecraft en la nube de Google Colab, con almacenamiento persistente en Google Drive.

### 🚀 Objetivo del Proyecto Colab

- Ejecutar servidores Minecraft en la nube, sin instalar nada en la PC.
- Usar widgets interactivos para seleccionar tipo, versión y configuración del servidor.
- Descargar y preparar el servidor automáticamente en Google Drive.
- Iniciar el servidor y exponerlo con playit.gg.
- Compartir el notebook fácilmente con amigos.

### 🧰 Tecnologías Colab

- **Google Colab** (máquina virtual Linux gratis)
- **ipywidgets** para la interfaz interactiva
- **requests** para descargas
- **playit.gg** para túnel
- **Google Drive** para almacenamiento persistente

---

## 📦 Estructura Recomendada

```
ServerMine/
├── app_web/                ← Código fuente de la app web
│   ├── backend/
│   ├── frontend/
│   └── ...
├── ServerColab.ipynb       ← Notebook de Google Colab mejorado
├── requirements.txt
└── README.md
```

---

## 🔒 Permisos necesarios

- **Web:** El servidor debe tener permisos para ejecutar procesos y escribir archivos.
- **Colab:** Solo necesitas una cuenta de Google.

---

## 🛣️ Roadmap

- [ ] Mejorar la experiencia en Google Colab (más widgets, menos pasos manuales)
- [ ] Prototipo funcional de la app web (backend + frontend)
- [ ] Consola en tiempo real y gestión de túnel en la web
- [ ] Gestión de mundos y mods/plugins
- [ ] Documentación y guía para usuarios

---

## 📄 Licencia

Este proyecto es de código abierto y se distribuye bajo la licencia MIT.