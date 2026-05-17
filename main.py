from fastapi import FastAPI, UploadFile
from faster_whisper import WhisperModel
import tempfile
import uvicorn

app = FastAPI()

model = WhisperModel(
    "medium",
    device="cpu",
    compute_type="int8"
)


@app.post("/transcribe")
async def transcribe(file: UploadFile):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        temp_path = tmp.name

    segments, info = model.transcribe(
        temp_path,
        language="pl"
    )

    text = " ".join(segment.text for segment in segments)

    return {
        "text": text
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
