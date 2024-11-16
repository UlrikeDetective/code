const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const musicRoutes = require('./routes/music');
const apiRoutes = require('./routes/api');

app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/music', musicRoutes);
app.use('/api', apiRoutes);

app.get('/', (req, res) => res.redirect('/music'));

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
