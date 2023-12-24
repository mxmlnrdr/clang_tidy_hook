import os

from tests.test_hook.cmake_helper import (
    execute_cmake_dummy_project,
    clean_cmake_dummy_project,
    BUILD_FOLDER,
)

from hook.compilation_database import CompilationDatabase


def test_find_compilation_database() -> None:
    execute_cmake_dummy_project()
    compile_db = CompilationDatabase()
    expected_result = os.path.join(
        "./" + BUILD_FOLDER + "/" + "compile_commands.json"
    )

    result_existing = compile_db.is_existing()
    result_path = compile_db.get_database_path()
    clean_cmake_dummy_project()

    assert result_existing
    assert result_path == expected_result


def test_find_none_compilation_database() -> None:
    compile_db = CompilationDatabase()

    result_existing = compile_db.is_existing()
    result_path = compile_db.get_database_path()

    assert not result_existing
    assert result_path is None


def test_extract_include_directory_list() -> None:
    execute_cmake_dummy_project()
    compile_db = CompilationDatabase()
    current_work_dir = os.path.normpath(os.path.join(os.getcwd()))
    expected_result = [
        current_work_dir + "/" + "tests/test_hook" "/dummy_project/include"
    ]

    result = compile_db.get_include_directories()
    clean_cmake_dummy_project()

    assert result == expected_result


def test_extract_source_file_list() -> None:
    execute_cmake_dummy_project()
    compile_db = CompilationDatabase()
    current_work_dir = os.path.normpath(os.path.join(os.getcwd()))
    expected_result = [
        current_work_dir + "/" + "tests/test_hook/dummy_project/err.cpp",
        current_work_dir + "/" + "tests/test_hook/dummy_project/ok.cpp",
    ]

    result = compile_db.get_source_file_list()
    clean_cmake_dummy_project()

    assert result == expected_result
