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

@app.get("/")
async def index():
    return {"message": "hello world"}

@app.get("/expression/")
def read_expression(key: str):
    with ConnectDb() as db:
        try:
            cur = db.execute(f'SELECT * FROM expressions WHERE slug="{key}"').fetchone()
            expression = {
                'id': cur[0],
                'category_id': cur[1] ,
                'slug': cur[2],
                'jp': cur[3],
                'en': cur[4],
                'ru': cur[5]
                }

        except Exception as e:
            raise

    return expression

@app.get("/expressions/")
def read_all_expressions():
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

    return expressions_list

@app.get("/expressions-in-category")
def read_expressions_in_category(key: str):
    expressions_list = {}

    with ConnectDb() as db:
        try:
            for expression in db.execute(f'SELECT * FROM expressions WHERE category_id="{key}" ORDER BY id ASC'):
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

    return expressions_list



# @app.post("/data/")
# def update_data(post_data: MyPostData):
#     test_data[post_data.name] = post_data.mean
#     return {"message": "post success!!"}