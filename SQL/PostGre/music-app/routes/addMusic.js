const express = require('express');
const router = express.Router();
const axios = require('axios');

// Render the Add/Search page
router.get('/', (req, res) => {
  res.render('addMusic'); // This will load the new view for adding/searching music
});

// Search for songs using the API
router.get('/search', async (req, res) => {
  const { query } = req.query;

  if (!query) {
    return res.status(400).json({ error: 'Query parameter is required' });
  }

  try {
    const response = await axios.get(`https://api.deezer.com/search?q=${query}`);
    const songs = response.data.data.map(song => ({
      title: song.title,
      artist: song.artist.name,
      album: song.album.title,
      cover: song.album.cover_medium,
    }));
    res.json(songs);
  } catch (err) {
    console.error('Error fetching from API:', err.message);
    res.status(500).json({ error: 'Failed to fetch songs.' });
  }
});

module.exports = router;
