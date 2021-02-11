# web-video-test

Sample project showing how to generate, stream, and use HLS video.

## Components

- HLS Generator: uses `pyav` to write a video stream that changes over time
- Server: uses `fastapi` to serve videos in the `backend/public/video` folder
  via the `streams/{file}` route
- Client: uses `react-hls-player` (based on `hls.js`) to request the video
  from the server

Note that the HLS generator is hooked up to start when the server starts.

## Install

Uses `npm` for JS packages and `poetry` for Python packages.

### Front End

The front end was initialized with `create-react-app`.

```sh
cd frontend && npm install
```

### Back End

```sh
cd backend && poetry install
```

## Run

### Front End

```sh
cd frontend && npm start
```

This should open a web browser to <http://localhost:3000>.

### Back End

```sh
cd backend && poetry run uvicorn backend.main:app
```

An HLS video should start being written to `backend/public/videos/vid.m3u8`.

Once both processes are started, the video should play in the browser (you
may need to refresh the page).
