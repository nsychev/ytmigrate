import json
from dataclasses import dataclass
from pathlib import Path

import magic
from yt_dlp import YoutubeDL


@dataclass
class YoutubeResult:
    title: str
    description: str
    video_path: str
    thumbnail_path: str | None


def download(path: str, url: str) -> YoutubeResult:
    # https://github.com/yt-dlp/yt-dlp/blob/master/devscripts/cli_to_api.py
    yt_params = {
        'extract_flat': 'discard_in_playlist',
        'fragment_retries': 10,
        'ignoreerrors': 'only_download',
        'outtmpl': {'default': '%(id)s.%(ext)s'},
        'paths': {'home': path},
        'postprocessors': [{'key': 'FFmpegConcat',
                     'only_multi_video': True,
                     'when': 'playlist'}],
        'retries': 10,
        'writethumbnail': True,
        'writeinfojson': True
    }

    with YoutubeDL(params=yt_params) as ytdlp:
        ytdlp.download([url])

    video_path: str | None = None
    thumbnail_path: str | None = None
    json_path: str | None = None

    path_as_path = Path(path)

    for child in path_as_path.iterdir():
        mime = magic.from_file(child, mime=True)
        if mime.startswith("image/"):
            thumbnail_path = str(child)
        if mime.startswith("video/"):
            video_path = str(child)
        if mime.startswith("application/json"):
            json_path = str(child)

    if video_path is None or json_path is None:
        raise RuntimeError(f"Could not download video, no suitable files from {list(path_as_path.iterdir())}")

    with open(json_path) as f:
        info = json.load(f)

    return YoutubeResult(title=info["title"], description=info.get("description", ""), video_path=video_path, thumbnail_path=thumbnail_path)
