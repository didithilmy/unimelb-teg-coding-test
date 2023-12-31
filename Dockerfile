FROM python:3.9

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/app
COPY ./models /code/models
ENV MODEL_PATH /code/models/model.pickle
ENV PYTHONPATH=$PYTHONPATH:/code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
