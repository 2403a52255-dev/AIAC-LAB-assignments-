-- ======================================================
-- SAFE RESET (CLEAN START)
-- ======================================================
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS staff_backup;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS emp;
DROP TABLE IF EXISTS department;

-- Make sure view is dropped using correct syntax
DROP VIEW IF EXISTS high_salary_employees;

SET FOREIGN_KEY_CHECKS = 1;

-- ======================================================
-- CREATE TABLES
-- ======================================================
CREATE TABLE department (
    dep_id INT PRIMARY KEY,
    dep_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

CREATE TABLE emp (
    empid INT PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    department_id INT,
    salary DECIMAL(10,2),
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES department(dep_id)
);

-- ======================================================
-- INSERT SAMPLE DATA
-- ======================================================
INSERT INTO department (dep_id, dep_name, location) VALUES
    (1, 'Engineering', 'New York'),
    (2, 'Sales', 'Chicago'),
    (3, 'HR', 'San Francisco'),
    (4, 'IT', 'Los Angeles'),
    (5, 'Marketing', 'Bangalore');

INSERT INTO emp (empid, firstname, lastname, department_id, salary, hire_date) VALUES
    (101, 'Alice', 'Smith', 1, 85000.00, '2020-06-15'),
    (102, 'Bob', 'Jones', 2, 65000.00, '2019-03-01'),
    (103, 'Carol', 'Lee', 1, 92000.00, '2021-11-12'),
    (104, 'David', 'Brown', 4, 72000.00, '2022-02-18'),
    (105, 'Eva', 'Clark', 3, 48000.00, '2023-07-25'),
    (106, 'Ravi', 'Kumar', 2, 55000.00, '2021-04-20'),
    (107, 'Amit', 'Sharma', 4, 76000.00, '2023-01-05');

-- ======================================================
-- BASIC QUERIES (1-27)
-- ======================================================

-- 1. Employee names and departments
SELECT e.firstname, e.lastname, d.dep_name AS department
FROM emp e
JOIN department d ON e.department_id = d.dep_id;

-- 2. Unique department names
SELECT DISTINCT dep_name FROM department;

-- 3. Employees with salary > 50000
SELECT firstname, lastname, salary FROM emp WHERE salary > 50000;

-- 4. Employees in IT
SELECT e.firstname, e.lastname, d.dep_name
FROM emp e
JOIN department d ON e.department_id = d.dep_id
WHERE d.dep_name = 'IT';

-- 5. Employees hired after 2020
SELECT firstname, lastname, hire_date
FROM emp
WHERE hire_date > '2020-12-31';

-- 6. Employees by ascending salary
SELECT firstname, lastname, salary
FROM emp
ORDER BY salary ASC;

-- 8. Top 3 highest-paid employees
SELECT firstname, lastname, salary
FROM emp
ORDER BY salary DESC
LIMIT 3;

-- 9. Total employees
SELECT COUNT(*) AS total_employees FROM emp;

-- 10. Average salary
SELECT AVG(salary) AS average_salary FROM emp;

-- 11. Highest and lowest salary
SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary FROM emp;

-- 12. Total salary per department
SELECT d.dep_name, SUM(e.salary) AS total_salary
FROM emp e
JOIN department d ON e.department_id = d.dep_id
GROUP BY d.dep_name;

-- 13. Departments with more than one employee
SELECT d.dep_name, COUNT(e.empid) AS employee_count
FROM emp e
JOIN department d ON e.department_id = d.dep_id
GROUP BY d.dep_name
HAVING COUNT(e.empid) > 1;

-- 14. Average salary by department
SELECT d.dep_name, AVG(e.salary) AS avg_salary
FROM emp e
JOIN department d ON e.department_id = d.dep_id
GROUP BY d.dep_name;

-- 15. Count employees hired each year
SELECT YEAR(hire_date) AS hire_year, COUNT(*) AS total_hired
FROM emp
GROUP BY YEAR(hire_date)
ORDER BY hire_year;

-- 16. Employees with department locations
SELECT e.firstname, e.lastname, d.dep_name, d.location
FROM emp e
JOIN department d ON e.department_id = d.dep_id;

-- 17. Employees in Bangalore
SELECT e.firstname, e.lastname, d.dep_name, d.location
FROM emp e
JOIN department d ON e.department_id = d.dep_id
WHERE d.location = 'Bangalore';

-- 18. All employees (even without department)
SELECT e.firstname, e.lastname, d.dep_name
FROM emp e
LEFT JOIN department d ON e.department_id = d.dep_id;

-- 19. Departments with no employees
SELECT d.dep_name
FROM department d
LEFT JOIN emp e ON e.department_id = d.dep_id
WHERE e.empid IS NULL;

-- 20. Count employees in each department
SELECT d.dep_name, COUNT(e.empid) AS employee_count
FROM department d
LEFT JOIN emp e ON e.department_id = d.dep_id
GROUP BY d.dep_name;

-- 21. Employees earning above average salary
SELECT firstname, lastname, salary
FROM emp
WHERE salary > (SELECT AVG(salary) FROM emp);

-- 22. Department with highest avg salary
SELECT d.dep_name, AVG(e.salary) AS avg_salary
FROM emp e
JOIN department d ON e.department_id = d.dep_id
GROUP BY d.dep_name
ORDER BY avg_salary DESC
LIMIT 1;

-- 23. Most recently hired employee
SELECT firstname, lastname, hire_date
FROM emp
ORDER BY hire_date DESC
LIMIT 1;

-- 24. Employees with 2nd highest salary
SELECT firstname, lastname, salary
FROM emp
WHERE salary = (
  SELECT MAX(salary)
  FROM emp
  WHERE salary < (SELECT MAX(salary) FROM emp)
);

-- 25. Employees in same department as 'Amit Sharma'
SELECT e2.firstname, e2.lastname
FROM emp e2
WHERE e2.department_id = (
  SELECT e1.department_id
  FROM emp e1
  WHERE e1.firstname = 'Amit' AND e1.lastname = 'Sharma'
);

-- 26. Increase IT salaries by 10%
UPDATE emp e
JOIN department d ON e.department_id = d.dep_id
SET e.salary = e.salary * 1.10
WHERE d.dep_name = 'IT';

-- 27. Change Ravi's department to Marketing
UPDATE emp e
JOIN department d ON d.dep_name = 'Marketing'
SET e.department_id = d.dep_id
WHERE e.firstname = 'Ravi';

-- ======================================================
-- ADDITIONAL QUERIES (28–50)
-- ======================================================

-- 28. Delete employees with salary < 40000
DELETE FROM emp WHERE salary < 40000;

-- 29. Add new column 'email' if it doesn't already exist (safe method)
-- Using INFORMATION_SCHEMA + prepared statement to be compatible across MySQL versions
SET @col_exists = (
  SELECT COUNT(*) 
  FROM INFORMATION_SCHEMA.COLUMNS 
  WHERE TABLE_SCHEMA = DATABASE() 
    AND TABLE_NAME = 'emp' 
    AND COLUMN_NAME = 'email'
);

SET @sql_stmt = IF(@col_exists = 0,
                   'ALTER TABLE emp ADD COLUMN email VARCHAR(100);',
                   'SELECT ''email column already exists'';'
                  );

PREPARE stmt FROM @sql_stmt;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- 30. Update emails (will update existing rows)
UPDATE emp
SET email = CONCAT(LOWER(firstname), '.', LOWER(lastname), '@company.com');

-- 31. Top 2 departments by avg salary
SELECT d.dep_name, AVG(e.salary) AS avg_salary
FROM emp e
JOIN department d ON e.department_id = d.dep_id
GROUP BY d.dep_name
ORDER BY avg_salary DESC
LIMIT 2;

-- 32. Employees per city
SELECT d.location AS city, COUNT(e.empid) AS total_employees
FROM department d
LEFT JOIN emp e ON e.department_id = d.dep_id
GROUP BY d.location;

-- 33. Employee count + total salary
SELECT d.dep_name, COUNT(e.empid) AS employee_count, SUM(e.salary) AS total_salary
FROM emp e
JOIN department d ON e.department_id = d.dep_id
GROUP BY d.dep_name;

-- 34. Names starting with 'A'
SELECT firstname, lastname FROM emp WHERE firstname LIKE 'A%';

-- 35. Last name ends with 'a'
SELECT firstname, lastname FROM emp WHERE lastname LIKE '%a';

-- 36. Employees hired in 2020
SELECT firstname, lastname, hire_date FROM emp WHERE YEAR(hire_date) = 2020;

-- 37. Days since hired
SELECT firstname, lastname, DATEDIFF(CURDATE(), hire_date) AS days_since_hired FROM emp;

-- 38. Names in uppercase
SELECT UPPER(firstname) AS first_upper, UPPER(lastname) AS last_upper FROM emp;

-- 39. Concatenate full name
SELECT CONCAT(firstname, ' ', lastname) AS full_name FROM emp;

-- 40. Salary between 45000 and 60000
SELECT firstname, lastname, salary FROM emp WHERE salary BETWEEN 45000 AND 60000;

-- 41. Create view for high salary (drop first to ensure compatibility)
DROP VIEW IF EXISTS high_salary_employees;
CREATE VIEW high_salary_employees AS
SELECT firstname, lastname, salary, department_id
FROM emp
WHERE salary > 55000;

-- 42. Display view records
SELECT * FROM high_salary_employees;

-- 43. Ensure department name NOT NULL (already declared as NOT NULL)
ALTER TABLE department MODIFY dep_name VARCHAR(100) NOT NULL;

-- 44. Drop the view (clean up)
DROP VIEW IF EXISTS high_salary_employees;

-- 45. Rename emp table to staff (safe because we dropped staff earlier if existed)
RENAME TABLE emp TO staff;

-- 46. Create backup of staff
CREATE TABLE staff_backup AS SELECT * FROM staff;

-- 47. Delete all data (keep structure)
DELETE FROM staff;

-- 48. Drop backup table
DROP TABLE IF EXISTS staff_backup;

-- 49. Create index on lastname
CREATE INDEX idx_lastname ON staff(lastname);

-- 50. Drop the index
DROP INDEX idx_lastname ON staff;

-- 51. Rename staff BACK to emp for next run
RENAME TABLE staff TO emp;

-- (OPTIONAL) Quick verification SELECT
SELECT * FROM emp LIMIT 5;
