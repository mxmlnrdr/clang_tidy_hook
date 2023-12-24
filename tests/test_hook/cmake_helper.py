import os
import shutil

from cmake import _program as cmake_caller

DUMMY_PROJECT_FOLDER = "tests/test_hook/dummy_project"
BUILD_FOLDER = "tests/test_hook/dummy_project/build"


def execute_cmake_dummy_project() -> None:
    cmake_caller(
        "cmake",
        [
            "-DCMAKE_BUILD_TYPE=Debug",
            "-S " + DUMMY_PROJECT_FOLDER,
            "-B " + BUILD_FOLDER,
        ],
    )


def clean_cmake_dummy_project() -> None:
    if os.path.exists(BUILD_FOLDER):
        shutil.rmtree(BUILD_FOLDER)
