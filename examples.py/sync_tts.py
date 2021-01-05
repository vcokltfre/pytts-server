from requests import post, get

def get_tts(text: str, output: str, url: str = "https://localhost:5555"):
    resp = post(url + "/generate", json={"text":text})
    fileid = resp.json()["fileid"]

    resp = get(url + f"/static/{fileid}.mp3")
    with open(output, 'wb') as f:
        f.write(resp.content)
