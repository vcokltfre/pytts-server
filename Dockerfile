FROM python:3.8

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN apt update -y && apt upgrade -y

RUN apt install -y espeak ffmpeg

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5555"]