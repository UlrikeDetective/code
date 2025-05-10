CREATE TABLE music (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  artist VARCHAR(255) NOT NULL,
  album VARCHAR(255) NOT NULL,
  album_cover_url TEXT NOT NULL,
  rating INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Select * from music;

INSERT INTO music (title, artist, album, album_cover_url, rating)
VALUES ('Test Song', 'Test Artist', 'Test Album', 'https://via.placeholder.com/150', 5);

