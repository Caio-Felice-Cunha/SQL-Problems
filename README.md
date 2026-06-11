# SQL Problems

A portfolio of solved SQL interview and practice problems from DataLemur, HackerRank, and StrataScratch. Each folder holds the problem statement (with the original schema and expected-output screenshots) and my solution, so the repo doubles as a reference for common patterns: window functions, self-joins, pivots, gap-and-island date logic, and safe percentage math.

The solutions target the dialect of the platform that hosts the problem. DataLemur and StrataScratch (code_type=3) run PostgreSQL, so those solutions assume Postgres semantics (integer division, EXTRACT, single-quoted strings). HackerRank problems that use idioms like `if()` or `REPLACE(x, '0', '')` are MySQL. ANSI-standard solutions (plain aggregates) run on either. Each non-trivial solution now carries a one-line dialect tag in its header.

## How to read this repo

1. Open any problem folder.
2. `Problem*.md` has the prompt, the source link, and the schema/example screenshots.
3. The solution is either inside that same markdown file under "My Solution" or in a sibling `Solution - Code.sql` file.

There is nothing to install or run locally. The queries execute against datasets hosted on each platform (DataLemur, HackerRank, StrataScratch). To try one, open its source link and paste the solution into that platform's editor.

## Index

### DataLemur (PostgreSQL)

| Problem | Difficulty | Company |
| --- | --- | --- |
| [App Click-through Rate (CTR)](./DataLemur%20-%20App%20Click-through%20Rate%20%28CTR%29%20%5BFacebook%20SQL%20Interview%20Question%5D/Problem%20and%20Solution.md) | Easy | Facebook |
| [Average Post Hiatus (Part 1)](./DataLemur%20-%20Average%20Post%20Hiatus%20%28Part%201%29%20%5BFacebook%20SQL%20Interview%20Question%5D/Problem%20and%20Solution.md) | Easy | Facebook |
| [Cards Issued Difference](./DataLemur%20-%20Cards%20Issued%20Difference%20%5BJPMorgan%20Chase%20SQL%20Interview%20Question%5D/Problem%20and%20Solution.md) | Easy | JPMorgan Chase |
| [Duplicate Job Listings](./DataLemur%20-%20Duplicate%20Job%20Listings/Problem%20and%20Solution.md) | Easy | LinkedIn |
| [Histogram of Tweets](./Datalemur%20-%20Histogram%20of%20Tweets/Problem.md) | Medium | Twitter |
| [Second Day Confirmation](./DataLemur%20-%20Second%20Day%20Confirmation%20%5BTikTok%20SQL%20Interview%20Question%5D/Problem%20and%20Solution.md) | Easy | TikTok |
| [Teams Power Users](./DataLemur%20-%20Teams%20Power%20Users%20%5BMicrosoft%20SQL%20Interview%20Question%5D/Problem%20and%20Solution.md) | Easy | Microsoft |

### HackerRank (MySQL / ANSI)

| Problem | Difficulty | Topic |
| --- | --- | --- |
| [Population Density Difference](./HackerRank%20-%20Population%20Density%20Difference/Problem%20and%20Solution.md) | Easy | Aggregation |
| [The Blunder](./HackerRank%20-%20The%20Blunder/Problem%20and%20Solution.md) | Easy | Aggregation |
| [Japan Population](./HackerRank%20-%20japan%20population/Problem%20and%20Solution.md) | Easy | Aggregation |
| [The Company](./HackerRank%20-%20the%20company/Problem%20and%20Answer.md) | Medium | Joins |
| [Occupations](./Hackerrank%20-%20occupations/Problem.md) | Medium | Pivot |

### StrataScratch (PostgreSQL, code_type=3)

| Problem | Difficulty | Company |
| --- | --- | --- |
| [Bikes Last Used](./StrataScratch%20-%20Bikes%20Last%20Used/Problem%20and%20Solution.md) | Easy | Lyft / DoorDash |
| [Count Abigail Breslin Oscar Nominations](./StrataScratch%20-%20Count%20the%20number%20of%20movies%20that%20Abigail%20Breslin%20nominated%20for%20oscar/Problem%20and%20Solution.md) | Easy | Google / Netflix |
| [Posts Reacted To With a Heart](./StrataScratch%20-%20Find%20all%20posts%20which%20were%20reacted%20to%20with%20a%20heart/Problem%20and%20Solution.md) | Easy | Meta/Facebook |
| [Matching Hosts and Guests](./StrataScratch%20-%20Find%20matching%20hosts%20and%20guests%20in%20a%20way%20that%20they%20are%20both%20of%20the%20same%20gender%20and%20nationality/Problem%20and%20Solution.md) | Medium | Airbnb |
| [Number Of Units Per Nationality](./StrataScratch%20-%20Number%20Of%20Units%20Per%20Nationality/Problem%20and%20Solution.md) | Medium | Airbnb |
| [Popularity Percentage](./StrataScratch%20-%20Popularity%20Percentage/Problem.md) | Hard | Meta/Facebook |
| [Ranking Most Active Guests](./StrataScratch%20-%20Ranking%20Most%20Active%20Guests/Problem%20and%20Solution.md) | Medium | Airbnb |

## License

[MIT](./LICENSE)
