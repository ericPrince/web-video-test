"""
Starts a server that exposes (HLS) videos via "/streams/{file}"

The server also starts a process to generate an HLS video
"""

from pathlib import Path
import multiprocessing as mp

import numpy as np

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, StreamingResponse, FileResponse

from . import hls_example


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/streams/{file}")
async def stream_file(file):
    # TODO: handle if file does not exist
    return FileResponse(Path("public/videos") / file)


vid_process = mp.Process(target=hls_example.main)


@app.on_event("startup")
def start_vid_writer():
    vid_process.start()


@app.on_event("shutdown")
def stop_vid_writer():
    vid_process.terminate()
    # TODO: clean out public/videos


# old demo
"""
import cv2


@app.get("/video-stream")
async def video_stream():
    im = np.random.uniform(0, 255, [200, 300]).astype(np.uint8)
    _, data = cv2.imencode('.jpg', im)

    # return Response(bytearray(data), media_type="image/jpeg")
    return StreamingResponse(random_video(), media_type="multipart/x-mixed-replace;boundary=frame")


async def random_video():
    while True:
    # for _ in range(20):
        im = np.random.uniform(0, 255, [200, 300]).astype(np.uint8)

        _, data = cv2.imencode('.jpg', im)
        resp_data = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + bytearray(data) + b'\r\n'
        yield resp_data
        await asyncio.sleep(0.1)
"""
