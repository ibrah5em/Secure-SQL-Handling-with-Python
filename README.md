# 🔐 SQL Injection Prevention with Python + Flask

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask\&logoColor=black)
![SQL Server](https://img.shields.io/badge/Database-Microsoft_SQL_Server-red?logo=microsoftsqlserver\&logoColor=white)
![Security](https://img.shields.io/badge/SQL--Injection-Protected-green?logo=shield\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Working-brightgreen?style=flat-square)

💡 A beginner-friendly project to explore **backend development**, **database security**, and **SQL injection prevention** using Python and Flask.

---

## 📘 Introduction

When I first thought about `SQL`, the image that came to mind was a hacker injecting malicious queries into a website. My curiosity led me to learn about **SQL Injection**, how it works, and how to defend against it.

To explore this, I built a simple yet practical app with two goals:

1. ✅ Create a Python script to connect to a SQL Server database.
2. 🔐 Build a backend that filters and blocks SQL injection attempts.

Although I had only basic knowledge of relational databases, I saw this as a great opportunity to **go beyond the assignment** and learn something useful for real-world development.

---

## 🚀 Project Overview

In a web application:

* The **frontend** sends user inputs (e.g., login credentials).
* The **backend** processes requests and interacts with the **database**.
* If not secured, the backend becomes vulnerable to SQL injection.

> ✅ This project aims to **secure the backend** by validating input using **regular expressions**, preventing malicious SQL statements.

![Data Flowchart](https://github.com/user-attachments/assets/53081f06-c525-46d2-aaaa-38bb7a7b203d)

🧠 *Tip: In real-world applications, a dedicated **Secure API** can be used to filter malicious requests more effectively.*

---

## 🧱 Tech Stack

| Layer    | Technology                   |
| -------- | ---------------------------- |
| Frontend | HTML, CSS, JavaScript        |
| Backend  | Python, Flask                |
| Database | Microsoft SQL Server         |
| Security | Regex-based Input Validation |

---

## 🎨 Frontend Preview

A simple login form built using HTML, CSS, and JavaScript — no frameworks used.

![Login Form](https://github.com/user-attachments/assets/cb365b23-d3f0-4686-b34c-82b1605575a7)

📁 File Structure:

```
/Project-Files/
├── template/
├── static/
```

---

## 🗃️ Database Setup

Created using **Microsoft SQL Server**:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) NOT NULL,
    password NVARCHAR(50) NOT NULL
);

-- Insert example data
INSERT INTO users (username, password) VALUES ('admin', 'admin');
```

📌 *Database Name:* `myDB`

---

## 🔌 Backend Setup

### 📦 Installation

```bash
pip install pyodbc Flask
```

* `pyodbc`: For connecting to SQL Server
* `Flask`: Lightweight web framework

---

### 🛠️ Database Connection

```python
import pyodbc as odbc

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=X\SQLEXPRESS;'
    'DATABASE=myDB;'
    'Trusted_Connection=yes;'
)

conn = odbc.connect(conn_str)
```

📝 Replace `X\SQLEXPRESS` with your actual SQL Server name. Use:

```sql
SELECT @@SERVERNAME
```

---

### ⚙️ Flask App Example

```python
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the secure app!'

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🛡️ SQL Injection Prevention

Using **regular expressions** to validate user input:

```python
import re

if not re.match(r'^[a-zA-Z0-9_]+$', username):
    return 'Invalid username format'
if not re.match(r'^[a-zA-Z0-9_]+$', password):
    return 'Invalid password format'
```

✔️ Only allows alphanumeric characters and underscores
❌ Blocks characters like `'`, `;`, `--`, etc., which are often used in injection attempts

---

### 🧪 Regex Demo

```python
pattern = r'^[a-zA-Z0-9_]+$'
username = 'user123'

if re.match(pattern, username):
    print('✅ Valid username')
```

---

## 📂 Project Files

Project structure located in `/Project-Files`. Built with **Visual Studio Code**.

To start the server:

```bash
python app.py
```

### ✅ Output

```bash
* Running on http://127.0.0.1:5000/
* Debug mode: on
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔍 SQL Injection Testing

Tried a basic injection attempt on the login form:

![SQL Injection Attempt](https://github.com/user-attachments/assets/13eb80fa-0819-4443-a9d7-85c53e93ba7d)

**Result:** ✅ Rejected with `Invalid username format` — injection blocked!

---

## 💾 Bonus: Run SQL from File

Included a helper function to execute `.sql` files if needed:

```python
def execute_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql_commands = file.read().split(';')
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    for command in sql_commands:
        if command.strip():
            cursor.execute(command)
    conn.commit()
    cursor.close()
    conn.close()
```

Use this to auto-run `/SQL/create_tables.sql` (optional).

---

## 🧠 Lessons Learned

* ✔️ Connecting Python to SQL Server using `pyodbc`
* ✔️ Handling HTTP requests using `Flask`
* ✔️ Validating user input with regex
* ✔️ Preventing SQL Injection in simple web apps

---

## 📌 Final Notes

This was my **first backend project** combining Flask with a relational database. The app runs securely, blocks SQL injection, and reinforces backend fundamentals. I'm excited to continue building more secure apps and learning deeper concepts!

---

## 🙏 Acknowledgments

This project was completed as part of the *Information Security* course at Antioch Syrian University, under the guidance of **Ms. Nabiha Halak**.

Thank you for the valuable insights and support throughout the assignment.

