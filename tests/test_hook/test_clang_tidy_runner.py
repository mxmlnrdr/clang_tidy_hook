import pytest
from tests.test_hook.cmake_helper import (
    execute_cmake_dummy_project,
    clean_cmake_dummy_project,
)

from hook.clang_tidy_runner import ClangTidyRunner


def test_clang_tidy_runner_no_error_found() -> None:
    execute_cmake_dummy_project()
    input_arguments = [
        "-p=tests/test_hook/dummy_project/build/compile_commands.json",
        "--print-all-options",
    ]

    input_files = [
        "tests/test_hook/dummy_project/ok.c",
        "tests/test_hook/dummy_project/ok.cpp",
    ]

    runner = ClangTidyRunner(args=input_arguments, source_files=input_files)
    with pytest.raises(SystemExit) as execution_info:
        runner.run()
    clean_cmake_dummy_project()

    assert execution_info.value.code == 0


def test_clang_tidy_runner_error_found() -> None:
    execute_cmake_dummy_project()
    input_arguments = [
        "-p=tests/test_hook/dummy_project/build/compile_commands.json",
        "--print-all-options",
    ]

    input_files = [
        "tests/test_hook/dummy_project/err.c",
        "tests/test_hook/dummy_project/err.cpp",
    ]

    runner = ClangTidyRunner(args=input_arguments, source_files=input_files)
    with pytest.raises(SystemExit) as execution_info:
        runner.run()
    clean_cmake_dummy_project()

    assert execution_info.value.code == 1


def test_clang_tidy_runner_header_file() -> None:
    execute_cmake_dummy_project()
    input_arguments = [
        "-p=tests/test_hook/dummy_project/build/compile_commands.json",
        "--print-all-options",
    ]

    input_files = ["tests/test_hook/dummy_project/include/ok.h"]

    runner = ClangTidyRunner(args=input_arguments, source_files=input_files)
    with pytest.raises(SystemExit) as execution_info:
        runner.run()
    clean_cmake_dummy_project()

    assert execution_info.value.code == 0
