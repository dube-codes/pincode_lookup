# Pincode Lookup API

A simple **FastAPI-based Pincode Lookup API** built as a learning project to practice REST API development, Pydantic validation, custom exception handling, and API response models.

The project currently uses hardcoded pincode data stored in `pincode_data.py` and does **not use a database**.

## 🚀 Features

- Get location details using a pincode
- Get details for multiple pincodes using a bulk API
- Request validation using Pydantic
- Custom exception handling
- Response models using Pydantic
- Hardcoded pincode data
- REST API development with FastAPI
- Interactive API documentation
- Run the application using Uvicorn

## 🛠️ Technologies Used

- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**

## 📁 Project Structure

```text
pincode-lookup/
│
├── venv/
├── __pycache__/
├── .gitignore
├── exceptions.py
├── main.py
├── models.py
├── pincode_data.py
├── requirements.txt
└── README.md
```

### File Overview

- `main.py` — FastAPI application and API endpoints
- `models.py` — Pydantic request and response models
- `exceptions.py` — Custom exceptions and exception handlers
- `pincode_data.py` — Hardcoded pincode data
- `requirements.txt` — Python project dependencies
- `README.md` — Project documentation

## 🔌 API Endpoints

### 1. Root Endpoint

```http
GET /
```

Returns a welcome message.

### 2. Lookup Pincode

```http
GET /pincode/{code}
```

Returns location information for a specific pincode.

Example:

```http
GET /pincode/110001
```

Example response:

```json
{
  "pincode": "110001",
  "city": "New Delhi",
  "state": "Delhi",
  "district": "Central Delhi"
}
```

The API validates that the pincode contains exactly **6 digits**. If the format is invalid, a custom `InvalidPinCodeError` is raised. If the pincode is not available in the dataset, a custom `PinCodeNotFound` exception is raised.

### 3. Bulk Pincode Lookup

```http
POST /pincode/bulk
```

This endpoint accepts multiple pincodes and returns the matching records along with a list of pincodes that were not found.

Example request:

```json
{
  "pincodes": ["110001", "400001", "560001"]
}
```

Example response structure:

```json
{
  "found": 2,
  "not_found": 1,
  "results": [],
  "missing": ["560001"]
}
```

## 🧩 Validation and Custom Exceptions

This project uses **Pydantic** models for request and response validation.

Custom exceptions are also implemented for application-specific errors:

- `InvalidPinCodeError`
- `PinCodeNotFound`

These exceptions are registered with FastAPI using custom exception handlers.

## 💾 Data Storage

This project **does not use a database**.

The pincode information is currently stored as hardcoded Python data in:

```text
pincode_data.py
```

For example:

```python
pincode_db = {
    "110001": {
        "pincode": "110001",
        "city": "New Delhi",
        "state": "Delhi",
        "district": "Central Delhi",
    }
}
```

This approach was used for learning and keeping the project simple.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/dube-codes/pincode_lookup.git
```

```bash
cd pincode_lookup
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI provides interactive API documentation automatically.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## 🎯 What I Learned

This project helped me practice:

- Building REST APIs with FastAPI
- Creating GET and POST endpoints
- Using Pydantic for data validation
- Creating request and response models
- Implementing custom exceptions
- Creating custom exception handlers
- Handling missing data
- Working with structured Python data
- Running FastAPI applications with Uvicorn
- Managing a Python project with Git and GitHub

## 🔮 Future Improvements

Possible improvements for future versions:

- Add a database such as PostgreSQL
- Replace hardcoded data with database queries
- Add SQLAlchemy
- Add automated tests
- Add authentication
- Add more pincode-related APIs

## 📌 Project Status

This is a **learning project** focused on practicing Python and FastAPI.

The current version uses hardcoded pincode data and does not use a database.
