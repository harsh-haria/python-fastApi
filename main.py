from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from utility.config import conn
from bson import ObjectId

from models.studentDetails import StudentDetails

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.get('/fetchAll')
async def fetchAll():
    data = conn.LibraryManagementSystem.students.find({})
    studentData = []
    for item in data:
        item['_id'] = str(item['_id'])
        studentData.append(item)
    print(studentData)
    print(type(studentData))
    return studentData

@app.post('/insertStudent')
async def addStudent(student: StudentDetails):
    response = conn.LibraryManagementSystem.students.insert_one(student.dict())
    print(response)
    return {'message': 'Student added successfully!'}

@app.get('/fetchStudent/{id}')
async def fetchStudent(id: str):
    data = conn.LibraryManagementSystem.students.find_one({'_id': ObjectId(id)})
    data['_id'] = str(data['_id'])
    return data

@app.put('/updateStudent/{id}')
async def updateStudent(id: str, student: StudentDetails):
    response = conn.LibraryManagementSystem.students.update_one({'_id': ObjectId(id)}, {'$set': student.dict()})
    print(response)
    return {'message': f'Student {id} updated successfully!'}

@app.delete('/deleteStudent/{id}')
async def deleteStudent(id: str):
    response = conn.LibraryManagementSystem.students.delete_one({'_id': ObjectId(id)})
    print(response)
    return {'message': f'Student {id} deleted successfully!'}