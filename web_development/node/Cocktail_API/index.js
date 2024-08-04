const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', async (req, res) => {
  try {
    const response = await axios.get('https://www.thecocktaildb.com/api/json/v1/1/random.php');
    const cocktail = response.data.drinks[0];
    res.render('index', { cocktail });
  } catch (error) {
    console.error(error);
    res.send('Error retrieving data from API.');
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
