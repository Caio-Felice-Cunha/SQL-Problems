# Problem: Duplicate Job Listings
Easy | Linkedin<br>
<br>
Link: https://datalemur.com/questions/duplicate-job-listings <br>
<br>
This is the same question as problem #8 in the SQL Chapter of Ace the Data Science Interview!<br>
Assume you are given the table below that shows job postings for all companies on the LinkedIn platform. Write a query to get the number of companies that have posted duplicate job listings.<br>
Clarification:
* Duplicate job listings refer to two jobs at the same company with the same title and description.
![image](https://user-images.githubusercontent.com/111542025/233737069-3c7d06af-5841-4ff2-a2c2-071a8e91613b.png)<br>
![image](https://user-images.githubusercontent.com/111542025/233737092-77818ddc-15be-4dcb-bc6e-50baf794cb2a.png)

### Explanation
Because job IDs 945 and 164 are at the same company (345), and the jobs have the same title and description, there is exactly one company with a duplicate job.<br>
The dataset you are querying against may have different input & output - this is just an example!

# My Solution
Dialect: PostgreSQL.

A duplicate is two jobs at the same company sharing the same title and description, so the grouping key must be (company_id, title, description), not company_id alone. Grouping only by company_id would flag any company with two or more different postings.

````sql
WITH DuplicateCTE AS (
  SELECT
    company_id
  FROM
    job_listings
  GROUP BY
    company_id, title, description
  HAVING
    COUNT(*) > 1
)
SELECT
  COUNT(DISTINCT company_id) AS co_w_duplicate_jobs
FROM
  DuplicateCTE;
````
