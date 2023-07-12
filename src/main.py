import os
from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from prediction import ModelPrediction

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), 'templates'))

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

@app.post("/predict")
def predict_input_file(file: UploadFile):
    output = ModelPrediction().predict(file.file)
    response = StreamingResponse(iter([output.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=output.csv"
    return response
