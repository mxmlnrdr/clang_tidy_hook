import os

from hook.path_utils import (
    extract_file_pathes,
    extract_arguments,
    convert_to_relative_pathes,
    match_absolute_pathes_based_on_relative_pathes,
    extract_header_pathes,
    match_absolute_headers_in_include_dirs,
)


def test_extract_file_pathes() -> None:
    input_args = [
        "tests/test_hook/__init__.py",
        "tests/test_hook/test_path_utils.py",
        "--print-all-options",
        "-header-filter=*/conan/cache_data/*",
    ]
    expected_output = [
        "tests/test_hook/__init__.py",
        "tests/test_hook/test_path_utils.py",
    ]

    result = extract_file_pathes(argument_list=input_args)
    assert result == expected_output


def test_extract_arguments() -> None:
    input_args = [
        "home/user/test_hook/main.py",
        "home/user/dummy_file.cpp",
        "/src/component/dummy_file.h",
        "--print-all-options",
        "-header-filter=*/conan/cache_data/*",
    ]
    expected_output = [
        "--print-all-options",
        "-header-filter=*/conan/cache_data/*",
    ]

    result = extract_arguments(input_arguments=input_args)
    assert result == expected_output


def test_convert_to_relative_pathes() -> None:
    input_pathes = [
        os.path.normpath(
            os.path.join(os.getcwd(), "tests/test_hook/__init__.py")
        )
    ]
    expected_output = ["tests/test_hook/__init__.py"]

    result = convert_to_relative_pathes(input_pathes=input_pathes)

    assert result == expected_output


def test_match_absolute_pathes_based_on_relative_pathes() -> None:
    input_pathes_absolute = [
        os.path.normpath(
            os.path.join(os.getcwd(), "tests/test_hook/__init__.py")
        ),
        os.path.normpath(
            os.path.join(os.getcwd(), "tests/test_hook/test_path_utils.py")
        ),
    ]
    input_pathes_relative = [
        "tests/test_hook/__init__.py",
        "tests/test_hook/test_path_utils.py",
        "tests/test_hook/not_existing.py",
    ]
    expected_output = [
        os.path.normpath(
            os.path.join(os.getcwd(), "tests/test_hook/__init__.py")
        ),
        os.path.normpath(
            os.path.join(os.getcwd(), "tests/test_hook/test_path_utils.py")
        ),
    ]

    result = match_absolute_pathes_based_on_relative_pathes(
        absolute_pathes=input_pathes_absolute,
        relative_pathes=input_pathes_relative,
    )

    assert result == expected_output


def test_extract_header_pathes() -> None:
    input_files = [
        "tests/test_hook/dummy_header.hpp",
        "tests/test_hook/dummy_source.cpp",
        "/tests/test_hook/example_header.h",
        "/tests/test_hook/example_source.c",
    ]
    expected_output = [
        "tests/test_hook/dummy_header.hpp",
        "/tests/test_hook/example_header.h",
    ]

    result = extract_header_pathes(files=input_files)
    assert result == expected_output


def test_match_absolute_headers_in_include_dirs() -> None:
    header_input = [
        "tests/first_directory/first_header.hpp",
        "/tests/second_directory/second_header.h",
        "/tests/third_directory/third_header.h",
        "/tests/fourth_directory/fourth_header.h",
        "/tests/fifth_directory/fifth_header.h",
        "/tests/seventh_header.h",
    ]

    include_directories = [
        "tests/first_directory/",
        "/tests/second_directory",
        "dummy_path_absolute/tests/third_directory/",
        "dummy_pathes_absolute/tests/fourth_directory",
        "dummy_pathes_absolute/tests/sixth_directory",
    ]

    expected_output = [
        "tests/first_directory/first_header.hpp",
        "/tests/second_directory/second_header.h",
        "dummy_path_absolute/tests/third_directory/third_header.h",
        "dummy_pathes_absolute/tests/fourth_directory/fourth_header.h",
    ]

    result = match_absolute_headers_in_include_dirs(
        headers=header_input, include_dirs=include_directories
    )

    assert result == expected_output


def test_match_absolute_headers_in_include_dirs_parent_level() -> None:
    header_input = [
        "tests/first_directory/library_name/first_header.hpp",
    ]

    include_directories = [
        "tests/first_directory/",
    ]

    expected_output = [
        "tests/first_directory/library_name/first_header.hpp",
    ]

    result = match_absolute_headers_in_include_dirs(
        headers=header_input, include_dirs=include_directories
    )

    assert result == expected_output
