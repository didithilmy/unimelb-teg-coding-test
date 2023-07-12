# Unimelb Transport Engineering Group - Coding Interview

Muhammad Aditya Hilmy <mhilmy@student.unimelb.edu.au>

## Task

Develop an API that allows user to provide an input file in the form of CSV.
The server program will use the input to create a prediction, and output the prediction as a CSV file.

## Trying the API

The server program is implemented using [FastAPI](https://github.com/tiangolo/fastapi). It exposes a REST API endpoint `/predict`.
The input of the endpoint is a CSV file, encoded with multipart form-data and the field name is `file`.

### Running with Docker

The easiest way to get started is by using Docker. Run the following command to test it out quickly.
```sh
docker run --rm -p 8000:80 didithilmy/unimelb-teg-coding-test
```

Once this is done, you can access [http://localhost:8000](http://localhost:8000).

### Installing dependencies
To install the dependencies, simply run:
```sh
pip install -r requirements.txt
```

### Running the server
To run the server, execute the following command:
```bash
bash run.sh
```

### Invoking the API

To test the API, you can use `curl` to make a request.

```sh
curl -F "file=@/path/to/input.csv" http://localhost:8000/predict
```

Alternatively, navigate to `http://localhost:8000` and use the file uploader there.
