from fastapi import FastAPI
from app.endpoints_calculator import router  # Ajusta el nombre

app = FastAPI()
app.include_router(router)