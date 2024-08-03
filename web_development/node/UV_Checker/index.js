require('dotenv').config();
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;

// Your other code...


// Set EJS as the templating engine
app.set('view engine', 'ejs');
app.use(express.static('public'));

// Define the root route
app.get('/', async (req, res) => {
    let location = req.query.location || 'New York'; // default location
    let latitude = 40.7128; // Replace with actual latitude
    let longitude = -74.0060; // Replace with actual longitude

    try {
        const response = await axios.get(`https://api.openuv.io/api/v1/uv?lat=${latitude}&lng=${longitude}`, {
            headers: {
                'x-access-token': process.env.OPENUV_API_KEY
            }
        });

        const uvData = {
            location: location,
            uvIndex: response.data.result.uv
        };
        res.render('index', { uvData: uvData, error: null });
    } catch (error) {
        res.render('index', { uvData: null, error: 'Error fetching UV data' });
    }
});


app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
