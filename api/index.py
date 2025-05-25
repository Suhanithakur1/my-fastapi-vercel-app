from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from file
with open("marks.json", "r") as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_data.get(name, None) for name in names]
    return JSONResponse(content={"marks": result})
