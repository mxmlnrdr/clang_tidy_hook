[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![build status](https://github.com/mxmlnrdr/clang_tidy_hook/actions/workflows/pre-commit_ci.yml/badge.svg)](https://github.com/mxmlnrdr/clang_tidy_hook/actions/workflows/pre-commit_ci.yml)
[![build status](https://github.com/mxmlnrdr/clang_tidy_hook/actions/workflows/pytest.yml/badge.svg)](https://github.com/mxmlnrdr/clang_tidy_hook/actions/workflows/pytest.yml)
# clang_tidy_hook
A pre-commit hook implementation for usage of clang-tidy.

## Features
- ready to use without additional system dependencies
- installs clang-tidy within the hook as a python module
- searches for existing compilation database (compile_commands.json)
- aborts pre-commit without error in case no compilation database available
- calls clang-tidy only for *.c / *.cpp files which are part of compilation database
- calls clang-tidy only for *.h / *.hpp files which are in include directories of compilation database
- supports all clang-tidy offered input arguments
- clang-tidy warnings are printed but lead to successful hook exit (return code 0)
- clang-tidy errors are printed and lead to unsuccessful hook exit (return code 1)

## Limitations
- compilation database has to be available within repository (preceding execution of cmake required by user). Details about compilation database can be found [here](https://clang.llvm.org/docs/JSONCompilationDatabase.html).

## Contribution
To develop on this codebase & execute the tests:
```
python -m pip install -e '.[test]'
```

## Acknowledgments
* `clang-tidy` itself is [provided by the LLVM project](https://github.com/llvm/llvm-project) under the Apache 2.0 License with LLVM exceptions.
* [pre-commit framework](https://pre-commit.com/) for managing and maintaining multi-language pre-commit hooks
* Work for this pre-commit hook inspired by: [Ross Jacob's pre-commit-hooks](https://github.com/pocc/pre-commit-hooks)
