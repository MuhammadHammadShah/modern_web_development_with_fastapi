from fastapi import FastAPI, Body, Header, Response

app = FastAPI()

# 1.


@app.get("/hi")
def greet():
    return "Hello? World?"

# 2.


@app.get("/hi/{who}")
def greet(who):
    return f"hello? {who}"

# 3.
# remove the who param from fastapi path functions


@app.get("/hii")
def greet1(who):
    return f"Hello? {who}"

# 4.
# use the path function with body


@app.post("/hiii")
def greet2(who1: str = Body(ambed=True)):
    return f" Hello? {who1}? "


@app.post("/hi1")
def greet3(who: str = Header()):
    return f" Hello? {who}? "


@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return {"user_agent": user_agent}


@app.get("/happy")
def happy(status_code=404):
    return ":)"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal header"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
