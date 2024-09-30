#!/usr/bin/env python3
"""
This Module explores relationships in SQL tables, these relationships
define how tables are connected to one another. Creating relationship among
tables provides efficient data retrieval and maintenance.


Source Article URL: https://www.geeksforgeeks.org/relationships-in-sql-one-to-one-one-to-many-many-to-many/
"""

import sqlite3

con = sqlite3.connect(":memory:")
curr = con.cursor()

def display_table(
    table_name: str,
    col_names: list[str],
    space: int=20
):
    """
    Displays an sqlite database table.
    
    Args:
        table_name (str): The name of the database table.
        col_names (list): A list of the defined column attribute names.
        space (int): Whitespace used to left adjust each entry.
    """    
    n = len(col_names)
    print()
    print(f"Table Name: {table_name}")
    print()
    def boarder_line(n: int=n):
        for idx in range(n):
            if idx == 0:
                print("+", "-"*space, sep="", end="")
            elif idx == n-1:
                print("+", "-"*space, "+", sep="", end="")
            else:
                print("+", "-"*space, sep="", end="")
        print()

    def display_data(obj):
        n = len(obj)
        for idx, data in enumerate(obj):
            if idx == 0:
                print("| ", str(data).ljust(space-1, " "), sep="", end="")
            elif idx == n-1:
                print("| ", str(data).ljust(space-1, " "), "|", sep="", end="")
            else:
                print("| ", str(data).ljust(space-1, " "), sep="", end="")
        print()
    
    boarder_line()
    display_data(col_names)
    boarder_line()
    for obj in curr.execute(f"SELECT * FROM {table_name};").fetchall():
        display_data(obj)
        boarder_line()
        
# SQL RELATIONSHIP: One to One relationship
table_1 = """
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(50)
);
"""

table_2 = """
CREATE TABLE users_profile (
    profile_id INT PRIMARY KEY,
    role VARCHAR(50),
    department VARCHAR(50),
    user_id INT UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(users_id)
)
"""
# Create the one to one relationship tables `users` and `users_profile`

curr.execute(table_1)
curr.execute(table_2)

# Insert data in to `users` and `users_profile` table
query_1 = """
INSERT INTO users
VALUES
    (1, 'ramesh'), (2, 'riya'), (3, 'akhil');
"""
query_2 = """
INSERT INTO users_profile
VALUES
    (1, "Jnr. Intern", "HR", 3),
    (2, "Jnr. Engr Intern", "Engr", 2),
    (3, "Jnr. Manager", "Admin", 1);
"""
curr.execute(query_1)
curr.execute(query_2)

print("\nSQL RELATIONSHIP: One to One Relationship")
display_table("users", ["user_id", "username"])
display_table("users_profile", ["profile_id", "role", "department", "users_id"])

# SQL RELATIONSHIP: One to many relationship
table_3 = """
CREATE TABLE departments (
    department_id  INT PRIMARY KEY,
    department_name VARCHAR(50)
);
"""

table_4 = """
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
"""
# Create the database table for department and employees
curr.execute(table_3)
curr.execute(table_4)

query_3 = """
INSERT INTO departments
VALUES
    (1, 'technical'), (2, 'accounts'), (3, 'pr'), (4, 'product management');
"""

query_4 = """
INSERT INTO employees
VALUES
    (1, 'Ramesh', 3), (2, 'Riya', 1),
    (3, 'Neha', 2), (4, 'Mayank', 1),
    (5, 'Kritila', 4), (6, 'Anuj', 4),
    (7, 'Sam', 1), (8, 'Gurpreet', 2)
"""
curr.execute(query_3)
curr.execute(query_4)

print("\nSQL RELATIONSHIP: One to Many Relationship")        
display_table("departments", ["department_id", "department_name"], 21)
display_table("employees", ["employee_id", "employee_name", "department_id"])

# SQL RELATIONSHIP: Many to many relationship
table_5 = """
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);
"""

table_6 = """
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
);
"""

table_7 = """
CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
"""

# Create tables `students` and `courses`
curr.execute(table_5)
curr.execute(table_6)
curr.execute(table_7)

# Add data to `students`, `courses`, and `student_courses` tables

query_5 = """
INSERT INTO students 
VALUES
    (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')
"""

query_6 = """
INSERT INTO courses
VALUES
    (101, "Mathematics"),
    (102, "History"),
    (103, "Computer Science")
"""

query_7 = """
INSERT INTO student_courses 
VALUES
    (1, 101),
    (1, 102),
    (2, 102)
"""
curr.execute(query_5)
curr.execute(query_6)
curr.execute(query_7)

print("\nSQL RELATIONSHIP: Many to Many Relationship")
display_table("students", ["student_id", "student_name"])
display_table("courses", ["course_id", "course_name"])
display_table("student_courses", ["student_id", "course_id"])

# SQL RELATIONSHIP: Self Referencing Relationship

table_8 = """
CREATE TABLE employeeManagement (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
"""

# Create table `employees`
curr.execute(table_8)

# Insert data into `employeeManagement`
query_8 = """
INSERT INTO employeeManagement
VALUES
    (1, 'Alice', Null),
    (2, 'Bob', 1),
    (3, 'Charlie', 1);
"""
curr.execute(query_8)

print("\nSQL RELATIONSHIP: Self Referencing")
display_table("employeeManagement", ["employee_id", "employee_name", "manager_id"])
