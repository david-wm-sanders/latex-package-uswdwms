import subprocess
from pathlib import Path

print(f"Making example...")
commands = [["pdflatex.exe", "example.tex"],
            ["bibtex.exe", "example.aux"],
            ["pdflatex.exe", "example.tex"],
            ["pdflatex.exe", "example.tex"]]
for command in commands:
    subprocess.run(command)
