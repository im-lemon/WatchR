import yt_dlp # type:ignore

def yt_dwnld(video):
    ydl_opts = {
        'quiet': True,
        'merge_output_format': 'mp4',
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video)