-- This command lists all records of the table second_table, displaying score and name, ordered by score (top first)
-- It excludes rows where the name column does not contain a value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
