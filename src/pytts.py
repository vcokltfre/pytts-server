import pyttsx3
import concurrent.futures
from asyncio import get_event_loop
from pathlib import Path

Path("./static").mkdir(exist_ok=True)


class TTSGenerator:
    def __init__(self, max_len: int = 512):
        self.max_len = max_len
        self.loop = get_event_loop()
        self.engine = pyttsx3.init()

    def _generate_file(self, text: str):
        text = text.lower()
        tid = hex(abs(hash(text)))[2:]
        if Path(f"./static/{tid}.mp3").exists():
            return tid, False
        self.engine.save_to_file(text[:self.max_len], f"./static/{tid}.mp3")
        self.engine.runAndWait()
        return tid, True

    async def generate(self, text: str):
        with concurrent.futures.ThreadPoolExecutor() as pool:
            result = await self.loop.run_in_executor(pool, self._generate_file, text)
        return result
