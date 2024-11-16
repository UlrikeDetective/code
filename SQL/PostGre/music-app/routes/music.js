const express = require('express');
const router = express.Router();
const pool = require('../database');

// Get all music entries
router.get('/', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM music ORDER BY listened_at DESC');
    res.render('music', { music: result.rows });
  } catch (err) {
    console.error(err);
  }
});

// Add a new entry
router.post('/add', async (req, res) => {
  const { title, artist, album_cover_url, rating } = req.body;
  try {
    await pool.query('INSERT INTO music (title, artist, album_cover_url, rating) VALUES ($1, $2, $3, $4)', [title, artist, album_cover_url, rating]);
    res.redirect('/music');
  } catch (err) {
    console.error(err);
  }
});

// Update an entry
router.post('/update/:id', async (req, res) => {
  const { id } = req.params;
  const { rating } = req.body;
  try {
    await pool.query('UPDATE music SET rating = $1 WHERE id = $2', [rating, id]);
    res.redirect('/music');
  } catch (err) {
    console.error(err);
  }
});

// Delete an entry
router.post('/delete/:id', async (req, res) => {
  const { id } = req.params;
  try {
    await pool.query('DELETE FROM music WHERE id = $1', [id]);
    res.redirect('/music');
  } catch (err) {
    console.error(err);
  }
});

module.exports = router;
