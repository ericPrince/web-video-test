from typing import *
from pathlib import Path
from contextlib import contextmanager
import av


@contextmanager
def AvHlsStreamWriter(
    file: Union[Path, str],
    width: int,
    height: int,
    options: Dict[str, str] = {"hls_flags": "delete_segments"},
    codec: str = "h264",
    fps: Optional[float] = None,
    pix_fmt: str = "yuv420p",
):
    """
    Use as a context manager, provides the pyav container and stream

    with AvHlsStreamWriter('vid.m3u8', 300, 200) as container, stream:
        for img in np_frame_source():
            frame = av.VideoFrame.from_ndarray(img, format='rgb24')
            for packet in stream.encode(frame):
                container.mux(packet)

    """
    container = av.open(str(file), "w", format="hls", options=options)

    stream = container.add_stream(codec, rate=fps)
    stream.width = width
    stream.height = height
    stream.pix_fmt = pix_fmt

    yield container, stream

    # flush stream
    for packet in stream.encode():
        container.mux(packet)

    # close the file
    container.close()
