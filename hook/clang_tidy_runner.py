import subprocess
import sys
from typing import List

from clang_tidy import _get_executable as clang_tidy_get_exe


class ClangTidyRunner:
    def __init__(self, args: List[str], source_files: List[str]):
        self.command = clang_tidy_get_exe("clang-tidy").__str__()
        self.files = source_files
        self.args = args

    def run(self) -> None:
        stdout = b""
        stderr = b""
        output = b""
        returncode = 0

        for filename in self.files:
            call_argument = (
                self.command + " " + filename + " " + " ".join(self.args)
            )
            sp_child = subprocess.run(
                call_argument,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            stdout += sp_child.stdout
            stderr += sp_child.stderr
            output += sp_child.stdout
            output += sp_child.stderr
            returncode = max(sp_child.returncode, returncode)
        # --fix-errors returns 0 even if there are errors
        if len(stderr) > 0 and "--fix-errors" in self.args:
            returncode = 1
        sys.stderr.buffer.write(output)
        sys.exit(returncode)
