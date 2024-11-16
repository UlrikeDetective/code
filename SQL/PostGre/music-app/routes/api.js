const express = require('express');
const router = express.Router();
const axios = require('axios');

// Search albums using Deezer API
router.get('/search', async (req, res) => {
  const { query } = req.query; // Get the search query from the request
  if (!query) {
    return res.status(400).json({ error: 'Query parameter is required' });
  }

  try {
    const response = await axios.get(`https://api.deezer.com/search/album?q=${query}`);
    const albums = response.data.data.map(album => ({
      id: album.id,
      title: album.title,
      artist: album.artist.name,
      cover: album.cover_medium, // Use cover_medium or cover_big for higher resolution
      link: album.link,
    }));
    res.json(albums); // Send the album data back to the client
  } catch (error) {
    console.error('Error fetching from Deezer API:', error.message);
    res.status(500).json({ error: 'Failed to fetch album data' });
  }
});

module.exports = router;
