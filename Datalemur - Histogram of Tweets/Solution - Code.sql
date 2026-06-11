-- Problem: ../Datalemur%20-%20Histogram%20of%20Tweets/Problem.md
-- My Solution
-- Dialect: PostgreSQL.
-- tweet_date is a timestamp, so EXTRACT(YEAR ...) keeps tweets posted after
-- midnight on Dec 31 2022 that a BETWEEN '2022-01-01' AND '2022-12-31' range drops.

WITH TweetsCountCTE AS(
  SELECT
    user_id,
    COUNT(tweet_id) AS NumberTweets
  FROM
    tweets
  WHERE
    EXTRACT(YEAR FROM tweet_date) = 2022
  GROUP BY
    user_id)
SELECT
  NumberTweets,
  COUNT(user_id) AS NumberUsers
FROM
  TweetsCountCTE
GROUP BY
  NumberTweets;
