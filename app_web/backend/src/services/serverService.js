import VanillaService from './vanilla/VanillaService.js';
import ForgeService from './forge/ForgeService.js';
import FabricService from './fabric/FabricService.js';
import DownloadService from './download/DownloadService.js';
import GoogleDriveService from './drive/GoogleDriveService.js';

class ServerService {
  constructor() {
    this.supportedTypes = ['vanilla', 'forge', 'fabric'];
    this.services = {
      vanilla: VanillaService,
      forge: ForgeService,
      fabric: FabricService
    };
  }

  /**
   * Obtiene las versiones disponibles de todos los tipos de servidor
   */
  async getAvailableVersions() {
    try {
      console.log('🔍 Consultando versiones disponibles...');
      
      // Obtener versiones en paralelo
      const [vanillaData, forgeData, fabricData] = await Promise.all([
        this.services.vanilla.getSupportedVersions(),
        this.services.forge.getSupportedVersions(),
        this.services.fabric.getSupportedVersions()
      ]);

      return {
        success: true,
        supportedTypes: this.supportedTypes,
        versionsByType: {
          vanilla: {
            versions: vanillaData.versions,
            total: vanillaData.total,
            apiStatus: vanillaData.success ? 'OK' : 'Error'
          },
          forge: {
            versions: forgeData.versions,
            total: forgeData.total,
            apiStatus: forgeData.success ? 'OK' : 'Error'
          },
          fabric: {
            versions: fabricData.versions,
            total: fabricData.total,
            apiStatus: fabricData.success ? 'OK' : 'Error'
          }
        },
        commonVersions: this.findCommonVersions(
          vanillaData.versions, 
          forgeData.versions, 
          fabricData.versions
        ),
        lastUpdated: new Date().toISOString()
      };
    } catch (error) {
      console.error('Error fetching versions:', error);
      throw new Error('No se pudieron obtener las versiones de Minecraft');
    }
  }

  /**
   * Valida si una combinación tipo-versión es compatible
   */
  async validateCompatibility(type, version) {
    try {
      const normalizedType = type.toLowerCase();
      
      if (!this.supportedTypes.includes(normalizedType)) {
        return {
          compatible: false,
          message: `Tipo de servidor no reconocido. Tipos válidos: ${this.supportedTypes.join(', ')}`
        };
      }

      const service = this.services[normalizedType];
      const isSupported = await service.isVersionSupported(version);
      const supportedData = await service.getSupportedVersions();

      return {
        compatible: isSupported,
        message: isSupported 
          ? `${normalizedType.charAt(0).toUpperCase() + normalizedType.slice(1)} soporta esta versión` 
          : `${normalizedType.charAt(0).toUpperCase() + normalizedType.slice(1)} no soporta la versión ${version}`,
        supportedVersions: supportedData.versions.slice(0, 10),
        apiStatus: supportedData.success ? 'OK' : 'Error consultando API'
      };
    } catch (error) {
      console.error('Error validating compatibility:', error);
      return {
        compatible: false,
        message: 'Error validando compatibilidad',
        error: error.message
      };
    }
  }

  /**
   * Descarga y sube un servidor a Google Drive
   */
  async downloadAndUploadServer(type, version) {
    try {
      const normalizedType = type.toLowerCase();
      
      if (!this.supportedTypes.includes(normalizedType)) {
        throw new Error(`Tipo de servidor no soportado. Tipos válidos: ${this.supportedTypes.join(', ')}`);
      }

      console.log(`🚀 Iniciando proceso completo para ${normalizedType} ${version}`);
      
      // Paso 1: Obtener URL de descarga
      const service = this.services[normalizedType];
      const downloadInfo = await service.getDownloadUrl(version);
      
      // Paso 2: Descargar archivo
      const downloadResult = await DownloadService.downloadFile(
        downloadInfo.url, 
        downloadInfo.filename
      );
      
      // Paso 3: Subir a Google Drive
      const uploadResult = await GoogleDriveService.uploadFile(
        downloadResult.localPath, 
        downloadResult.filename
      );
      
      // Paso 4: Limpiar archivo local (opcional)
      try {
        await DownloadService.cleanOldFiles(1); // Limpiar archivos de más de 1 hora
        console.log('🧹 Limpieza de archivos completada');
      } catch (cleanupError) {
        console.warn('⚠️ Error en limpieza:', cleanupError.message);
      }
      
      return {
        success: true,
        type: normalizedType,
        version: version,
        filename: downloadResult.filename,
        size: downloadResult.size,
        sizeFormatted: downloadResult.sizeFormatted,
        driveFileId: uploadResult.driveFileId,
        driveUrl: uploadResult.driveUrl,
        message: `Servidor ${normalizedType} ${version} descargado y subido exitosamente`
      };
      
    } catch (error) {
      console.error('❌ Error in complete download process:', error);
      throw error;
    }
  }

  /**
   * Encuentra versiones comunes entre todos los tipos de servidor
   */
  findCommonVersions(vanillaVersions, forgeVersions, fabricVersions) {
    return vanillaVersions.filter(version => 
      forgeVersions.includes(version) && fabricVersions.includes(version)
    ).slice(0, 10);
  }
}

export default new ServerService();