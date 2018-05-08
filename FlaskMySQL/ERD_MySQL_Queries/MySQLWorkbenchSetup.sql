USE twitter;

SELECT * FROM users;

SELECT * FROM users
WHERE id = 1 or id = 4;

SELECT * FROM users
ORDER BY birthday DESC;

UPDATE users SET
first_name = 'Cobe', last_name = 'BryBry'
WHERE id = 1;

SELECT * FROM users
WHERE id = 1;

SELECT CONCAT_WS(' ', 'Cool', 'guy', first_name, last_name) AS cool_guys 
FROM users;

