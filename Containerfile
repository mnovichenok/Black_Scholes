from quay.io/lib/python

COPY requirements.txt requirements.txt
COPY black_scholes.py black_scholes.py
COPY fastapi_app.py fastapi_app.py

RUN pip install -r requirements.txt --no-cache-dir

# Launch
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0"]
