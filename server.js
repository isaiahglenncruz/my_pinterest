// server.js
const express = require('express');
const bodyParser = require('body-parser');
const multer = require('multer');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

// 404
app.use((req, res, next) => {
    res.status(404).sendFile(path.join(__dirname, 'views', 'error.html'));
});

// server start
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
