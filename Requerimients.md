# 🟩 Minecraft Server Launcher – Web & Colab

Este proyecto tiene dos versiones principales para lanzar y gestionar servidores de Minecraft de forma sencilla, ambas con gestión de archivos y mundos en Google Drive:

---

### 🌐 Versión 1: App Web
Permite a cualquier usuario crear, configurar e iniciar un servidor de Minecraft desde una interfaz web sencilla, con soporte para túnel (playit.gg) y **almacenamiento de archivos persistente en Google Drive**.

#### 🚀 Objetivo del Proyecto Web
- Crear y gestionar servidores Minecraft desde cualquier navegador.
- Seleccionar tipo de servidor: `vanilla`, `forge`, `fabric`.
- Elegir versión de Minecraft.
- Configurar y crear mundos personalizados.
- Iniciar y detener el servidor desde la web.
- Ver la consola y el estado del servidor en tiempo real.
- Mostrar y copiar el enlace del túnel (playit.gg o Ngrok).
- (Opcional) Subir y gestionar mods/plugins.
- **Todos los archivos del servidor, mundos y configuraciones se almacenan y gestionan en Google Drive del usuario, igual que en Colab.**

#### 🧰 Tecnologías Web
- **Backend:** Node.js (Express) o Python (FastAPI/Flask)
- **Frontend:** React + Vite, HTML, CSS, JS (Bootstrap, Vue, etc.)
- **Websockets:** Para consola en tiempo real
- **Almacenamiento:** Google Drive (API), igual que en Colab
- **Infraestructura:** VPS propio, nube o local (Docker)

**Estructura:**
```
app_web/
  frontend/   # React + Vite
  backend/    # Node.js + Express
```

---

### 📓 Versión 2: Notebook Interactivo (Google Colab)
Un notebook mejorado para lanzar servidores Minecraft en la nube, pensado para usuarios que prefieren Google Colab:
- Lanzamiento de servidores Minecraft en entornos cloud temporales.
- Almacenamiento de mundos y configuraciones en Google Drive.
- Interfaz interactiva y fácil de usar.
- Automatización de instalación y ejecución.

**Tecnologías:**
- Python 3.x
- Google Colab
- Google Drive API

**Estructura:**
```
ServerColab.ipynb
```

---

## 🚀 Objetivo General
Permitir a cualquier usuario crear, configurar e iniciar servidores de Minecraft fácilmente desde la web o desde Google Colab, con almacenamiento seguro y acceso sencillo en Google Drive.

## 🛣️ Roadmap General
- [x] Definir arquitectura y tecnologías
- [x] Crear estructura base de carpetas y archivos
- [ ] Implementar backend Express (API, gestión de mundos, túneles, integración con Google Drive)
- [ ] Implementar frontend React (UI moderna, gestión de servidores)
- [ ] Mejorar notebook de Colab (automatización, integración con Drive)
- [ ] Documentar y probar ambos flujos

## 📦 Requisitos
- Tener Docker instalado (para la app web)
- Tener cuenta de Google (para Colab, Drive y la app web)
- (Opcional) Tener Java instalado si se ejecuta localmente

## 📄 Licencia
Este proyecto es de código abierto y se distribuye bajo la licencia MIT 