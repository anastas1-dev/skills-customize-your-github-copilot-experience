from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Create a FastAPI application
app = FastAPI(title="Task Management API")

# Pydantic models for data validation
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

# In-memory storage for tasks (for this assignment)
tasks_db: List[Task] = []
next_id = 1

# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint for the Task Management API"""
    return {"message": "Welcome to the Task Management API"}

# TODO: Implement GET /tasks endpoint
# Should return a list of all tasks

# TODO: Implement POST /tasks endpoint
# Should accept a TaskCreate model and add it to the tasks list

# TODO: Implement GET /tasks/{task_id} endpoint
# Should return a specific task by ID

# TODO: Implement PUT /tasks/{task_id} endpoint
# Should update a task's title and/or completed status

# TODO: Implement DELETE /tasks/{task_id} endpoint
# Should remove a task from the list

# To run this API, use:
# pip install fastapi uvicorn
# uvicorn starter_code:app --reload
