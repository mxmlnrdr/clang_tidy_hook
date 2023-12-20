from hook.main import extract_arguments


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
