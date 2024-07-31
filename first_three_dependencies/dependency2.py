from fastapi import FastAPI, Depends, Query


# function to become a dependency
def func_to_become_dependency(name: str = Query(...), password: str = Query(...)):
    return {
        "name": name,
        "valid": True
    }


app = FastAPI()


@app.get("/getdependsfunc")
def read_root(user: dict = Depends(func_to_become_dependency)) -> dict:
    return user
