from fastapi import APIRouter
from pydantic import BaseModel
from app.calculator import sum, resta, multiply

router = APIRouter()

class Numbers(BaseModel):
    a: int
    b: int

@router.post("/sum")
def sum_endpoint(numbers: Numbers) -> int:
    return sum(numbers.a, numbers.b)

@router.post("/resta")
def resta_endpoint(numbers: Numbers) -> int:
    return resta(numbers.a, numbers.b)

@router.post("/multiply")
def multiply_endpoint(numbers: Numbers) -> int:
    return multiply(numbers.a, numbers.b)