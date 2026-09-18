from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    return {"model_name": model_name}
