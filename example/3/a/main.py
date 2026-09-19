from fastapi import FastAPI

app = FastAPI()


# The name comes from the URL itself — visiting /hello/Alice is
# different from visiting /hello/Bob. That's what "dynamic" means
# here: the response changes based on what's in the request.
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
