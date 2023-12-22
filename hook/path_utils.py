import os
from typing import List


def extract_file_pathes(argument_list: List[str]) -> List[str]:
    return [f for f in argument_list if os.path.exists(f)]


def convert_to_relative_pathes(input_pathes: List[str]) -> List[str]:
    return [os.path.relpath(path) for path in input_pathes]


def match_absolute_pathes_based_on_relative_pathes(
    absolute_pathes: List[str], relative_pathes: List[str]
) -> List[str]:
    matched_files = [
        absolute
        for absolute in absolute_pathes
        if any(relative in absolute for relative in relative_pathes)
    ]
    return matched_files


def extract_header_pathes(files: List[str]) -> List[str]:
    header_extension = ["h", "hpp"]
    headers = [
        file for file in files if file.split(".")[-1] in header_extension
    ]
    return headers
