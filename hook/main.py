#!/usr/bin/env python3
import logging
import sys
from typing import List

from hook.path_utils import (
    convert_to_relative_pathes,
    extract_file_pathes,
    match_absolute_pathes_based_on_relative_pathes,
)
from hook.compile_db_utils import (
    find_compilation_database,
    extract_source_file_list,
)
from hook.clang_tidy_runner import ClangTidyRunner


def extract_arguments(input_arguments: List[str]) -> List[str]:
    extracted_arguments = []
    for arg in input_arguments:
        if arg.startswith("-"):
            extracted_arguments.append(arg)
    return extracted_arguments


def main(argv: List[str] = sys.argv) -> None:
    logging.basicConfig(level=logging.INFO)
    logging.debug("Input args: " + " ".join(argv))
    files_to_check = extract_file_pathes(argv[1:])
    logging.debug("Input files: " + " ".join(files_to_check))
    files_to_check_relative = convert_to_relative_pathes(files_to_check)
    logging.debug("Input relative: " + " ".join(files_to_check_relative))
    compilation_database = find_compilation_database()
    if compilation_database is None:
        sys.stderr.write(
            "No compilation database found. " "SKIPPING code checker run.\n"
        )
        sys.exit(0)
    logging.debug("Compile db: " + compilation_database.__str__())
    source_file_list = extract_source_file_list(compilation_database.__str__())
    logging.debug("Compile db files: " + " ".join(source_file_list))
    compiled_files = match_absolute_pathes_based_on_relative_pathes(
        absolute_pathes=source_file_list,
        relative_pathes=files_to_check_relative,
    )
    logging.debug("Compiled files to check: " + " ".join(compiled_files))

    if not compiled_files:
        sys.stderr.write(
            "No compiled files to check. " "SKIPPING code checker run.\n"
        )
        sys.exit(0)
    arguments = extract_arguments(argv)
    arguments.append("-p=" + compilation_database.__str__())
    logging.debug("Arguments: " + " ".join(arguments))
    cmd = ClangTidyRunner(arguments, compiled_files)
    cmd.run()


if __name__ == "__main__":
    main()
