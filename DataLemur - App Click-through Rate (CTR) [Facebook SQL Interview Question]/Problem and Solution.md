# Problem: App Click-through Rate (CTR) [Facebook SQL Interview Question]
Easy | Facebook<br>
Link: https://datalemur.com/questions/click-through-rate<br>
<br>
This is the same question as problem #1 in the SQL Chapter of Ace the Data Science Interview!<br>

Assume you have an events table on Facebook app analytics. Write a query to calculate the click-through rate (CTR) for the app in 2022 and round the results to 2 decimal places.<br>

### Definition and note:
* Percentage of click-through rate (CTR) = 100.0 * Number of clicks / Number of impressions;
* To avoid integer division, multiply the CTR by 100.0, not 100.

### events Table:
![image](https://user-images.githubusercontent.com/111542025/234586803-e641b4a0-639d-417e-833a-7e8f47d90418.png)
![image](https://user-images.githubusercontent.com/111542025/234586873-533980a4-c179-4c72-8733-8c4a5748d6bb.png)
# My Solution:
Dialect: PostgreSQL.

Filtering by EXTRACT(YEAR FROM timestamp) = 2022 avoids two issues with the BETWEEN range. The literal '12/31/2022' is midnight on Dec 31, so a BETWEEN range would drop every event during that last day, and MM/DD/YYYY string literals depend on the session DateStyle setting.

````sql
SELECT
  app_id,
  ROUND(100.0 *
    COUNT(CASE
          WHEN event_type = 'click' THEN 1
            ELSE NULL END) /
    COUNT(CASE
          WHEN event_type = 'impression' THEN 1
            ELSE NULL END),2) AS ctr
FROM
  events
WHERE
  EXTRACT(YEAR FROM timestamp) = 2022
GROUP BY
  app_id;
````
