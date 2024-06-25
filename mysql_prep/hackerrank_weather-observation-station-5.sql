-- Query the two cities in `STATION` with the shortest and longest `CITY` names, as well as their
-- respective lengths (i.e.: number of characters in the name). If there is more than one smallest
-- or largest city. Choose the one that comes first when ordered alphabetically. 

WITH t AS (
	    SELECT CITY, CHAR_LENGTH(CITY) AS char_length
	    FROM STATION
	    GROUP BY CITY
	    ORDER BY char_length, CITY
),
t2 AS (
	    SELECT MIN(CITY) AS city, char_length
	    FROM t
	    GROUP BY char_length
),
smallest_city AS(
	    SELECT city, char_length
	    FROM t2
	    ORDER BY char_length ASC
	    LIMIT 1
),
largest_city AS(
	    SELECT city, char_length
	    FROM t2
	    ORDER BY char_length DESC
	    LIMIT 1
)

SELECT * FROM smallest_city
UNION ALL
SELECT * FROM largest_city;

