from pathlib import Path
import itertools as it

import numpy as np
import av

from .hls_stream import AvHlsStreamWriter


def main():
    """
    Generates a sample HLS video to be served by the server
    """
    vid_file = Path("public/videos/vid.m3u8")
    total_frames = 200
    width = 480
    height = 320

    vid_file.parent.mkdir(parents=True, exist_ok=True)

    with AvHlsStreamWriter(vid_file, width, height) as (container, stream):
        # for frame_i in range(total_frames):
        for frame_i in it.count():
            img = np.empty((width, height, 3))
            img[:, :, 0] = 0.5 + 0.5 * np.sin(
                2 * np.pi * (0 / 3 + frame_i / total_frames)
            )
            img[:, :, 1] = 0.5 + 0.5 * np.sin(
                2 * np.pi * (1 / 3 + frame_i / total_frames)
            )
            img[:, :, 2] = 0.5 + 0.5 * np.sin(
                2 * np.pi * (2 / 3 + frame_i / total_frames)
            )

            img = np.round(255 * img).astype(np.uint8)
            img = np.clip(img, 0, 255)

            frame = av.VideoFrame.from_ndarray(img, format="rgb24")
            for packet in stream.encode(frame):
                container.mux(packet)


if __name__ == "__main__":
    main()
