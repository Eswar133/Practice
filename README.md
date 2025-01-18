

## **Combined Oracle SQL and PL/SQL Syllabus**

---

### **Section 1: Introduction to Databases and SQL**

1. **Introduction to Databases**
   - What is a Database?
   - Understanding DBMS vs RDBMS
   - Overview of SQL and its Importance

2. **SQL Basics**
   - SQL Standards and Sublanguages (DDL, DML, DCL, TCL, DQL)
   - Differences between Oracle 10g, 11g, and 12c
   - Installation of Oracle 12c
   - Introduction to SQL*Plus and Oracle SQL Developer Tool

3. **Data Types and Operators**
   - Data Types in Oracle (VARCHAR2, NUMBER, DATE, CLOB, BLOB, etc.)
   - Operators in Oracle (Arithmetic, Comparison, Logical, etc.)

4. **Working with SQL Queries**
   - Using SELECT Statement to Retrieve Records
   - Working with Column and Table Aliases
   - Data Filtering and Sorting within a Single Table
   - Clauses in SQL:
     - WHERE Clause
     - HAVING Clause
     - GROUP BY Clause
     - ORDER BY Clause
     - USING Clause
     - FOR UPDATE Clause

5. **DDL Commands**
   - Table Creation using CREATE Statement
   - Creating Table from Another Table
   - Dropping a Table using DROP Command
   - Altering Table Columns (ADD, MODIFY, RENAME)
   - Using TRUNCATE Command
   - Difference between DELETE and TRUNCATE Commands

6. **DML Commands**
   - Inserting Rows into a Table
   - Updating Records using UPDATE Command
   - Deleting Records using DELETE Command
   - Copying Data and Structure from One Table to Another
   - Using MERGE and INSERT ALL Commands

7. **Constraints**
   - Column-Level and Row-Level Constraints
   - Types of Constraints:
     - NOT NULL
     - UNIQUE
     - PRIMARY KEY
     - FOREIGN KEY (Referential Integrity)
     - CHECK
   - Enabling and Disabling Constraints
   - Retrieving Information about Constraints

8. **Built-in Functions**
   - Single-Row Functions (Character, Number, Date, Conversion)
   - Aggregate Functions (COUNT, SUM, MAX, MIN, AVG)
   - Using GROUP BY and HAVING Clauses
   - Difference between WHERE and HAVING Clauses

9. **Joins**
   - Importance of Joins
   - Types of Joins:
     - Equi Join
     - Non-Equi Join
     - Self Join
     - Outer Join (Left, Right, Full)
     - Cross Join

10. **Set Operators and Pseudo Columns**
    - Working with Set Operators (UNION, UNION ALL, INTERSECT, MINUS)
    - Using Pseudo Columns (ROWNUM, ROWID)

11. **Subqueries**
    - Importance of Subqueries
    - Types of Subqueries:
      - Single-Row Subqueries
      - Multi-Row Subqueries
      - Correlated Subqueries

12. **Database Transactions**
    - Understanding Transactions (COMMIT, ROLLBACK, SAVEPOINT)
    - ACID Properties of Transactions

---

### **Section 2: Introduction to PL/SQL**

1. **What is PL/SQL?**
   - Advantages of PL/SQL over SQL
   - PL/SQL Architecture
   - PL/SQL Block Structure (Declaration, Execution, Exception Handling)

2. **PL/SQL Basics**
   - PL/SQL Data Types (Scalar, Composite, Reference, LOB)
   - Variables and Constants
   - PL/SQL Operators
   - Comments in PL/SQL

3. **Control Structures**
   - Conditional Control:
     - IF-THEN, IF-THEN-ELSE, IF-THEN-ELSIF
     - CASE Statement
   - Iterative Control:
     - Basic LOOP
     - FOR LOOP
     - WHILE LOOP
   - Sequential Control:
     - GOTO Statement
     - NULL Statement

4. **PL/SQL Cursors**
   - Introduction to Cursors
   - Types of Cursors:
     - Implicit Cursors
     - Explicit Cursors
   - Cursor Attributes (%FOUND, %NOTFOUND, %ISOPEN, %ROWCOUNT)
   - Cursor FOR LOOP
   - Parameterized Cursors
   - REF Cursors

5. **Exception Handling**
   - What are Exceptions?
   - Types of Exceptions:
     - Predefined Exceptions
     - User-Defined Exceptions
   - Handling Exceptions (EXCEPTION Block)
   - RAISE_APPLICATION_ERROR
   - PRAGMA EXCEPTION_INIT

6. **PL/SQL Subprograms**
   - Procedures:
     - Creating Procedures
     - Passing Parameters (IN, OUT, IN OUT)
     - Dropping Procedures
   - Functions:
     - Creating Functions
     - Difference between Procedures and Functions
     - Dropping Functions

7. **PL/SQL Packages**
   - What are Packages?
   - Advantages of Packages
   - Package Specification and Body
   - Creating and Dropping Packages
   - Overloading in Packages

8. **PL/SQL Triggers**
   - What are Triggers?
   - Types of Triggers:
     - Row-Level Triggers
     - Statement-Level Triggers
     - BEFORE and AFTER Triggers
     - INSTEAD OF Triggers
   - Creating and Dropping Triggers
   - Trigger Execution Order

9. **PL/SQL Collections**
   - What are Collections?
   - Types of Collections:
     - Associative Arrays (INDEX BY Tables)
     - Nested Tables
     - VARRAYs (Variable-Size Arrays)
   - Methods for Collections (COUNT, DELETE, EXISTS, etc.)

10. **Dynamic SQL in PL/SQL**
    - What is Dynamic SQL?
    - EXECUTE IMMEDIATE Statement
    - DBMS_SQL Package

11. **Advanced PL/SQL Concepts**
    - Bulk Processing (BULK COLLECT, FORALL)
    - Autonomous Transactions
    - PL/SQL Wrapper (Encrypting PL/SQL Code)

---

### **Section 3: Integration of SQL and PL/SQL**

1. **Using SQL in PL/SQL**
   - Embedding SQL Statements in PL/SQL Blocks
   - Using SELECT, INSERT, UPDATE, DELETE in PL/SQL
   - Transaction Control in PL/SQL (COMMIT, ROLLBACK, SAVEPOINT)

2. **PL/SQL and Database Interaction**
   - Using Cursors for Data Retrieval
   - Using Procedures and Functions for Data Manipulation
   - Using Triggers for Automated Actions

---

### **Section 4: Practical Exercises and Projects**

1. **Hands-On Practice**
   - Write SQL queries for data retrieval and manipulation.
   - Write PL/SQL blocks for real-world scenarios (e.g., payroll processing, inventory management).
   - Create stored procedures, functions, and triggers.

2. **Mini Projects**
   - Design a database system (e.g., library, e-commerce) and implement it using SQL and PL/SQL.
   - Create a package for a specific business logic (e.g., employee management).

3. **Debugging and Optimization**
   - Debug SQL and PL/SQL code using Oracle SQL Developer.
   - Optimize SQL queries and PL/SQL code for better performance.

---

### **Section 5: Additional Topics (Optional)**

1. **Database Security**
   - User Management
   - Roles and Privileges
   - Auditing

2. **Performance Tuning**
   - SQL Tuning (Indexes, Execution Plans)
   - PL/SQL Tuning (Bulk Processing, Profiling)

3. **Advanced SQL Features**
   - Analytic Functions (ROW_NUMBER, RANK, DENSE_RANK)
   - Hierarchical Queries (CONNECT BY, LEVEL)
   - Flashback Queries

