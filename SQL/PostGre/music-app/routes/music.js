const express = require('express');
const router = express.Router();
const db = require('../database');

// Middleware to parse JSON (move this to app.js if not already defined there)
router.use(express.json());

// Display saved songs
router.get('/', async (req, res) => {
  const { sort } = req.query;

  // Construct SQL query based on sort option
  let query = 'SELECT * FROM music';
  if (sort === 'recency') {
    query += ' ORDER BY created_at DESC';
  }

  try {
    const { rows } = await db.query(query);
    res.render('music', { music: rows });
  } catch (err) {
    console.error('Error fetching music:', err.message);
    res.status(500).send('Server error');
  }
});

// Add a new song
router.post('/add', async (req, res) => {
  console.log('Incoming request body:', req.body); // Log the incoming data

  const { title, artist, album, album_cover_url } = req.body;

  // Validate required fields
  if (!title || !artist || !album || !album_cover_url) {
    console.error('Missing required fields:', { title, artist, album, album_cover_url });
    return res.status(400).json({ error: 'All fields (title, artist, album, album_cover_url) are required.' });
  }

  try {
    // Insert song into the database
    await db.query(
      'INSERT INTO music (title, artist, album, album_cover_url) VALUES ($1, $2, $3, $4)',
      [title, artist, album, album_cover_url]
    );

    console.log('Music added to database:', { title, artist, album, album_cover_url });
    res.status(201).json({ message: 'Music added successfully' });
  } catch (err) {
    // Handle specific database errors
    if (err.code === '23505') {
      // Duplicate entry error (PostgreSQL error code)
      res.status(400).json({ error: 'Music already exists in the database.' });
    } else {
      console.error('Error adding music to database:', err.message);
      res.status(500).json({ error: 'Failed to add music.' });
    }
  }
});

module.exports = router;
