# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. Students will create endpoints, handle requests, and return JSON responses, gaining practical experience with modern web development tools.

## 📝 Tasks

### 🛠️	Create a Simple FastAPI App

#### Description
Set up a basic FastAPI application with at least one endpoint that returns a JSON response.

#### Requirements
Completed program should:
- Import and initialize FastAPI
- Define a root endpoint (`/`) that returns a welcome message in JSON
- Run the app locally for testing

#### Example
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
```

### 🛠️	Add CRUD Endpoints

#### Description
Expand your FastAPI app to support basic CRUD (Create, Read, Update, Delete) operations for a resource (e.g., items, users).

#### Requirements
Completed program should:
- Define a resource model using Pydantic
- Implement endpoints for:
  - Creating a new resource (POST)
  - Reading all resources (GET)
  - Reading a single resource by ID (GET)
  - Updating a resource by ID (PUT)
  - Deleting a resource by ID (DELETE)
- Return appropriate JSON responses and status codes

#### Example
```python
# Example endpoints:
@app.post("/items/")
@app.get("/items/")
@app.get("/items/{item_id}")
@app.put("/items/{item_id}")
@app.delete("/items/{item_id}")
```

### 🛠️	API Documentation and Testing

#### Description
Explore FastAPI's automatic documentation and test your endpoints using the interactive Swagger UI.

#### Requirements
Completed program should:
- Access the docs at `/docs` in the browser
- Test all endpoints using the Swagger UI
- Ensure all endpoints work as expected
