# FastAPI Whisper Transcription (Docker)

This project exposes a `POST /transcribe` endpoint that accepts an audio file and returns transcribed text.

## Docker (build and run)

```powershell
docker build -t transcribe-api .
docker run --rm -p 8000:8000 transcribe-api
```

API will be available at `http://127.0.0.1:8000`.

## Docker Compose

```powershell
docker compose up --build
```

## Quick test request (PowerShell)

```powershell
curl.exe -X POST "http://127.0.0.1:8000/transcribe" -F "file=@C:\Users\bombe\Desktop\Audio_requests\Diagnoza_dane.wav"
```

## Notes

- The first request can be slower because Whisper model files may be downloaded on first run.
- This image installs `ffmpeg`, which is required for audio decoding with `faster-whisper`.

