# clang_tidy_hook
A pre-commit hook implementation for usage of clang-tidy.

## Features
- ready to use without additional system dependencies
- installs clang-tidy within the hook as a python module
- searches for existing compilation database (compile_commands.json)
- aborts pre-commit without error in case no compilation database available
- calls clang-tidy only for *.c/*.cpp files which are part of compilation database
- supports all clang-tidy offered input arguments
- clang-tidy warnings are printed but lead to successful hook exit (return code 0)
- clang-tidy errors are printed and lead to unsuccessful hook exit (return code 1)

## Limitations
- header files are currently ignored
- compilation database has to be available within repository (preceding execution of cmake required by user). Details about compilation database can be found [here](https://clang.llvm.org/docs/JSONCompilationDatabase.html).

## Source
Work inspired by:
https://github.com/pocc/pre-commit-hooks/
