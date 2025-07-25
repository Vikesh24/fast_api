from fastapi import APIRouter

router = APIRouter()

@router.get("/author/{author_id}")
def read_author(author_id: int):
    return {
        "author_id": author_id,
        "name": "Ernest Hemingway"
    }