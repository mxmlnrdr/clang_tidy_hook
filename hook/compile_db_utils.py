import os
import json
from typing import List, Union


def find_compilation_database() -> Union[str, None]:
    name = "compile_commands.json"
    path = "./"
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None


def extract_source_file_list(compile_db_path: str) -> List[str]:
    with open(compile_db_path) as json_data:
        data = json.load(json_data)
        json_data.close()
    file_list = []
    for entry in data:
        file_list.append(entry["file"])
    return file_list


def extract_include_directories(compile_db_path: str) -> List[str]:
    with open(compile_db_path) as json_data:
        data = json.load(json_data)
        json_data.close()
    entries = [entry.__str__() for entry in data]
    entry_strings = [single.split(" ") for single in entries]
    entry_strings_flat = [
        item for sublist in entry_strings for item in sublist
    ]
    include_prefix = "-I"
    include_directories = [
        entry[len(include_prefix) :]
        for entry in entry_strings_flat
        if entry.startswith(include_prefix)
    ]
    # remove duplicates
    include_directories = list(set(include_directories))
    return include_directories
