#!/usr/bin/env python3
import sys
from typing import List

from hook.clang_tidy_runner import ClangTidyRunner
from hook.compilation_database import CompilationDatabase
from hook.file_utils import get_compiled_files
from hook.path_utils import extract_file_pathes, extract_arguments


def main(argv: List[str] = sys.argv) -> None:
    arguments = extract_arguments(argv)
    compile_db_directory = "./"
    compile_db = CompilationDatabase(compile_db_directory)
    if not compile_db.is_existing():
        sys.stderr.write(
            "No compilation database found in: "
            + str(compile_db_directory)
            + ".SKIPPING code checker run.\n"
        )
        sys.exit(0)

    files_to_check = extract_file_pathes(argv[1:])
    compiled_files = get_compiled_files(
        files=files_to_check,
        include_dirs=compile_db.get_include_directories(),
        source_files=compile_db.get_source_file_list(),
    )
    if not compiled_files:
        sys.stderr.write(
            "No compiled files to check in compilation database (Path: "
            + str(compile_db.get_database_path())
            + "). SKIPPING code checker run.\n"
        )
        sys.exit(0)

    arguments.append("-p=" + str(compile_db.get_database_path()))

    cmd = ClangTidyRunner(arguments, compiled_files)
    return_code, output = cmd.run()
    sys.stderr.buffer.write(output)
    sys.exit(return_code)


if __name__ == "__main__":
    main()
