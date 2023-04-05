from typing import Union
import uvicorn
from fastapi import FastAPI
from route import routes
from fastapi.staticfiles import StaticFiles

tags_metadata = [
    {
        "name": "add",
        "description": "Used to add the address of the person ",
    },
    {
        "name": "address",
        "description": "give the address book",
        
    },
    {
        "name": "update",
        "description": "Used to update the address of the person",
    },
    {
        "name": "delete",
        "description": "Used to delete the address of the person",
    },
]


app =FastAPI(openapi_tags=tags_metadata)
app.include_router(routes)

import sys

if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0',port=8001)
