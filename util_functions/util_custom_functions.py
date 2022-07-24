from functools import reduce
from os import remove
from pathlib import Path


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


def clean_up(title_filename: tuple[str, list[str]]) -> bool:
    a_video_title, filenames = title_filename
    for f_name in filenames:
        remove(f_name)
    filenames_exist = all(map(lambda file: Path(file).exists(), filenames))
    a_video_title_file = f"{a_video_title}.txt"
    remove(a_video_title_file)
    return not filenames_exist and not Path(a_video_title_file).exists()
