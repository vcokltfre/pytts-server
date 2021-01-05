# vcokltfre/pytts-server

## A Python text-to-speech API made with FastAPI using pyttsx3

### Prerequisites:
- You must have `espeak` and `ffmpeg` installed
- You must have `docker` and `docker-compose` installed to use the docker-compose setup

### Running the server:
- Native host: `uvicorn main:app --host 0.0.0.0 --port 5555`
- Docker compose: `sudo docker-compose up -d`