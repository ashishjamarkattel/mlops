# app/api.py
from fastapi import FastAPI
import uvicorn

# Define application
app = FastAPI(
    title="TagIfAI - Made With ML",
    description="Classify machine learning projects.",
    version="0.1",
)

# app/api.py
from http import HTTPStatus
from typing import Dict

@app.get("/")
def _index() -> Dict:
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response


if __name__ == "__main__":
    uvicorn.run(app, port= 8000, host = "0.0.0.0")