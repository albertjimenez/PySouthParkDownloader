from subprocess import run, DEVNULL
from sys import argv
from urllib.parse import urlparse

from yt_dlp import YoutubeDL

from post_processor.sp_post_processor import SPPostProcessor
from util_functions.util_custom_functions import compose, clean_up


def init_check_arguments(arguments: list[str]) -> str:
    def check_ffmpeg_is_installed():
        print("Checking if ffmpeg is present in PATH")
        try:
            assert run("ffmpeg -h",
                       shell=True, stdout=DEVNULL,
                       stderr=DEVNULL).returncode == 0, "Return code different than zero whilst running 'ffmpeg -h'. Installation may be corrupted"
        except Exception:
            print("ffmpeg is not found. Install it before using this script. Visit https://ffmpeg.org/download.html")

    check_ffmpeg_is_installed()
    if len(arguments) == 1:
        raise ValueError(
            "Argument URL is missing from argv. Please pass it as a parameter to the execution of this script")
    url = argv[1]
    if urlparse(url).scheme == "":
        raise ValueError(f"URL={url} is malformed or not a valid URL. Please amend it")
    return url


def download(url: str) -> tuple[str, list[str]]:
    ydl_opts = {}
    filename_collector = SPPostProcessor()
    with YoutubeDL(ydl_opts) as ydl:
        ydl.add_post_processor(filename_collector)
        info_dict = ydl.extract_info(url, download=True)
    if "webpage_url" not in info_dict or info_dict["webpage_url"].count("/") < 5:
        raise ValueError(
            f"webpage_url attribute could not be parsed into a valid title. Value={info_dict.get('webpage_url')}")
    video_title = info_dict.get("webpage_url", None).split('/')[5]
    for f_name in filename_collector.filenames:
        with open(f"{video_title}.txt", "a") as current_file:
            current_file.write("file '" + f_name + "'\n")
    command_to_run = f"ffmpeg -f concat -safe 0 -i {video_title}.txt -c copy {video_title}.mp4"
    run(command_to_run, shell=True)
    return video_title, filename_collector.filenames


if __name__ == '__main__':
    compose(clean_up, download, init_check_arguments)(argv)
