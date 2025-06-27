import axios from 'axios';

class FabricService {
  /**
   * Obtiene las versiones soportadas por Fabric desde su API oficial
   */
  async getSupportedVersions() {
    try {
      const response = await axios.get('https://meta.fabricmc.net/v2/versions/game');
      const stableVersions = response.data
        .filter(v => v.stable)
        .map(v => v.version)
        .slice(0, 15); // Solo las últimas 15 versiones estables
      
      return {
        success: true,
        versions: stableVersions,
        total: stableVersions.length
      };
    } catch (error) {
      console.error('Error fetching Fabric versions:', error);
      return {
        success: false,
        versions: ['1.20.1', '1.19.4', '1.19.2'], // Fallback
        total: 3,
        error: 'Error consultando API de Fabric'
      };
    }
  }

  /**
   * Obtiene la última versión del loader de Fabric
   */
  async getLatestLoaderVersion() {
    try {
      const response = await axios.get('https://meta.fabricmc.net/v2/versions/loader');
      return response.data[0].version;
    } catch (error) {
      return '0.15.1'; // Fallback
    }
  }

  /**
   * Obtiene la URL de descarga para Fabric
   */
  async getDownloadUrl(version) {
    try {
      const loaderVersion = await this.getLatestLoaderVersion();
      
      // Usar el instalador de Fabric que es más confiable
      return {
        url: 'https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.0/fabric-installer-1.0.0.jar',
        filename: `fabric-installer-${version}.jar`
      };
    } catch (error) {
      return {
        url: 'https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.0/fabric-installer-1.0.0.jar',
        filename: `fabric-installer-${version}.jar`
      };
    }
  }

  /**
   * Valida si una versión es compatible con Fabric
   */
  async isVersionSupported(version) {
    const supportedData = await this.getSupportedVersions();
    return supportedData.versions.includes(version);
  }
}

export default new FabricService();
