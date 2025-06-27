class ForgeService {
  /**
   * Obtiene las versiones soportadas por Forge
   */
  async getSupportedVersions() {
    try {
      // En un caso ideal, consultaríamos la API de Forge
      // Por ahora usamos versiones conocidas que sabemos que funcionan
      const forgeVersions = [
        '1.21.1', '1.21', '1.20.6', '1.20.4', '1.20.2', '1.20.1',
        '1.19.4', '1.19.3', '1.19.2', '1.19.1', '1.19',
        '1.18.2', '1.18.1', '1.18',
        '1.17.1', '1.17',
        '1.16.5', '1.16.4'
      ];
      
      return {
        success: true,
        versions: forgeVersions,
        total: forgeVersions.length
      };
    } catch (error) {
      return {
        success: false,
        versions: ['1.20.1', '1.19.4'],
        total: 2
      };
    }
  }

  /**
   * Obtiene la URL de descarga para Forge
   */
  async getDownloadUrl(version) {
    const forgeVersion = this.getForgeVersionFor(version);
    return {
      url: `https://maven.minecraftforge.net/net/minecraftforge/forge/${version}-${forgeVersion}/forge-${version}-${forgeVersion}-installer.jar`,
      filename: `forge-${version}-${forgeVersion}-installer.jar`
    };
  }

  /**
   * Obtiene la versión de Forge correspondiente a una versión de Minecraft
   */
  getForgeVersionFor(mcVersion) {
    const forgeVersions = {
      '1.21.1': '52.0.0',
      '1.21': '51.0.0',
      '1.20.6': '50.1.0',
      '1.20.4': '49.1.0',
      '1.20.2': '48.1.0',
      '1.20.1': '47.2.0',
      '1.19.4': '45.2.0',
      '1.19.3': '44.1.0',
      '1.19.2': '43.3.0',
      '1.19.1': '42.0.0',
      '1.19': '41.1.0',
      '1.18.2': '40.2.0',
      '1.18.1': '39.1.0',
      '1.18': '38.0.0',
      '1.17.1': '37.1.0',
      '1.17': '36.2.0',
      '1.16.5': '36.2.0',
      '1.16.4': '35.1.0'
    };
    
    return forgeVersions[mcVersion] || '47.2.0'; // Fallback
  }

  /**
   * Valida si una versión es compatible con Forge
   */
  async isVersionSupported(version) {
    const supportedData = await this.getSupportedVersions();
    return supportedData.versions.includes(version);
  }
}

export default new ForgeService();
