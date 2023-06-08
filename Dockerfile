FROM python:3.8.5

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY model_gum_v2.h5 model_gum_v2.h5

COPY server.py server.py

ENV PYTHONUNBUFFERED=1 

ENV HOST 0.0.0.0

EXPOSE 3001

CMD [ "python", "server.py" ]