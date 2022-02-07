from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from model_loader import ModelLoader

app = FastAPI(title="CLASSIFICATION service example",
              version="0.0.1",
              description="An app to classify text using SciKitLearn")

model_loader = ModelLoader()


class Classification_Request(BaseModel):
    text : str
    author : str

    class Config:
        schema_extra = {
            "example": {"text":"This is a movie description text about happy "
                               "things and people having fun and "
                               "sometimes crying.",
                        "author": "Some Author"}
        }

@app.get("/healthcheck")
def health():
    return {"Message": "All is Good"}


@app.get("/Models")
def list_models():
    model_names = list(model_loader.models.keys())
    model_names.sort()
    return {"Num_Models": len(model_names),
            "Model_Names": list(model_names)}


@app.post("/apply_model/{model_name}")
async def apply_model(req : Classification_Request,
                      model_name: str ):
    text = req.text
    author = req.author
    if not model_name in model_loader.models:
        raise HTTPException(status_code=404,
                            detail="Model Not Found")
    m = model_loader[model_name]
    r = m.classify(text)

    return {"text_length": len(text)+200,
            "text_class": r,
            "text_author": author}
