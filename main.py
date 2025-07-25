from fastapi import FastAPI
import uvicorn

from books_router import router as books_router
from authors_router import router as authors_router

app = FastAPI()
app.include_router(books_router)
app.include_router(authors_router)

@app.get("/")
def welcome():
    return "Welcome to the world of FastAPI mamey"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=3000)