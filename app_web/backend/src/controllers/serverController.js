import serverService from '../services/serverService.js';

class ServerController {
  
  /**
   * GET /api/server/versions
   * Obtiene las versiones disponibles de Minecraft y tipos soportados
   */
  async getVersions(req, res) {
    try {
      console.log('Solicitando versiones disponibles...');
      
      const result = await serverService.getAvailableVersions();
      
      res.status(200).json({
        success: true,
        message: 'Versiones obtenidas exitosamente',
        data: {
          supportedTypes: result.supportedTypes.map(type => ({
            id: type,
            name: this.getTypeDisplayName(type),
            description: this.getTypeDescription(type)
          })),
          versions: result.versions,
          total: result.versions.length
        }
      });
      
    } catch (error) {
      console.error('Error getting versions:', error);
      res.status(500).json({
        success: false,
        message: 'Error obteniendo las versiones de Minecraft',
        error: error.message
      });
    }
  }

  /**
   * POST /api/server/download
   * Descarga y sube un servidor Minecraft a Google Drive
   */
  async downloadServer(req, res) {
    try {
      const { type, version } = req.body;
      
      // Validar parámetros requeridos
      if (!type || !version) {
        return res.status(400).json({
          success: false,
          message: 'Faltan parámetros requeridos',
          error: 'Los campos "type" y "version" son obligatorios',
          example: {
            type: 'vanilla',
            version: '1.20.1'
          }
        });
      }

      console.log(`Procesando solicitud de descarga: ${type} ${version}`);

      // Validar compatibilidad
      const compatibility = await serverService.validateCompatibility(type, version);
      if (!compatibility.compatible) {
        return res.status(400).json({
          success: false,
          message: 'Combinación no compatible',
          error: compatibility.message,
          suggestion: 'Verifica las versiones disponibles en /api/server/versions'
        });
      }

      // Informar que el proceso ha comenzado
      res.status(202).json({
        success: true,
        message: 'Descarga iniciada',
        status: 'processing',
        details: {
          type: type,
          version: version,
          compatibility: compatibility.message,
          estimatedTime: '2-5 minutos'
        }
      });

      // Procesar descarga en segundo plano
      this.processDownloadInBackground(type, version, req);

    } catch (error) {
      console.error('Error processing download request:', error);
      res.status(500).json({
        success: false,
        message: 'Error procesando la solicitud de descarga',
        error: error.message
      });
    }
  }

  /**
   * GET /api/server/compatibility/:type/:version
   * Verifica si una combinación tipo-versión es compatible
   */
  async checkCompatibility(req, res) {
    try {
      const { type, version } = req.params;
      
      if (!type || !version) {
        return res.status(400).json({
          success: false,
          message: 'Parámetros incompletos',
          error: 'Se requieren tipo y versión en la URL'
        });
      }

      console.log(`Verificando compatibilidad: ${type} ${version}`);
      
      const compatibility = await serverService.validateCompatibility(type, version);
      
      res.status(200).json({
        success: true,
        message: 'Compatibilidad verificada',
        data: {
          type: type,
          version: version,
          compatible: compatibility.compatible,
          message: compatibility.message,
          typeInfo: {
            name: this.getTypeDisplayName(type),
            description: this.getTypeDescription(type)
          }
        }
      });
      
    } catch (error) {
      console.error('Error checking compatibility:', error);
      res.status(500).json({
        success: false,
        message: 'Error verificando compatibilidad',
        error: error.message
      });
    }
  }

  /**
   * GET /api/server/status
   * Estado general del servicio de servidores
   */
  async getStatus(req, res) {
    try {
      res.status(200).json({
        success: true,
        message: 'Servicio de servidores operativo',
        data: {
          service: 'server-download',
          status: 'operational',
          supportedTypes: ['vanilla', 'forge', 'fabric'],
          features: {
            download: true,
            googleDriveUpload: true, // Será true cuando se implemente completamente
            versionValidation: true,
            compatibilityCheck: true
          },
          endpoints: {
            versions: '/api/server/versions',
            download: '/api/server/download',
            compatibility: '/api/server/compatibility/:type/:version',
            status: '/api/server/status'
          }
        }
      });
    } catch (error) {
      res.status(500).json({
        success: false,
        message: 'Error obteniendo estado del servicio',
        error: error.message
      });
    }
  }

  /**
   * Procesa la descarga en segundo plano
   * En una implementación real, esto se haría con un sistema de colas
   */
  async processDownloadInBackground(type, version, req) {
    try {
      console.log(`Iniciando descarga en segundo plano: ${type} ${version}`);
      
      const result = await serverService.downloadAndUploadServer(type, version);
      
      console.log('Descarga completada exitosamente:', result);
      
      // En una implementación real, aquí se notificaría al usuario
      // mediante WebSockets, webhooks, o un sistema de notificaciones
      
    } catch (error) {
      console.error('Error en descarga en segundo plano:', error);
      
      // En una implementación real, aquí se notificaría el error al usuario
    }
  }

  /**
   * Obtiene el nombre para mostrar de un tipo de servidor
   */
  getTypeDisplayName(type) {
    const displayNames = {
      vanilla: 'Minecraft Vanilla',
      forge: 'Minecraft Forge',
      fabric: 'Minecraft Fabric'
    };
    return displayNames[type.toLowerCase()] || type;
  }

  /**
   * Obtiene la descripción de un tipo de servidor
   */
  getTypeDescription(type) {
    const descriptions = {
      vanilla: 'Servidor oficial de Minecraft sin modificaciones',
      forge: 'Servidor con soporte para mods de Forge',
      fabric: 'Servidor moderno y ligero con soporte para mods de Fabric'
    };
    return descriptions[type.toLowerCase()] || 'Servidor de Minecraft';
  }
}

const serverController = new ServerController();
export default serverController;