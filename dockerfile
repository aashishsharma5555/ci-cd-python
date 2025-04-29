FROM python:3.10-slim

WORKDIR /app

COPY requirment.txt .

RUN pip install -r requirment.txt

COPY . .

CMD ["gunicorn","--bind", "0.0.0.0:5000", "app.py"]
