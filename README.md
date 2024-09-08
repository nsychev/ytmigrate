# ytmigrate

Tool for migrating videos from YouTube to VK.

## Why?

VK is awful, but in some cases we can't do anything because
YouTube access is now limited in Russia.

## Installation

Recommended way is via `pipx`:

```bash
pipx install git+https://github.com/nsychev/ytmigrate.git
```

Also `pip` works too (starting with 19.x, which added support for PEP 517), but do you really want to install a few more packages in your global Python distribution?

```bash
pip install git+https://github.com/nsychev/ytmigrate.git
```

Also you will need libmagic and ffmpeg. Find them in your package manager. For example, in Ubuntu:

```bash
sudo apt install libmagic1 ffmpeg
```

ffmpeg can be easily installed on Windows. See [ahupp/python-magic#293](https://github.com/ahupp/python-magic/issues/293) on how to install libmagic.

## Usage

```
Usage: ytmigrate [OPTIONS] URL

  Tool for migrating videos from YouTube to VK.

Options:
  -g, --group-id INTEGER  Group ID to upload to, defaults to personal page
  -a, --album-id INTEGER  Album ID to upload to, optional
  --debug                 Debug mode
  --help                  Show this message and exit.
```

Pass your VK token with video scope in environment variable `VK_TOKEN`.

[Issue token](https://oauth.vk.com/authorize?client_id=6287487&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1)

## Help wanted

- [ ] Support automatic publishing
- [ ] Upload entire playlists

## License

[MIT License](LICENSE) is applied to this repository.
