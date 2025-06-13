class ServerDownloader:
    forge_versions_map = {
        "1.21.1": "52.1.1",
        "1.20.1": "47.4.0",
        "1.19.1": "42.0.9",
        "1.18.1": "39.1.2",
        "1.17.1": "37.1.1",
        "1.16.2": "33.0.61",
        "1.15.1": "30.0.51",
        "1.14.2": "26.0.63",
        "1.13.2": "25.0.223",
        "1.12.1": "14.22.1.2485",
        "1.11.2": "13.20.1.2588",
        "1.10.2": "12.18.3.2511",
        "1.9.4": "12.17.0.2317",
        "1.8.8": "11.15.0.1655"
    }

    @staticmethod
    def descargar_jar(server_type, version, destino):
        import os
        import requests
        import json

        if server_type == 'forge':
            forge_version = ServerDownloader.forge_versions_map.get(version)
            if not forge_version:
                raise ValueError(f"Versión Forge no soportada: {version}")
            server_url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{version}-{forge_version}/forge-{version}-{forge_version}-installer.jar"
            jar_name = 'forge.jar'
        elif server_type == 'vanilla':
            server_url = f"https://mcutils.com/api/server-jars/vanilla/{version}/download"
            jar_name = 'vanilla.jar'
        elif server_type == 'fabric':
            server_url = 'https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.jar'
            jar_name = 'fabric-installer.jar'
        else:
            raise ValueError("Tipo de servidor no soportado")

        os.makedirs(destino, exist_ok=True)
        ruta_jar = os.path.join(destino, jar_name)
        respuesta = requests.get(server_url)
        if respuesta.status_code == 200:
            with open(ruta_jar, 'wb') as f:
                f.write(respuesta.content)
        else:
            raise RuntimeError(f"Error {respuesta.status_code}: la versión que elegiste no está disponible.")

        with open(os.path.join(destino, "config.json"), 'w') as f:
            json.dump({"server_type": server_type, "server_version": version}, f)

        with open(os.path.join(destino, "eula.txt"), 'w') as f:
            f.write("eula=true\n")

# Exponer la función para importación directa
descargar_jar = ServerDownloader.descargar_jar
