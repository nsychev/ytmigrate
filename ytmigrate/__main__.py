import os
import sys
import tempfile

import click
from .download import download
from .upload import upload


def reupload(url: str, path: str, group_id: int | None, album_id: int | None, publish: bool, debug: bool):
    video = download(path, url)
    upload(
        video.video_path,
        video.title,
        group_id=group_id,
        album_id=album_id,
        thumbnail_path=video.thumbnail_path,
        description=video.description,
        # is_public=publish,
        debug=debug,
    )


@click.command()
@click.option("--group-id", "-g", type=int, help="Group ID to upload to, defaults to personal page.")
@click.option("--album-id", "-a", type=int, help="Album ID to upload to, optional.")
@click.option("--publish", is_flag=True, help="Make the video public.", hidden=True)  # TODO
@click.option("--debug", is_flag=True, help="Debug mode (warning: very verbose).")
@click.argument("url", type=str)
def main(group_id: int | None, album_id: int | None, debug: bool, url: str, publish: bool = False):
    """Tool for migrating videos from YouTube to VK."""
    if "VK_TOKEN" not in os.environ:
        click.echo(click.style("[!] VK_TOKEN environment variable is not set", fg="red"))
        sys.exit(1)

    if debug:
        from http.client import HTTPConnection
        HTTPConnection.debuglevel = 1

        import pathlib
        target = (pathlib.Path.cwd() / "ytmigrate-debug")
        target.mkdir(exist_ok=True)
        click.echo(click.style(f"[!] Debug mode enabled, saving to {target}", fg="red"))

        reupload(url, str(target), group_id, album_id, publish, debug)
    else:
        with tempfile.TemporaryDirectory() as temp_dir:
            reupload(url, temp_dir, group_id, album_id, publish, debug)


if __name__ == "__main__":
    main()
