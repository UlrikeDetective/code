-- Migration to add hashtags column to books table
ALTER TABLE books ADD COLUMN hashtags TEXT;

-- Optional: Seed some initial hashtags for existing books
UPDATE books SET hashtags = '#surfing #waves #coast' WHERE title ILIKE '%surf%' AND hashtags IS NULL;
UPDATE books SET hashtags = '#cooking #recipes #food' WHERE (title ILIKE '%kitchen%' OR title ILIKE '%recipes%' OR title ILIKE '%cooking%') AND hashtags IS NULL;
UPDATE books SET hashtags = '#japan #culture #travel' WHERE (title ILIKE '%japan%' OR title ILIKE '%tokyo%' OR title ILIKE '%kyoto%') AND hashtags IS NULL;
UPDATE books SET hashtags = '#crime #thriller #mystery' WHERE title ILIKE '%crime%' AND hashtags IS NULL;
UPDATE books SET hashtags = '#fiction #modern' WHERE hashtags IS NULL;
