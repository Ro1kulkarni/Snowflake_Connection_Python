-- Create or replace a table named 'my_table' in the 'conn' schema of the 'rohan' database
-- The table contains two columns: 'YearsExperience' (float) and 'Salary' (integer)
CREATE OR REPLACE TABLE rohan.conn.my_table (
    YearsExperience FLOAT,
    Salary INT
);

-- Select all data from the 'my_table' to view its contents
SELECT * FROM rohan.conn.my_table;

-- Insert multiple rows of data into the 'my_table'
-- Adding records with YearsExperience and Salary values
INSERT INTO rohan.conn.my_table (YearsExperience, Salary) 
VALUES (1.2, 2000), (3.3, 4000);

-- Truncate (clear) all the data in 'my_table' without dropping the table itself
TRUNCATE rohan.conn.my_table;

-- Drop (delete) the 'my_table' entirely from the schema
DROP TABLE rohan.conn.my_table;

-- Display all tables within the current schema or the specified one
SHOW TABLES;

-- Display a list of all users in the Snowflake account
SHOW USERS;

-- Show all grants (permissions) assigned to the user 'ACME_ADMIN'
SHOW GRANTS TO USER ACME_ADMIN;

-- Show all roles available in the Snowflake account
SHOW ROLES;
