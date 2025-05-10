import express from "express";
import bodyParser from "body-parser";
import mysql from "mysql2/promise"; // Using mysql2 with promises for async/await support

const db = mysql.createPool({
  host: "localhost",
  user: "root",
  database: "world",
  password: "Susilein",
  port: 3306, // Default MySQL port
});

const app = express();
const port = 3001;

let quiz = [];
let totalCorrect = 0;
let currentQuestion = {};

// Fetch data from MySQL
async function fetchData() {
  try {
    const [rows] = await db.query("SELECT * FROM capital");
    quiz = rows;
    console.log('Data fetched successfully:', quiz);
  } catch (err) {
    console.error("Error executing query", err);
    quiz = []; // Ensure quiz is an array
  }
}

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

// GET home page
app.get("/", async (req, res) => {
  try {
    totalCorrect = 0;
    await nextQuestion();
    console.log('Current question:', currentQuestion);
    res.render("index.ejs", { question: currentQuestion });
  } catch (err) {
    console.error("Error in GET / route", err);
    res.status(500).send("Server Error");
  }
});

// POST a new post
app.post("/submit", async (req, res) => {
  try {
    let answer = req.body.answer.trim();
    let isCorrect = false;
    if (currentQuestion.capital.toLowerCase() === answer.toLowerCase()) {
      totalCorrect++;
      console.log('Total correct:', totalCorrect);
      isCorrect = true;
    }

    await nextQuestion();
    res.render("index.ejs", {
      question: currentQuestion,
      wasCorrect: isCorrect,
      totalScore: totalCorrect,
    });
  } catch (err) {
    console.error("Error in POST /submit route", err);
    res.status(500).send("Server Error");
  }
});

async function nextQuestion() {
  if (quiz.length === 0) {
    await fetchData();
  }
  const randomCountry = quiz[Math.floor(Math.random() * quiz.length)];
  currentQuestion = randomCountry;
}

// Start the server and fetch the quiz data
app.listen(port, async () => {
  try {
    await fetchData();
    console.log(`Server is running at http://localhost:${port}`);
  } catch (err) {
    console.error("Error starting server", err);
  }
});
