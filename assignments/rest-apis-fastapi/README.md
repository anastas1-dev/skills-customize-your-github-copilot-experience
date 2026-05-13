# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build scalable REST APIs using the FastAPI framework. You'll create a simple API with multiple endpoints, handle different HTTP methods, and work with request/response models to build a real-world application.

## 📝 Tasks

### 🛠️ Create a Basic API with GET and POST Endpoints

#### Description
Build a simple task management API with endpoints to retrieve and create tasks. Start by setting up a FastAPI application and implementing basic CRUD operations.

#### Requirements
Completed program should:

- Create a FastAPI application with a root endpoint that returns a welcome message
- Implement a GET `/tasks` endpoint that returns a list of all tasks (initially empty)
- Implement a POST `/tasks` endpoint that accepts a task description and adds it to the list
- Each task should have an `id`, `title`, and `completed` status
- Example response for GET `/tasks`:
  ```json
  [
    {"id": 1, "title": "Learn FastAPI", "completed": false},
    {"id": 2, "title": "Build an API", "completed": false}
  ]
  ```

### 🛠️ Add Task Update and Delete Operations

#### Description
Extend the API with endpoints to update and delete individual tasks. This teaches how to handle path parameters and different HTTP methods.

#### Requirements
Completed program should:

- Implement a GET `/tasks/{task_id}` endpoint to retrieve a specific task by ID
- Implement a PUT `/tasks/{task_id}` endpoint to update a task's title or completed status
- Implement a DELETE `/tasks/{task_id}` endpoint to remove a task
- Return appropriate error responses (e.g., 404) when a task is not found
- Example usage:
  ```
  PUT /tasks/1
  {"title": "Advanced FastAPI", "completed": true}
  ```

### 🛠️ Use Pydantic Models for Data Validation

#### Description
Define Pydantic models to validate request and response data. This ensures data consistency and provides automatic API documentation.

#### Requirements
Completed program should:

- Create a Pydantic `Task` model with fields for `id`, `title`, and `completed`
- Create a `TaskCreate` model for request data (without the `id` field)
- Use these models in endpoint signatures for automatic validation and OpenAPI documentation
- FastAPI should automatically generate interactive documentation at `/docs`
- Invalid requests should return a 422 validation error
