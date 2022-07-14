from re import I
from fastapi import FastAPI
from server.routes.student import router as StudentRouter


app = FastAPI()

app.include_router(StudentRouter,tags=["Student"],prefix="/student")

@app.get("/",tags=["Root"])
async def read_root():
    return {"message": "Hello world !"}


# @app.get("/student/",tags=["Student"])
# def student():
#     return {"get"}

# @app.post("/student/",tags=["Student"])
# def student_id():
#     return {"post"}


# @app.get("/student/{id}",tags=["Student"])
# def student_id():
#     return {"get_id"}

# @app.put("/student/{id}",tags=["Student"])
# def student_id():
#     return {"put_id"}

# @app.delete("/student/{id}",tags=["Student"])
# def student_id():
#     return {"delete_id"}



# @app.get("/",tags=["Root"])
# async def read_root():
#     return {"message": "welelllll"}