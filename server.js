const express = require('express');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

// Serve static frontend files
app.use(express.static(path.join(__dirname, 'public')));

// Serve examples directory at /examples
app.use('/examples', express.static(path.join(__dirname, 'examples')));

// Health endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', uptime: process.uptime() });
});

// Basic info endpoint
app.get('/info', (req, res) => {
  res.json({
    name: 'python-playground',
    description: 'Interactive browser-based Python playground using Pyodide',
    version: '1.0.0'
  });
});

app.listen(port, () => {
  console.log(`Python-playground server listening on http://localhost:${port}`);
});
