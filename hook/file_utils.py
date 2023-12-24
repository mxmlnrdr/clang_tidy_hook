from typing import List

from hook.path_utils import (
    extract_header_pathes,
    match_absolute_headers_in_include_dirs,
    convert_to_relative_pathes,
    match_absolute_pathes_based_on_relative_pathes,
)


def get_compiled_files(
    files: List[str], include_dirs: List[str], source_files: List[str]
) -> List[str]:
    relative_files = convert_to_relative_pathes(input_pathes=files)

    header_files = extract_header_pathes(files=relative_files)
    compiled_files = match_absolute_headers_in_include_dirs(
        headers=header_files, include_dirs=include_dirs
    )

    compiled_files += match_absolute_pathes_based_on_relative_pathes(
        absolute_pathes=source_files, relative_pathes=relative_files
    )
    return compiled_files
