from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from db import ConnectDb

class MyPostData(BaseModel):
    name: str
    mean: str


app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

expressions_list = {}

with ConnectDb() as db:
    try:
        for expression in db.execute('SELECT * FROM expressions ORDER BY id ASC'):
            expressions_list[expression[2]] = {
                'id': expression[0], 
                'category_id': expression[1],
                'slug': expression[2],
                'jp': expression[3],
                'en': expression[4],
                'ru': expression[5]
                }

    except Exception as e:
        raise


@app.get("/")
async def index():
    return {"message": "hello world"}

@app.get("/expression/")
def read_expression(key: str):
    return expressions_list[key]

@app.get("/expressions/")
def read_all_expressions():
    return expressions_list


# @app.post("/data/")
# def update_data(post_data: MyPostData):
#     test_data[post_data.name] = post_data.mean
#     return {"message": "post success!!"}