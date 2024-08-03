const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.use(express.static('public'));

app.get('/', async (req, res) => {
    let location = req.query.location || 'New York'; // default location
    try {
        const response = await axios.get(`https://api.openuv.io/api/v1/uv?lat={latitude}&lng={longitude}`, {
            headers: {
                'x-access-token': 'YOUR_API_KEY'
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
