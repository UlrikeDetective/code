const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

const posts = [];

app.get('/', (req, res) => {
    res.render('index', { posts: posts });
});

app.get('/new-post', (req, res) => {
    res.render('new-post');
});

app.post('/new-post', (req, res) => {
    const post = { title: req.body.title, content: req.body.content };
    posts.push(post);
    res.redirect('/');
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
