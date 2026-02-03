import sqlite3
import pandas as pd

# Connect to SQLite database (FULL PATH is safest)
conn = sqlite3.connect(
    r"C:\Users\Poonakutty\OneDrive\Desktop\job_postings.db"
)

# 1️⃣ Job count by title
df_jobs = pd.read_sql("""
SELECT title, COUNT(*) AS job_count
FROM data_analyst_job_postings
GROUP BY title
ORDER BY job_count DESC
""", conn)

print("Top Job Titles:")
print(df_jobs.head(10))

df_jobs.to_csv("job_count_by_title.csv", index=False)


# 2️⃣ Average salary by location
df_salary = pd.read_sql("""
SELECT location, AVG(salary_standardized) AS avg_salary
FROM data_analyst_job_postings
WHERE salary_standardized IS NOT NULL
GROUP BY location
ORDER BY avg_salary DESC
LIMIT 10
""", conn)

print("\nAverage Salary by Location:")
print(df_salary)

df_salary.to_csv("avg_salary_by_location.csv", index=False)


# 3️⃣ Remote vs Onsite
df_remote = pd.read_sql("""
SELECT 
  CASE
    WHEN work_from_home IN ('TRUE', 'Remote', 'Yes') THEN 'Remote'
    WHEN work_from_home IN ('FALSE', 'Onsite', 'No') THEN 'Onsite'
    WHEN work_from_home = 'Hybrid' THEN 'Hybrid'
    ELSE 'Unknown'
  END AS work_type,
  COUNT(*) AS job_count
FROM data_analyst_job_postings
GROUP BY work_type
""", conn)

print("\nRemote vs Work Type:")
print(df_remote)

df_remote.to_csv("remote_vs_worktype.csv", index=False)

# 4️⃣ Job posting trend (hiring momentum)
df_trend = pd.read_sql("""
SELECT posted_at, COUNT(*) AS jobs_posted
FROM data_analyst_job_postings
GROUP BY posted_at
ORDER BY jobs_posted DESC
""", conn)

print("\nJob Posting Trend:")
print(df_trend.head(10))

df_trend.to_csv("job_posting_trend.csv", index=False)
