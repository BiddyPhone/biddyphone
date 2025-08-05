const express = require('express');
const app = express();
const PORT = 3001;

app.use(express.json());

app.get('/api/rewards', (req, res) => {
  res.json({ sats: Math.floor(Math.random() * 20) + 100 });
});

app.post('/api/contact', (req, res) => {
  console.log('Contact form submitted:', req.body);
  res.status(200).json({ message: 'Contact received!' });
});

app.listen(PORT, () => {
  console.log(`Mock BiddyPhone API server running on http://localhost:${PORT}`);
});
