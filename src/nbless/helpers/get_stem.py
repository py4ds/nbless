from pathlib import PurePath


def get_stem(input_name: str) -> str:
    return PurePath(input_name).stem
