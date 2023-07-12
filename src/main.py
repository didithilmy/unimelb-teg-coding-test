import os
from fastapi import FastAPI, UploadFile, Request, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from prediction import ModelPrediction

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), 'templates'))

@app.get("/")
def read_root(request: Request):
    predict_url = request.url_for('predict_input_file')
    return templates.TemplateResponse("index.html", {'request': request, 'predict_url': predict_url})

@app.post("/predict")
def predict_input_file(file: UploadFile):
    try:
        output = ModelPrediction().predict(file.file)
        response = StreamingResponse(iter([output.getvalue()]), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=output.csv"
        return response
    except:
        raise HTTPException(status_code=400, detail="Invalid input file")

