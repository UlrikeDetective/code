const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const musicRoutes = require('./routes/music'); // For saved songs
const addMusicRoutes = require('./routes/addMusic'); // For add/search music

app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.use('/saved', musicRoutes); // Saved songs
app.use('/add', addMusicRoutes); // Add music manually or search for songs

// Homepage redirects to add music
app.get('/', (req, res) => res.redirect('/add'));

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
