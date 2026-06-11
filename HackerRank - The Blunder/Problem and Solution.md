# Problem: The Blunder
Easy | Aggregation<br>
Link: https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
<br>

Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.<br>

Write a query calculating the amount of error (i.e.:  actual - miscalculated average monthly salaries), and round it up to the next integer.<br>

Employees table:<br>
![image](https://user-images.githubusercontent.com/111542025/236263856-a1a48892-bf28-4c8b-9e97-d51a4b7186db.png)
![image](https://user-images.githubusercontent.com/111542025/236263900-55ffd9c6-5a4f-4189-8e94-5ba688cd4b46.png)

# My Solution
Dialect: MySQL.

The task asks for the error "rounded up to the next integer", which is CEIL applied to the difference of the two averages, not each average rounded separately and then subtracted. Rounding each term first can produce a different result (for example CEIL(33.33 - 0.67) = 33, but ROUND(33.33) - ROUND(0.67) = 32). The empty string for REPLACE uses single quotes so it works regardless of ANSI_QUOTES mode.

````sql
SELECT
    CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', ''))) AS error
FROM
    EMPLOYEES;
````
