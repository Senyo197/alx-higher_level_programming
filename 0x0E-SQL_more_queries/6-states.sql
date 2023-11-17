-- Create the database hbtn_0d_usa if it doesn't exist
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;
-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT UNIQUE NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
