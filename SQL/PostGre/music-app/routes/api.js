const express = require('express');
const router = express.Router();
const axios = require('axios');

router.get('/search', async (req, res) => {
  const { query } = req.query;
  try {
    const response = await axios.get(`https://api.example.com/albums?q=${query}`, {
      headers: { Authorization: `Bearer ${process.env.API_KEY}` },
    });
    res.json(response.data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to fetch album covers' });
  }
});

module.exports = router;
