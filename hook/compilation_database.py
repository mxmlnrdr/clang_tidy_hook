import os
import json
from typing import List, Union


class CompilationDatabase:
    def __init__(self) -> None:
        self.path: Union[str, None] = None
        self.include_directories: List[str] = []
        self.source_files: List[str] = []
        self.__find_compilation_database()
        if self.is_existing():
            self.__extract_include_directories()
            self.__extract_source_file_list()

    def __find_compilation_database(self) -> None:
        name = "compile_commands.json"
        path = "./"
        for root, dirs, files in os.walk(path):
            if name in files:
                self.path = os.path.join(root, name)

    def __extract_include_directories(self) -> None:
        if self.path is not None:
            with open(self.path) as json_data:
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
            self.include_directories = list(set(include_directories))

    def __extract_source_file_list(self) -> None:
        if self.path is not None:
            with open(self.path) as json_data:
                data = json.load(json_data)
                json_data.close()
            for entry in data:
                self.source_files.append(entry["file"])

    def is_existing(self) -> bool:
        return self.path is not None

    def get_database_path(self) -> Union[str, None]:
        return self.path

    def get_include_directories(self) -> List[str]:
        return self.include_directories

    def get_source_file_list(self) -> List[str]:
        return self.source_files
