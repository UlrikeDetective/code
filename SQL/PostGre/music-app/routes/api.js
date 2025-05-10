const express = require('express');
const axios = require('axios');
const router = express.Router();

// Search music by title, artist, or album
router.get('/search', async (req, res) => {
  const { query } = req.query; // Get the search query

  // Validate the search query
  if (!query || query.trim() === '') {
    return res.status(400).json({ error: 'Query parameter is required and cannot be empty.' });
  }

  try {
    // Fetch music data from Deezer API
    const response = await axios.get(`https://api.deezer.com/search?q=${encodeURIComponent(query)}`);

    // Map results to the desired format
    const musicResults = response.data.data.map(track => ({
      id: track.id,
      title: track.title,
      artist: track.artist.name,
      album: track.album.title,
      cover: track.album.cover_medium, // Medium-resolution cover
      link: track.link, // Link to the track on Deezer
    }));

    // Respond with the search results
    res.json(musicResults);
  } catch (error) {
    console.error('Error fetching music from Deezer API:', error.message);

    // Handle API response errors or unexpected issues
    if (error.response) {
      // API responded with an error
      res.status(error.response.status).json({ error: error.response.data.error.message });
    } else {
      // General server or network error
      res.status(500).json({ error: 'Failed to fetch music data. Please try again later.' });
    }
  }
});

module.exports = router;
