import board_pb2
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

def newBoard():
    nb = board_pb2.Board()
    for _ in range(0,9):
        for _ in range(0,9):
            nb.squares.append("EMPTY")
    nb.squares[0] = 1
    nb.squares[1] = 2
    return nb

db = {
    "0": {
        "name" : "Root Game",
        "board" : newBoard()
    }
}

app = FastAPI()

@app.get("/board/{id}")
def html_board(request: Request, id: str):
    return templates.TemplateResponse("board.html.jinja", {"request": request, "id": id, "game" : db[id]})


@app.get("/")
def read_root():
    newGame = newBoard()
    return {"Hello": newGame.SerializeToString()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

