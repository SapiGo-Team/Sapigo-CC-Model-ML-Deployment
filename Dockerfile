FROM python:3.8.5

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1 

ENV HOST 0.0.0.0

EXPOSE 8000

CMD [ "python", "server.py" ]