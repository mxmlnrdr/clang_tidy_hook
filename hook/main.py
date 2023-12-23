#!/usr/bin/env python3
import logging
import sys
from typing import List

from hook.path_utils import extract_file_pathes, extract_arguments
from hook.compile_db_utils import find_compilation_database
from hook.file_utils import get_compiled_files
from hook.clang_tidy_runner import ClangTidyRunner


def main(argv: List[str] = sys.argv) -> None:
    logging.basicConfig(level=logging.INFO)
    logging.debug("Input args: " + " ".join(argv))

    compile_db = find_compilation_database()
    if compile_db is None:
        sys.stderr.write(
            "No compilation database found. " "SKIPPING code checker run.\n"
        )
        sys.exit(0)
    logging.debug("Compile db: " + compile_db.__str__())

    files_to_check = extract_file_pathes(argv[1:])
    logging.debug("Input files: " + " ".join(files_to_check))

    compiled_files = get_compiled_files(
        files=files_to_check, compile_db=compile_db
    )
    logging.debug("Compiled files to check: " + " ".join(compiled_files))

    if not compiled_files:
        sys.stderr.write(
            "No compiled files to check. " "SKIPPING code checker run.\n"
        )
        sys.exit(0)
    arguments = extract_arguments(argv)
    arguments.append("-p=" + compile_db.__str__())
    logging.debug("Arguments: " + " ".join(arguments))
    cmd = ClangTidyRunner(arguments, compiled_files)
    cmd.run()


if __name__ == "__main__":
    main()
