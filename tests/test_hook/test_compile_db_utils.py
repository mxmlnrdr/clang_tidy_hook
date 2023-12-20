import os

from tests.test_hook.cmake_helper import (
    execute_cmake_dummy_project,
    clean_cmake_dummy_project,
    BUILD_FOLDER,
)

from hook.compile_db_utils import (
    find_compilation_database,
    extract_source_file_list,
)


def test_find_compilation_database() -> None:
    execute_cmake_dummy_project()
    expected_result = os.path.join(
        "./" + BUILD_FOLDER + "/" + "compile_commands.json"
    )

    result = find_compilation_database()
    clean_cmake_dummy_project()

    assert result == expected_result


def test_find_none_compilation_database() -> None:
    expected_result = None

    result = find_compilation_database()

    assert result == expected_result


def test_extract_source_file_list() -> None:
    execute_cmake_dummy_project()
    compile_db_path = os.path.join(
        "./" + BUILD_FOLDER + "/" + "compile_commands.json"
    )
    current_work_dir = os.path.normpath(os.path.join(os.getcwd()))
    expected_result = [
        current_work_dir + "/" + "tests/test_hook/dummy_project/err.cpp",
        current_work_dir + "/" + "tests/test_hook/dummy_project/ok.cpp",
    ]

    result = extract_source_file_list(compile_db_path=compile_db_path)
    clean_cmake_dummy_project()

    assert result == expected_result
