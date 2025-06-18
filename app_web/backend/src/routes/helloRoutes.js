import { Router } from 'express';
import { hello } from '../controllers/helloController.js';

const router = Router();

router.get('/', hello);

export default router;
