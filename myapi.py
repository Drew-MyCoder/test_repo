from fastapi import FastAPI, Path
from typing import Annotated, Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 2"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

#create end-point(url)
@app.get("/")
def index():
    return{"name": "First Data"}
#to run,use the name of the file (uvicorn myapi:app --reload)

#we want to return student with a particular id
@app.get("/get-student/{student_id}")
def get_student(
    student_id: Annotated[int, Path(description="The ID of the student you want to view", gt=0)],):
    return students[student_id]

#query parameter we dont need to add the {}
@app.get("/get-student-name")
#putting an asterisk in the fuction ensures default or required arguments can be placed in no particular order
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


#we want to create a new student with post. student: Student (cap reps class)
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    
    students[student_id] = student
    return students[student_id]

#crud => post,get,put,del

#update user, first create a new class so user doesn't have to inherit from the student class(required compulsory update of all fields)
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

#to delete user
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message": "{student_id.name} deleted successfully"}