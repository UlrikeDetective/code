const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const musicRoutes = require('./routes/music'); // For saved songs
const addMusicRoutes = require('./routes/addMusic'); // For add/search music

// Set EJS as the view engine
app.set('view engine', 'ejs');

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Middleware to parse incoming requests with URL-encoded payloads (forms)
app.use(bodyParser.urlencoded({ extended: true }));

// Middleware to parse JSON payloads for API routes
app.use(express.json());

// Define routes
app.use('/saved', musicRoutes); // Saved songs
app.use('/add', addMusicRoutes); // Add music manually or search for songs

// Homepage redirects to the Add Music page
app.get('/', (req, res) => res.redirect('/add'));

// Start the server on port 3000
app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
