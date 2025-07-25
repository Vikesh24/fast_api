from fastapi import FastAPI
import uvicorn
import uuid

app = FastAPI()

@app.get("/books/{book_id}")
def read_root(book_id: int):
    return {
        "job_id": uuid.uuid4(),
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=3000)