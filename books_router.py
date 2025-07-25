from fastapi import APIRouter
import uuid

router = APIRouter()

@router.get("/books")
def read_book_by_year(year: int=None):
    if year:
        return{
            "year": year,
            "books": ["book1", "book2"]
        }
    return{
        "books": ["All books"]
    }

@router.get("/books/{book_id}")
def read_book(book_id: int):
    return {
        "job_id": uuid.uuid4(),
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }