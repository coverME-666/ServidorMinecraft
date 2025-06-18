import dotenv from 'dotenv';
dotenv.config();
import express from 'express';
import cors from 'cors';
import helloRoutes from './routes/helloRoutes.js';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: "OK" });
});

app.use('/api/hello', helloRoutes);

app.listen(PORT, () => {
  console.log(`🚀 hello world desde: http://localhost:${PORT}`);
});
