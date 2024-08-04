const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Set up EJS as the templating engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to handle the homepage
app.get('/', async (req, res) => {
  try {
    // Fetch a random cocktail
    const response = await axios.get('https://www.thecocktaildb.com/api/json/v1/1/random.php');
    
    // Check if the response has the expected structure
    if (!response.data || !response.data.drinks || response.data.drinks.length === 0) {
      throw new Error('No data found');
    }

    // Extract the cocktail data
    const cocktail = response.data.drinks[0];
    
    // Render the 'index.ejs' template with the cocktail data
    res.render('index', { cocktail });
  } catch (error) {
    // Log detailed error information
    console.error('Error fetching data from API:', error.message);
    console.error('Error details:', error.response ? error.response.data : error.message);
    
    // Send a user-friendly error message
    res.send('Error retrieving data from API.');
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
