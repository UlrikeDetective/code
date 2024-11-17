const express = require('express');
const router = express.Router();
const db = require('../database');

// Display saved songs
router.get('/', async (req, res) => {
  const { sort } = req.query;

  let query = 'SELECT * FROM music';
  if (sort === 'rating') {
    query += ' ORDER BY rating DESC';
  } else if (sort === 'recency') {
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
  const { title, artist, album, album_cover_url, rating } = req.body;

  if (!title || !artist || !album || !album_cover_url) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  try {
    await db.query(
      'INSERT INTO music (title, artist, album, album_cover_url, rating) VALUES ($1, $2, $3, $4, $5)',
      [title, artist, album, album_cover_url, rating]
    );
    res.status(201).json({ message: 'Music added successfully' });
  } catch (err) {
    console.error('Error adding music:', err.message);
    res.status(500).json({ error: 'Failed to add music.' });
  }
});

module.exports = router;
