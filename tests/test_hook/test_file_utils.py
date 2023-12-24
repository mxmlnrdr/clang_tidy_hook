import os

from tests.test_hook.cmake_helper import (
    execute_cmake_dummy_project,
    clean_cmake_dummy_project,
)

from hook.file_utils import get_compiled_files


def test_get_compiled_files() -> None:
    execute_cmake_dummy_project()

    input_files = [
        "tests/test_hook/dummy_project/include/ok.h",
        "tests/test_hook/dummy_project/err.c",
        "tests/test_hook/dummy_project/err.cpp",
        "tests/test_hook/dummy_project/ok.c",
        "tests/test_hook/dummy_project/ok.cpp",
    ]

    current_work_dir = os.path.normpath(os.path.join(os.getcwd()))
    input_include_directories = [
        current_work_dir + "/" + "tests/test_hook/dummy_project/include",
    ]

    input_source_files = [
        current_work_dir + "/" + "tests/test_hook/dummy_project/err.cpp",
        current_work_dir + "/" + "tests/test_hook/dummy_project/ok.cpp",
    ]

    expected_output = [
        current_work_dir + "/" + "tests/test_hook/dummy_project/include/ok.h",
        current_work_dir + "/" + "tests/test_hook/dummy_project/err.cpp",
        current_work_dir + "/" + "tests/test_hook/dummy_project/ok.cpp",
    ]

    result = get_compiled_files(
        files=input_files,
        include_dirs=input_include_directories,
        source_files=input_source_files,
    )
    clean_cmake_dummy_project()

    assert result == expected_output
