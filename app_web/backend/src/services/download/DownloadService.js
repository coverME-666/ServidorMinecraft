import axios from 'axios';
import fs from 'fs-extra';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

class DownloadService {
  constructor() {
    this.downloadDir = path.join(__dirname, '../../../downloads');
  }

  /**
   * Descarga un archivo JAR desde una URL
   */
  async downloadFile(url, filename) {
    try {
      console.log(`📥 Descargando ${filename} desde: ${url}`);
      
      // Crear directorio de descargas si no existe
      await fs.ensureDir(this.downloadDir);
      
      // Ruta local del archivo
      const localPath = path.join(this.downloadDir, filename);
      
      // Descargar archivo
      const response = await axios({
        method: 'GET',
        url: url,
        responseType: 'stream',
        timeout: 300000 // 5 minutos de timeout
      });
      
      // Guardar archivo localmente
      const writer = fs.createWriteStream(localPath);
      response.data.pipe(writer);
      
      return new Promise((resolve, reject) => {
        writer.on('finish', () => {
          console.log(`✅ Descarga completada: ${filename}`);
          const stats = fs.statSync(localPath);
          resolve({
            success: true,
            localPath: localPath,
            filename: filename,
            size: stats.size,
            sizeFormatted: this.formatFileSize(stats.size)
          });
        });
        
        writer.on('error', (error) => {
          console.error('❌ Error writing file:', error);
          reject(new Error('Error guardando el archivo descargado'));
        });

        response.data.on('error', (error) => {
          console.error('❌ Error downloading:', error);
          reject(new Error('Error durante la descarga'));
        });
      });
      
    } catch (error) {
      console.error('❌ Error downloading file:', error);
      throw new Error(`Error descargando archivo: ${error.message}`);
    }
  }

  /**
   * Formatea el tamaño de archivo en una unidad legible
   */
  formatFileSize(bytes) {
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    if (bytes === 0) return '0 Bytes';
    const i = Math.floor(Math.log(bytes) / Math.log(1024));
    return Math.round(bytes / Math.pow(1024, i) * 100) / 100 + ' ' + sizes[i];
  }

  /**
   * Limpia archivos antiguos del directorio de descargas
   */
  async cleanOldFiles(maxAgeHours = 24) {
    try {
      const files = await fs.readdir(this.downloadDir);
      const now = Date.now();
      const maxAge = maxAgeHours * 60 * 60 * 1000;

      for (const file of files) {
        const filePath = path.join(this.downloadDir, file);
        const stats = await fs.stat(filePath);
        
        if (now - stats.mtime.getTime() > maxAge) {
          await fs.remove(filePath);
          console.log(`🗑️ Archivo antiguo eliminado: ${file}`);
        }
      }
    } catch (error) {
      console.error('❌ Error al limpiar archivos:', error.message);
    }
  }
}

export default new DownloadService();
