# Popularity Percentage <br>
Interview Question Date: November 2020 | Meta/Facebook | Hard | ID 10284<br>
Data Engineer | Data Scientist | BI Analyst | Data Analyst<br>
Link: https://platform.stratascratch.com/coding/10284-popularity-percentage?code_type=3

## Problem
Find the popularity percentage for each user on Meta/Facebook. The popularity percentage is defined as the total number of friends the user has divided by the total number of users on the platform, then converted into a percentage by multiplying by 100.<br>
Output each user along with their popularity percentage. Order records in ascending order by user id.<br>
The 'user1' and 'user2' column are pairs of friends.<br>

### Hints
* You’ll need to create two subqueries or CTEs to calculate total unique friends-pair and total number of friend per user
* To calculate total unique friends-pair, UNION the user1 and user2 columns. This will de-duplicate any users that are repeated in the column. You can ensure uniqueness by adding a DISTINCT. To calculate the total count of unique friends-pair, perform a count(*) on the subquery.
* To calculate the total number of friends per user, create one column that contains all users and a second column that contains all their friends. You can accomplish this by user1, user2 UNION user2, user1.
* JOIN the two subqueries together so that you can calculate the percentage of friends over total users in the platform. You’ll need to JOIN using a 1=1 relation as the key. The resulting table will be a list of users, their friends, and total number of users on the platform.
* Lastly, implement the percentage popularity formula by counting the number of friends per user and dividing by the total number of users on the platform.

# [My Solution](./Solution%20-%20Code.sql)
