import express from 'express';
import serverController from '../controllers/serverController.js';

const router = express.Router();

/**
 * @route GET /api/server/versions
 * @description Obtiene las versiones disponibles de Minecraft y tipos soportados
 * @access Public
 * @returns {Object} Lista de versiones y tipos soportados
 */
router.get('/versions', (req, res) => serverController.getVersions(req, res));

/**
 * @route POST /api/server/download
 * @description Descarga y sube un servidor Minecraft a Google Drive
 * @access Public
 * @body {Object} { type: string, version: string }
 * @returns {Object} Estado de la descarga iniciada  
 */
router.post('/download', (req, res) => serverController.downloadServer(req, res));

/**
 * @route GET /api/server/compatibility/:type/:version
 * @description Verifica si una combinación tipo-versión es compatible
 * @access Public
 * @param {string} type - Tipo de servidor (vanilla, forge, fabric)
 * @param {string} version - Versión de Minecraft
 * @returns {Object} Información de compatibilidad
 */
router.get('/compatibility/:type/:version', (req, res) => serverController.checkCompatibility(req, res));

/**
 * @route GET /api/server/status
 * @description Estado general del servicio de servidores
 * @access Public
 * @returns {Object} Estado del servicio y endpoints disponibles
 */
router.get('/status', (req, res) => serverController.getStatus(req, res));

export default router;