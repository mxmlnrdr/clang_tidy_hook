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
