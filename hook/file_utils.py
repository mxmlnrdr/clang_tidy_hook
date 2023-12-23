from typing import List

from hook.compile_db_utils import (
    extract_include_directories,
    extract_source_file_list,
)
from hook.path_utils import (
    extract_header_pathes,
    match_absolute_headers_in_include_dirs,
    convert_to_relative_pathes,
    match_absolute_pathes_based_on_relative_pathes,
)


def get_compiled_files(files: List[str], compile_db: str) -> List[str]:
    relative_files = convert_to_relative_pathes(input_pathes=files)

    header_files = extract_header_pathes(files=relative_files)
    include_dirs = extract_include_directories(compile_db_path=compile_db)
    compiled_files = match_absolute_headers_in_include_dirs(
        headers=header_files, include_dirs=include_dirs
    )

    source_files = extract_source_file_list(compile_db_path=compile_db)
    compiled_files += match_absolute_pathes_based_on_relative_pathes(
        absolute_pathes=source_files, relative_pathes=relative_files
    )
    return compiled_files
