const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.render('index', { uvData: null, error: null });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
