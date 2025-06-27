class ForgeService {
  /**
   * Obtiene las versiones soportadas por Forge
   */
  async getSupportedVersions() {
    try {
      const forgeVersions = [
        '1.21.1', '1.20.1', '1.19.1'
      ];
      
      return {
        success: true,
        versions: forgeVersions,
        total: forgeVersions.length
      };
    } catch (error) {
      return {
        success: false,
        versions: ['1.20.1', '1.19.1'],
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
      '1.20.1': '47.2.0',
      '1.19.1': '42.0.0'
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
