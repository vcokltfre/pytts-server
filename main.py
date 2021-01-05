from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.pytts import TTSGenerator


class Data(BaseModel):
    text: str


app = FastAPI(docs_url=None)
tts = TTSGenerator()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/generate")
async def generate(text: Data):
    tid, new = await tts.generate(text.text)
    return {"status":"ok", "fileid":tid, "new":new}
