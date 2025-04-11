from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel


class NewBook(BaseModel):
    title: str
    author: str


app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Асинхронность в Python",
        "author": "Matthew",
    },
    {
        "id": 2,
        "title": "Backend разработка в Python",
        "author": "Артем",
    }
]


@app.get('/books/',
         tags=['books'],
         summary='list all books')
def read_books():
    return books


@app.get('/books/{book_id}',
         tags=['books'],
         summary='get book by id')
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(404, detail='book didnt find')


@app.post('/books/create', tags=['books'])
def create_book(new_book: NewBook):
    books.append(
        {
            "id": len(books) + 1,
            "title": new_book.title,
            "author": new_book.author
        }
    )
    return {'success': True, 'message': f'book {books[-1]} created'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
