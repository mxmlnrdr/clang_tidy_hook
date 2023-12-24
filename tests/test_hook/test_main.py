import sys
import pytest

from hook.main import main
from tests.test_hook.cmake_helper import (
    execute_cmake_dummy_project,
    clean_cmake_dummy_project,
)


def dummy_function() -> None:
    sys.stderr.write("Nothing to do here.\n")
    sys.exit(1)


def test_dummy(capsys) -> None:  # type: ignore
    with pytest.raises(SystemExit) as execution_info:
        dummy_function()
    out, err = capsys.readouterr()
    assert execution_info.value.code == 1
    assert err == "Nothing to do here.\n"


def test_main_no_compilation_database(capsys) -> None:  # type: ignore
    clean_cmake_dummy_project()
    input_arguments = ["placeholder for default sys.argv[0]"]

    input_files = [
        "tests/test_hook/dummy_project/ok.c",
        "tests/test_hook/dummy_project/ok.cpp",
        "tests/test_hook/dummy_project/include/ok.h",
    ]

    with pytest.raises(SystemExit) as execution_info:
        main(argv=input_arguments + input_files)
    out, err = capsys.readouterr()

    assert execution_info.value.code == 0
    assert (
        "No compilation database found. " "SKIPPING code checker run.\n" in err
    )


def test_main_no_compiled_files(capsys) -> None:  # type: ignore
    execute_cmake_dummy_project()
    input_arguments = ["placeholder for default sys.argv[0]"]

    input_files = [
        "tests/test_hook/__init__.py",
        "tests/test_hook/dummy_project/ok.c",
    ]

    with pytest.raises(SystemExit) as execution_info:
        main(argv=input_arguments + input_files)
    out, err = capsys.readouterr()
    clean_cmake_dummy_project()

    assert execution_info.value.code == 0
    assert "No compiled files to check. " "SKIPPING code checker run.\n" in err


def test_main_no_error_found(capsys) -> None:  # type: ignore
    execute_cmake_dummy_project()
    input_arguments = ["placeholder for default sys.argv[0]"]

    input_files = [
        "tests/test_hook/dummy_project/ok.c",
        "tests/test_hook/dummy_project/ok.cpp",
        "tests/test_hook/dummy_project/include/ok.h",
    ]

    with pytest.raises(SystemExit) as execution_info:
        main(argv=input_arguments + input_files)
    out, err = capsys.readouterr()
    clean_cmake_dummy_project()

    assert execution_info.value.code == 0
    assert "inclusion of deprecated C++ header 'math.h'" in err
    assert "inclusion of deprecated C++ header 'stdio.h'" in err


def test_main_error_found(capsys) -> None:  # type: ignore
    execute_cmake_dummy_project()
    input_arguments = ["placeholder for default sys.argv[0]"]

    input_files = [
        "tests/test_hook/dummy_project/err.cpp",
        "tests/test_hook/dummy_project/ok.c",
        "tests/test_hook/dummy_project/ok.cpp",
        "tests/test_hook/dummy_project/include/ok.h",
    ]

    with pytest.raises(SystemExit) as execution_info:
        main(argv=input_arguments + input_files)
    out, err = capsys.readouterr()
    clean_cmake_dummy_project()

    assert execution_info.value.code == 1
    assert "error: non-void function 'main' should return a value" in err
