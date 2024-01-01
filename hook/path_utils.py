import os
from typing import List


def extract_file_pathes(argument_list: List[str]) -> List[str]:
    return [f for f in argument_list if os.path.exists(f)]


def extract_arguments(input_arguments: List[str]) -> List[str]:
    extracted_arguments = []
    for arg in input_arguments:
        if arg.startswith("-"):
            extracted_arguments.append(arg)
    return extracted_arguments


def convert_to_relative_pathes(input_pathes: List[str]) -> List[str]:
    return [os.path.relpath(path) for path in input_pathes]


def match_absolute_pathes_based_on_relative_pathes(
    absolute_pathes: List[str], relative_pathes: List[str]
) -> List[str]:
    matched_files = [
        absolute
        for absolute in absolute_pathes
        if any(absolute.endswith(relative) for relative in relative_pathes)
    ]
    return matched_files


def extract_header_pathes(files: List[str]) -> List[str]:
    header_extension = ["h", "hpp"]
    headers = [
        file for file in files if file.split(".")[-1] in header_extension
    ]
    return headers


def match_absolute_headers_in_include_dirs(
    headers: List[str], include_dirs: List[str]
) -> List[str]:
    headers_matched_absolute = []
    includes_filtered = [
        single_dir[:-1] if single_dir.endswith("/") else single_dir
        for single_dir in include_dirs
    ]
    for include in includes_filtered:
        for header in headers:
            if include.endswith(os.path.dirname(header)):
                headers_matched_absolute.append(
                    include + "/" + header.split("/")[-1]
                )
            elif include.endswith(os.path.dirname(os.path.dirname(header))):
                header_split = header.split("/")
                headers_matched_absolute.append(
                    include + "/" + header_split[-2] + "/" + header_split[-1]
                )
    return headers_matched_absolute
