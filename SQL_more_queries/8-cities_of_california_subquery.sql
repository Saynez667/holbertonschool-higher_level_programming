-- This scripts lists all the cities of the state of California using the database hbtn_0d_usa
SELECT id, name

-- for select all cities
FROM cities
 
-- for select all cities of California
WHERE state_id = (SELECT id FROM states WHERE name = 'California');

-- for order by ascending
ORDER BY id ASC;
