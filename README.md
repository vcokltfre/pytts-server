# vcokltfre/pytts-server

## A Python text-to-speech API made with FastAPI using pyttsx3

### Prerequisites:
- You must have `espeak` and `ffmpeg` installed
- You must have `docker` and `docker-compose` installed to use the docker-compose setup

### Running the server:
- Native host: `unicorn main:app --host 0.0.0.0 --port 5555`
- Docker compose: `sudo docker-compose up -d`

### Making requests
Send a `POST` request to `http://$addr:5555/generate` with a body content like:
```json
{
  "text":"Your text here."
}
```
you will receive a response like:
```json
{
  "status": "ok", # The request was processed successfully
  "fileid": "3517be4a1c1cbb75", # The file ID of the created file
  "new": true # Whether or not the file was generated, or already existed
}
```
you can access the generated file at `http://$addr:5555/static/$fileid.mp3`
