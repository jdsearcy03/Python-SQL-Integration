from sql_functions import *

password = input('Enter MySQL Password:\n')

#Connect SQL Server
connection = create_server_connection("localhost", "root", password)

#Create SQL Database
create_database_query = "CREATE DATABASE ServiceNow"
create_database(connection, create_database_query)

#Connect SQL Database
connection = create_db_connection("localhost", "root", password, "ServiceNow")

#Create Users Table
create_users_table = """
CREATE TABLE users (
    sys_id VARCHAR(60) PRIMARY KEY,
    user_name VARCHAR(60),
    first_name VARCHAR(60),
    last_name VARCHAR(60),
    email VARCHAR(60),
    department VARCHAR(60),
    location VARCHAR(60),
    vip BOOLEAN,
    street VARCHAR(60),
    city VARCHAR(40),
    zip INT,
    phone VARCHAR(20),
    gender VARCHAR(20),
    last_login DATE
    );
"""
execute_query(connection, create_users_table)

#Create Departments Table
create_departments_table = """
CREATE TABLE departments (
    sys_id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(40),
    description VARCHAR(40)
    );
"""
execute_query(connection, create_departments_table)

#Create Locations Table
create_locations_table = """
CREATE TABLE locations (
    sys_id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(80),
    street VARCHAR(60),
    city VARCHAR(40),
    zip INT,
    country VARCHAR(40)
    );
"""
execute_query(connection, create_locations_table)

#Create Incidents Table
create_incidents_table = """
CREATE TABLE incidents (
    sys_id VARCHAR(60) PRIMARY KEY,
    number VARCHAR(20),
    active BOOLEAN,
    priority INT,
    state INT,
    opened_at DATETIME,
    caller VARCHAR(60),
    assignment_group VARCHAR(60),
    assigned_to VARCHAR(60),
    resolved_by VARCHAR(60),
    resolved_at DATETIME
);
"""
execute_query(connection, create_incidents_table)

#Create User Groups Table
create_user_groups_table = """
CREATE TABLE user_groups (
    sys_id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(60),
    manager VARCHAR(60)
);
"""
execute_query(connection, create_user_groups_table)

#Add Foreign Keys to Users Table
alter_users = """
ALTER TABLE users
ADD FOREIGN KEY(department)
REFERENCES departments(sys_id)
ON DELETE SET NULL,
ADD FOREIGN KEY(location)
REFERENCES locations(sys_id)
ON DELETE SET NULL;
"""
execute_query(connection, alter_users)

#Add Foreign Keys to Incidents Table
alter_incidents = """
ALTER TABLE incidents
ADD FOREIGN KEY(assignment_group)
REFERENCES user_groups(sys_id)
ON DELETE SET NULL,
ADD FOREIGN KEY(assigned_to)
REFERENCES users(sys_id)
ON DELETE SET NULL,
ADD FOREIGN KEY(caller)
REFERENCES users(sys_id)
ON DELETE SET NULL,
ADD FOREIGN KEY(resolved_by)
REFERENCES users(sys_id)
ON DELETE SET NULL;
"""
execute_query(connection, alter_incidents)

#Add Foreign Keys to User Groups Table
alter_user_groups = """
ALTER TABLE user_groups
ADD FOREIGN KEY(manager)
REFERENCES users(sys_id)
ON DELETE SET NULL;
"""
execute_query(connection, alter_user_groups)