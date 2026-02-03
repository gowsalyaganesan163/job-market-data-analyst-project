-- =====================================
-- Job Market Analysis Queries
-- Table: data_analyst_job_postings
-- Database: job_postings.db
-- =====================================

-- 1. Job count by title
SELECT title, COUNT(*) AS job_count
FROM data_analyst_job_postings
GROUP BY title
ORDER BY job_count DESC;


-- 2. Average salary by location (Top 10)
SELECT location, AVG(salary_standardized) AS avg_salary
FROM data_analyst_job_postings
WHERE salary_standardized IS NOT NULL
GROUP BY location
ORDER BY avg_salary DESC
LIMIT 10;


-- 3. Jobs posted by date (table: data_analyst_job_postings)
SELECT posted_at, COUNT(*) AS jobs_posted
FROM data_analyst_job_postings
GROUP BY posted_at
ORDER BY jobs_posted DESC
LIMIT 10;


-- 4. Work type distribution (Remote / Onsite / Hybrid)
SELECT 
    CASE
        WHEN work_from_home IN ('TRUE', 'Remote', 'Yes') THEN 'Remote'
        WHEN work_from_home IN ('FALSE', 'Onsite', 'No') THEN 'Onsite'
        WHEN work_from_home = 'Hybrid' THEN 'Hybrid'
        ELSE 'Unknown'
    END AS work_type,
    COUNT(*) AS job_count
FROM data_analyst_job_postings
GROUP BY work_type;


-- 5. Jobs posted by Trend
SELECT posted_at, COUNT(*) AS jobs_posted
FROM data_analyst_job_postings
GROUP BY posted_at
ORDER BY jobs_posted DESC;
