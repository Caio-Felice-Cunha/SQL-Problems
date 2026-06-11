-- Problem: ../StrataScratch%20-%20Popularity%20Percentage/Problem.md
-- My Solution
-- Dialect: PostgreSQL (StrataScratch code_type=3).

WITH PairsUniqueCTE AS (
    SELECT 
        DISTINCT user1 AS UserId 
    FROM 
        facebook_friends
  UNION
    SELECT 
        DISTINCT user2 AS UserId 
    FROM 
        facebook_friends
),
CountFriendsCTE AS (
    SELECT 
        UserId,
        COUNT(*) AS TotalFriends
    FROM (
        SELECT user1 AS UserId FROM facebook_friends
    UNION ALL
        SELECT user2 AS UserId FROM facebook_friends) AS TotalUsers
    GROUP BY 
        UserId
)
SELECT
  PairsUniqueCTE.UserId,
  100.0 * CountFriendsCTE.TotalFriends
    / (SELECT COUNT(DISTINCT UserId) FROM PairsUniqueCTE) AS popularity_percent
FROM 
    PairsUniqueCTE
        LEFT JOIN 
    CountFriendsCTE USING(UserId)
ORDER BY  PairsUniqueCTE.UserId ASC;
