import subprocess
from pathlib import Path

print(f"Making example...")
commands = [["pdflatex.exe", "-shell-escape", "example.tex"],
            ["bibtex.exe", "example.aux"],
            ["pdflatex.exe", "-shell-escape", "example.tex"],
            ["pdflatex.exe", "-shell-escape", "example.tex"]]
for command in commands:
    subprocess.run(command)
