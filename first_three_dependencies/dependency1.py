from fastapi import FastAPI, Depends


def func1():
    print("I am from function 1")


def func2():
    print("I am from function 2")


app = FastAPI(dependencies=[Depends(func1), Depends(func2)])


@app.get("/getfuncs")
def get_functions():
    return {"message": "Hello, World!"}  # Return a JSON response
