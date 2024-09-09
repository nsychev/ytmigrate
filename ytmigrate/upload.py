import os

import click
import vk_api


def upload(
    video_path: str,
    name: str,
    /,
    group_id: int | None = None,
    album_id: int | None = None,
    thumbnail_path: str | None = None,
    description: str | None = None,
    # does not work for now
    is_public: bool = False,
    debug: bool = False
) -> str:
    vk_session = vk_api.VkApi(token = os.environ["VK_TOKEN"], api_version="5.199")
    uploader = vk_api.VkUpload(vk_session)

    click.echo(click.style("[*] Uploading video to VK", fg="yellow"))

    video = uploader.video(
        video_path,
        name=name,
        description=description,
        group_id=group_id,
        album_id=album_id,
        # does not work for now
        privacy_view="all" if is_public else None
    )

    if debug:
        click.echo(
            click.style(
                f"[.] Uploaded video info: {video}",
                fg="black"
            )
        )

    click.echo(
        click.style(
            f"[+] Video uploaded: https://vk.com/video{video['owner_id']}_{video['video_id']}",
            fg="green"
        )
    )


    if thumbnail_path:
        uploader.thumb_video(
            photo_path=thumbnail_path,
            owner_id=video["owner_id"],
            video_id=video["video_id"]
        )

        click.echo(click.style("[+] Thumbnail updated", fg="green"))
    else:
        click.echo(click.style("[-] No thumbnail provided, skipping this step", fg="yellow"))

    # TODO: fix
    click.echo(click.style("[!] Do not forget to publish the video manually in VK", fg="yellow"))
