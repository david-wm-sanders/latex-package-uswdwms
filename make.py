import platform
import subprocess
from pathlib import Path


project_main = "report"


def executable(program):
    extension = ".exe" if platform.system() == "Windows" else ""
    return f"{program}{extension}"


if __name__ == '__main__':
    print(f"Making report...")
    xelatex, bibtex = executable("xelatex"), executable("bibtex")
    commands = [[xelatex, "-shell-escape", f"{project_main}.tex"],
                [bibtex, f"{project_main}.aux"],
                [xelatex, "-shell-escape", f"{project_main}.tex"],
                [xelatex, "-shell-escape", f"{project_main}.tex"]]
    for command in commands:
        subprocess.run(command)
