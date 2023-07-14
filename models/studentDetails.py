from pydantic import BaseModel

class Address(BaseModel):
    country: str
    city: str

class socialDetails(BaseModel):
    type: str
    link: str

class Book(BaseModel):
    name: str
    id: str

class StudentEntry(BaseModel):
    inTime: str
    outTime: str

class StudentDetails(BaseModel):
    _id: str | None
    name: str
    email: str
    age: int
    address: Address
    phoneNum: list[int]
    socials: list[socialDetails]
    books: list[Book]
    entry: list[StudentEntry]