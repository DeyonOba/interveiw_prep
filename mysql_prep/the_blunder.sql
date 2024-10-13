
/*
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, 
but did not realize her keyboard's  key was broken until after completing the calculation.
She wants your help finding the difference between her miscalculation (using salaries with any zeros removed),
and the actual average salary.

Write a query calculating the amount of error (i.e.:`actual` - `miscalculation` average monthly salaries),
and round it up to the next integer.
*/

-- Convert the `Salary` column to a string datatype and apply the `REPLACE` function
-- in order to substitute each '0' character with an empty string '',
-- then convert the string datatype type back to an Integer using `UNSIGNED`

SELECT 
    CEIL(AVG(Salary) - AVG(CAST(REPLACE(CAST(Salary AS CHAR), '0', '') AS UNSIGNED)))
FROM EMPLOYEES;

-- MySQL CEILING function can also be used for returning the smallest integer not less than
-- the value given