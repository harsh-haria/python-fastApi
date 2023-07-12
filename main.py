from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from utility.config import conn

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.get('/fetchAll')
async def fetchAll():
    data = conn.LibraryManagementSystem.students.find({}, {'_id': 0})
    studentData = []
    for item in data:
        studentData.append(item)
    print(studentData)
    print(type(studentData))
    return studentData