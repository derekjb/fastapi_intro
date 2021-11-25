import os
os.add_dll_directory(r'C:\Users\Derek\anaconda3\Library\bin')

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    str = "message: Hello World"
    return {str}

@app.get("/items/")
async def get_item(item_id: int):
    item = item_id
    return  {item_id}