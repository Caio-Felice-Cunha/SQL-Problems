#!/usr/bin/env python3
"""Desk-check the four solutions that were corrected for logic or syntax.

These problems run against datasets hosted on DataLemur, HackerRank, and
StrataScratch, so the canonical answers cannot be reproduced here. What this
script does instead is build tiny in-memory tables that isolate the exact bug
each fix addresses, then assert that the corrected logic gives the right
answer while the original logic does not. It runs on the Python standard
library only (sqlite3), so:

    python tests/verify_fixed_solutions.py

Dialect note: sqlite3 is used as a portable harness. The PostgreSQL-specific
behaviour (integer division on bigint) is simulated explicitly with Python
integer math, because sqlite does floating-point division by default.
"""

import math
import sqlite3
import statistics
import sys


def section(title):
    print(f"\n== {title} ==")


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}")
    return condition


def test_duplicate_job_listings(con):
    section("Duplicate Job Listings (grouping key)")
    cur = con.cursor()
    cur.executescript(
        """
        DROP TABLE IF EXISTS job_listings;
        CREATE TABLE job_listings (job_id INT, company_id INT, title TEXT, description TEXT);
        -- company 345 has a real duplicate (same title AND description twice)
        INSERT INTO job_listings VALUES
          (945, 345, 'Data Analyst', 'Reviews data to identify insights'),
          (164, 345, 'Data Analyst', 'Reviews data to identify insights'),
        -- company 999 has TWO DIFFERENT postings, which is NOT a duplicate
          (300, 999, 'Role A', 'Desc A'),
          (301, 999, 'Role B', 'Desc B'),
        -- company 244 has a single posting
          (172, 244, 'Data Engineer', 'Builds pipelines');
        """
    )
    expected = 1  # only company 345

    old = """
        WITH DuplicateCTE AS (
          SELECT company_id, COUNT(title || ' ' || description) AS cnt
          FROM job_listings GROUP BY company_id)
        SELECT COUNT(DISTINCT company_id) FROM DuplicateCTE WHERE cnt >= 2;
    """
    new = """
        WITH DuplicateCTE AS (
          SELECT company_id FROM job_listings
          GROUP BY company_id, title, description HAVING COUNT(*) > 1)
        SELECT COUNT(DISTINCT company_id) FROM DuplicateCTE;
    """
    old_res = cur.execute(old).fetchone()[0]
    new_res = cur.execute(new).fetchone()[0]
    ok = True
    ok &= check(f"old grouping is wrong (returns {old_res}, not {expected})", old_res != expected)
    ok &= check(f"new grouping is correct (returns {expected})", new_res == expected)
    return ok


def test_the_blunder():
    section("The Blunder (CEIL of difference vs round-then-subtract)")
    # Crafted averages where the two formulas diverge.
    actual_avg, miscalc_avg = 33.33, 0.67
    canonical = math.ceil(actual_avg - miscalc_avg)        # CEIL(32.66) = 33
    round_then_subtract = round(actual_avg) - round(miscalc_avg)  # 33 - 1 = 32
    ok = True
    ok &= check(f"canonical CEIL(actual - miscalc) = {canonical}", canonical == 33)
    ok &= check(
        f"old round-each-then-subtract = {round_then_subtract} differs",
        round_then_subtract != canonical,
    )
    return ok


def test_popularity_percentage():
    section("Popularity Percentage (PostgreSQL integer division)")
    total_friends = 1   # a user with one friend
    total_users = 6     # six users on the platform
    # PostgreSQL bigint / bigint truncates toward zero before the * 100.
    old = (total_friends // total_users) * 100          # -> 0 for nearly everyone
    new = 100.0 * total_friends / total_users           # -> 16.666...
    ok = True
    ok &= check(f"old truncates to {old} (wrong)", old == 0)
    ok &= check(f"new = {new:.4f} (correct)", abs(new - 16.6667) < 1e-3)
    return ok


def test_occupations_pivot(con):
    section("Occupations (reserved-word alias + pivot shape)")
    cur = con.cursor()
    cur.executescript(
        """
        DROP TABLE IF EXISTS occupations;
        CREATE TABLE occupations(name TEXT, occupation TEXT);
        INSERT INTO occupations VALUES
          ('Samantha','Doctor'),('Julia','Actor'),('Maria','Actor'),
          ('Meera','Singer'),('Ashely','Professor'),('Ketty','Professor'),
          ('Christeen','Professor'),('Jane','Actor'),('Jenny','Doctor'),('Priya','Singer');
        """
    )
    # sqlite analog of the fixed query: CASE stands in for MySQL if(),
    # and the alias 'Ranked' (not the reserved word 'Order') must parse.
    rows = cur.execute(
        """
        SELECT
          MIN(CASE WHEN occupation='Doctor' THEN name END) AS Doctor,
          MIN(CASE WHEN occupation='Professor' THEN name END) AS Professor,
          MIN(CASE WHEN occupation='Singer' THEN name END) AS Singer,
          MIN(CASE WHEN occupation='Actor' THEN name END) AS Actor
        FROM (
          SELECT name, occupation,
                 ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS NumberRow
          FROM occupations) AS Ranked
        GROUP BY NumberRow;
        """
    ).fetchall()
    ok = True
    # First row should be the alphabetically-first name in each column.
    ok &= check("alias 'Ranked' parses and pivot returns rows", len(rows) == 3)
    ok &= check("first row holds the alphabetically-first names", rows[0] == ('Jenny', 'Ashely', 'Meera', 'Jane'))
    return ok


def main():
    con = sqlite3.connect(":memory:")
    results = [
        test_duplicate_job_listings(con),
        test_the_blunder(),
        test_popularity_percentage(),
        test_occupations_pivot(con),
    ]
    print()
    if all(results):
        print("All checks passed.")
        return 0
    print("Some checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
