from pydantic import BaseModel

class Address(BaseModel):
    country: str
    city: str

class socialDetails(BaseModel):
    type: str
    link: str

class StudentDetails(BaseModel):
    _id: str | None
    name: str
    email: str
    age: int
    address: Address
    phoneNum: list[int]
    socials: list[socialDetails]
