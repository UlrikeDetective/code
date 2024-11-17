const express = require('express');
const router = express.Router();
const axios = require('axios');

// Render the Add/Search page
router.get('/', (req, res) => {
  try {
    res.render('addMusic'); // Load the view for adding/searching music
  } catch (err) {
    console.error('Error rendering the Add/Search page:', err.message);
    res.status(500).send('An error occurred while loading the page.');
  }
});

// Search for songs using the API
router.get('/search', async (req, res) => {
  const { query } = req.query;

  // Validate query parameter
  if (!query) {
    return res.status(400).json({ error: 'Query parameter is required.' });
  }

  try {
    // Fetch songs from Deezer API
    const response = await axios.get(`https://api.deezer.com/search?q=${encodeURIComponent(query)}`);
    const songs = response.data.data.map(song => ({
      title: song.title,
      artist: song.artist.name,
      album: song.album.title,
      cover: song.album.cover_medium,
    }));

    // Respond with the list of songs
    res.json(songs);
  } catch (err) {
    console.error('Error fetching from Deezer API:', err.message);

    // Determine error type and respond accordingly
    if (err.response) {
      // Error response from the API
      res.status(err.response.status).json({ error: err.response.data.error.message });
    } else {
      // General server or network error
      res.status(500).json({ error: 'Failed to fetch songs. Please try again later.' });
    }
  }
});

module.exports = router;
