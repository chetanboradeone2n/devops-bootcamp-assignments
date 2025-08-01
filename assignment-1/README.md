# Assignment 1 - Simple REST API Webserver

This project is a RESTful API built using **Python** and **Flask**. It performs basic **CRUD operations** on an in-memory list of students.

> **C** = Create   |   **R** = Read   |   **U** = Update   |   **D** = Delete

---

## ✨ Features

- **GET** `/students` - Fetch all students  
- **POST** `/students` - Add a new student  
- **PUT** `/students/<id>` - Update a student by ID  
- **DELETE** `/students/<id>` - Delete a student by ID  
- **GET** `/api/v1/healthcheck` - Check if the server is running  

---

## ⚙️ Setup Instructions

### Step 1 - Clone the Repository

```bash
git clone https://github.com/chetanboradeone2n/rest_api_webserver.git
cd rest_api_webserver
```

### Step 2 - Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3 - Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 - Run the Application

```bash
python3 app.py
```

> The server will start at: `http://127.0.0.1:5000`

---

## 🧪 Example API Requests

### ✅ Healthcheck

```http
GET /api/v1/healthcheck
```

**Response:**

```json
{
  "status": "ok"
}
```

---

### ➕ Add a Student

```http
POST /students
```

**Body:**

```json
{
  "name": "John",
  "email": "john@example.com",
  "age": 21
}
```

---

### ✏️ Update a Student

```http
PUT /students/1
```

**Body:**

```json
{
  "name": "Johnny",
  "email": "johnny@example.com",
  "age": 22
}
```

---

### ❌ Delete a Student

```http
DELETE /students/1
```

---

## 📁 Project Structure

```
rest_api_webserver/
├── app.py
├── requirements.txt
└── README.md
```

---

## 👤 Author

**Chetan Borade**  
GitHub: [@chetanboradeone2n](https://github.com/chetanboradeone2n)

