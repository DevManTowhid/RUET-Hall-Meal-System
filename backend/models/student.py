from pydantic import *  

class Student(BaseModel):
    id: int
    name: str
    hall: str
    department: str
    series: str
    email: str
    phone: str
    password: str
    degree: str
    

