const express = require('express');
const router = express.Router();
const pool = require('../database'); // Ensure you have a database.js that exports a pg.Pool instance

// Render the music page
router.get('/', (req, res) => {
  res.render('music');
});

// Add a route to handle saving albums
router.post('/add', async (req, res) => {
    const { title, artist, album_cover_url, rating } = req.body;
  
    // Debug: Log incoming request data
    console.log('Request body:', req.body);
  
    if (!title || !artist || !album_cover_url) {
      console.log('Error: Missing required fields');
      return res.status(400).json({ error: 'Missing required fields' });
    }
  
    try {
      const query = 'INSERT INTO albums (title, artist, album_cover_url, rating) VALUES ($1, $2, $3, $4)';
      const values = [title, artist, album_cover_url, rating];
      
      // Debug: Log query and values
      console.log('Query:', query);
      console.log('Values:', values);
  
      await pool.query(query, values);
      res.status(201).json({ message: 'Album saved successfully!' });
    } catch (err) {
      // Debug: Log database error
      console.error('Error saving album:', err.message);
      res.status(500).json({ error: 'Failed to save album' });
    }
  });

module.exports = router;
