const express = require('express');
const axios = require('axios');
const router = express.Router();

// Search music by title, artist, or album
router.get('/search', async (req, res) => {
  const { query } = req.query; // Get the search query
  if (!query) {
    return res.status(400).json({ error: 'Query parameter is required' });
  }

  try {
    const response = await axios.get(`https://api.deezer.com/search?q=${encodeURIComponent(query)}`);
    const musicResults = response.data.data.map(track => ({
      id: track.id,
      title: track.title,
      artist: track.artist.name,
      album: track.album.title,
      cover: track.album.cover_medium, // Medium-resolution cover
      link: track.link, // Link to the track on Deezer
    }));
    res.json(musicResults); // Send the results back to the client
  } catch (error) {
    console.error('Error fetching music from Deezer API:', error.message);
    res.status(500).json({ error: 'Failed to fetch music data' });
  }
});

module.exports = router;
