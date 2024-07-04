-- Q1. Write a code to check NULL values
SELECT 
    COUNT(*) AS total_null_values
FROM 
    covid.`corona virus dataset`
WHERE 
    Province IS NULL 
    OR `Country/Region` IS NULL 
    OR Latitude IS NULL 
    OR Longitude IS NULL 
    OR Date IS NULL 
    OR Confirmed IS NULL 
    OR Deaths IS NULL 
    OR Recovered IS NULL;
    

-- Q2. If NULL values are present, update them with zeros for all columns. 
UPDATE 
    covid.`corona virus dataset`
SET 
    Province = COALESCE(Province, '0'),
    `Country/Region` = COALESCE(`Country/Region`, '0'),
    Latitude = COALESCE(Latitude, 0),
    Longitude = COALESCE(Longitude, 0),
    Date = COALESCE(Date, '0'),
    Confirmed = COALESCE(Confirmed, 0),
    Deaths = COALESCE(Deaths, 0),
    Recovered = COALESCE(Recovered, 0);

-- Q3. check total number of rows
SELECT 
    COUNT(*) AS total_rows
FROM 
    covid.`corona virus dataset`;

-- Q4. Check what is start_date and end_date
SELECT 
    MIN(Date) AS start_date,
    MAX(Date) AS end_date
FROM 
    covid.`corona virus dataset`;

-- Q5. Number of months present in dataset
SELECT 
    COUNT(DISTINCT DATE_FORMAT(STR_TO_DATE(Date, '%d-%m-%Y'), '%m')) AS num_months
FROM 
    covid.`corona virus dataset`;


-- Q6. Find monthly average for confirmed, deaths, recovered
SELECT 
    DATE_FORMAT(STR_TO_DATE(Date, '%d-%m-%Y'), '%m') AS month,
    AVG(Confirmed) AS avg_confirmed,
    AVG(Deaths) AS avg_deaths,
    AVG(Recovered) AS avg_recovered
FROM 
    covid.`corona virus dataset`
GROUP BY 
    month;


-- Q7. Find most frequent value for confirmed, deaths, recovered each month 
SELECT 
    DATE_FORMAT(STR_TO_DATE(Date, '%d-%m-%Y'), '%m') AS month,
    SUBSTRING_INDEX(GROUP_CONCAT(Confirmed ORDER BY Confirmed DESC), ',', 1) AS most_frequent_confirmed,
    SUBSTRING_INDEX(GROUP_CONCAT(Deaths ORDER BY Deaths DESC), ',', 1) AS most_frequent_deaths,
    SUBSTRING_INDEX(GROUP_CONCAT(Recovered ORDER BY Recovered DESC), ',', 1) AS most_frequent_recovered
FROM 
    covid.`corona virus dataset`
GROUP BY 
    month;


-- Q8. Find minimum values for confirmed, deaths, recovered per year
SELECT 
    YEAR(STR_TO_DATE(Date, '%d-%m-%Y')) AS year,
    MIN(Confirmed) AS min_confirmed,
    MIN(Deaths) AS min_deaths,
    MIN(Recovered) AS min_recovered
FROM 
    covid.`corona virus dataset`
GROUP BY 
    year;

-- Q9. Find maximum values of confirmed, deaths, recovered per year
SELECT 
    YEAR(STR_TO_DATE(Date, '%d-%m-%Y')) AS year,
    MAX(Confirmed) AS max_confirmed,
    MAX(Deaths) AS max_deaths,
    MAX(Recovered) AS max_recovered
FROM 
    covid.`corona virus dataset`
GROUP BY 
    year;


-- Q10. The total number of cases of confirmed, deaths, recovered each month
SELECT 
    DATE_FORMAT(STR_TO_DATE(Date, '%d-%m-%Y'), '%Y-%m') AS month,
    SUM(Confirmed) AS total_confirmed,
    SUM(Deaths) AS total_deaths,
    SUM(Recovered) AS total_recovered
FROM 
    covid.`corona virus dataset`
GROUP BY 
    month;


-- Q11. Check how corona virus spread out with respect to confirmed case
SELECT 
    SUM(Confirmed) AS total_confirmed,
    AVG(Confirmed) AS avg_confirmed,
    VARIANCE(Confirmed) AS variance_confirmed,
    STDDEV(Confirmed) AS stdev_confirmed
FROM 
    covid.`corona virus dataset`;

-- Q12. Check how corona virus spread out with respect to death case per month
SELECT 
    DATE_FORMAT(STR_TO_DATE(Date, '%d-%m-%Y'), '%m') AS month,
    SUM(Deaths) AS total_deaths,
    AVG(Deaths) AS avg_deaths,
    VARIANCE(Deaths) AS variance_deaths,
    STDDEV(Deaths) AS stdev_deaths
FROM 
    covid.`corona virus dataset`
GROUP BY 
    month;


-- Q13. Check how corona virus spread out with respect to recovered case per month
SELECT 
    DATE_FORMAT(STR_TO_DATE(Date, '%d-%m-%Y'), '%m') AS month,
    SUM(Recovered) AS total_recovered,
    round(AVG(Recovered)) AS avg_recovered,
    round(VARIANCE(Recovered)) AS variance_recovered,
    round(STDDEV(Recovered)) AS stdev_recovered
FROM 
    covid.`corona virus dataset`
GROUP BY 
    month;


-- Q14. Find Country having the highest number of confirmed cases
SELECT 
    `Country/Region`,
    MAX(Confirmed) AS highest_confirmed_cases
FROM 
    covid.`corona virus dataset`
GROUP BY 
    `Country/Region`
ORDER BY 
    highest_confirmed_cases DESC
LIMIT 1;

-- Q15. Find Country having the lowest number of death cases
SELECT 
    `Country/Region`,
    MIN(Deaths) AS lowest_death_cases
FROM 
    covid.`corona virus dataset`
GROUP BY 
    `Country/Region`
ORDER BY 
    lowest_death_cases ASC
LIMIT 1;

-- Q16. Find top 5 countries having the highest recovered cases
SELECT 
    `Country/Region`,
    SUM(Recovered) AS total_recovered_cases
FROM 
    covid.`corona virus dataset`
GROUP BY 
    `Country/Region`
ORDER BY 
    total_recovered_cases DESC
LIMIT 5;

 -- Q17. Countries have total number of confirmed cases
 SELECT 
    `Country/Region`,
    SUM(Confirmed) AS total_confirmed_cases
FROM 
    covid.`corona virus dataset`
GROUP BY 
    `Country/Region`
ORDER BY 
    total_confirmed_cases DESC

