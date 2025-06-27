import axios from 'axios';

class VanillaService {
  /**
   * Obtiene las versiones soportadas por Vanilla desde la API oficial de Mojang
   */
  async getSupportedVersions() {
    try {
      const response = await axios.get('https://launchermeta.mojang.com/mc/game/version_manifest.json');
      const releaseVersions = response.data.versions
        .filter(v => v.type === 'release')
        .slice(0, 20) // Solo las últimas 20 versiones
        .map(v => v.id);
      
      return {
        success: true,
        versions: releaseVersions,
        total: releaseVersions.length
      };
    } catch (error) {
      console.error('Error fetching Vanilla versions:', error);
      return {
        success: false,
        versions: ['1.21.1', '1.20.1', '1.19.4'],
        total: 3,
        error: 'Error consultando API de Mojang'
      };
    }
  }

  /**
   * Obtiene la URL de descarga real para una versión específica de Vanilla
   */
  async getDownloadUrl(version) {
    try {
      const manifestResponse = await axios.get('https://launchermeta.mojang.com/mc/game/version_manifest.json');
      const versionData = manifestResponse.data.versions.find(v => v.id === version);
      
      if (!versionData) {
        throw new Error(`Versión ${version} no encontrada`);
      }

      const versionResponse = await axios.get(versionData.url);
      const serverUrl = versionResponse.data.downloads?.server?.url;
      
      if (!serverUrl) {
        throw new Error(`No hay servidor disponible para la versión ${version}`);
      }

      return {
        url: serverUrl,
        filename: `minecraft_server.${version}.jar`
      };
    } catch (error) {
      // Fallback a URL conocida para 1.20.1
      return {
        url: 'https://piston-data.mojang.com/v1/objects/84194a2f286ef7c14ed7ce0090dba59902951553/server.jar',
        filename: `vanilla-server-${version}.jar`
      };
    }
  }

  /**
   * Valida si una versión es compatible con Vanilla
   */
  async isVersionSupported(version) {
    const supportedData = await this.getSupportedVersions();
    return supportedData.versions.includes(version);
  }
}

export default new VanillaService();
