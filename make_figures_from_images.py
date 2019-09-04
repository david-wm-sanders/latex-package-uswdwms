#!venv/bin/python3
"""Generates LaTeX figure floats for screenshots."""
import itertools
import sys
import time
from pathlib import Path


output_dir = Path(__file__).parent / "sections/_figure_lists/"
image_exts = ["png", "jpg", "jpeg"]


def escape_string_for_latex(s):
    s = s.replace("_", "\\_")
    return s


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: make_figures_from_images.py source_dir")
        sys.exit(1)

    source_path = Path(sys.argv[1])
    folder_name = source_path.name

    # Make the output_dir, creating parents as necessary
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Finding images in '{str(source_path)}'...")
    # shots = source_path.glob("*.png")
    images = []
    for ext in image_exts:
        images.extend(source_path.glob(f"*.{ext}"))

    tf_p = output_dir / f"_{folder_name}_{time.strftime('%Y%m%d%H%M%S')}.tex"
    with tf_p.open(mode="w", encoding="utf-8") as tf:
        for image in images:
            print(f"Processing {str(image)}")
            # Begin a figure
            tf.write("\\begin{figure}[h!]\n")
            # Configure figure
            tf.write("\\centering\n\\captionsetup{skip=\\skipfigurecaptionlen}\n")
            # Include graphic
            image_p = str(image)
            image_p = image_p.replace("\\", "/")
            tf.write(f"\\includegraphics[width=1\\textwidth]{{{image_p}}}\n")
            # Add blank caption
            tf.write(f"\\caption{{\\todo{{blank: insert caption for {escape_string_for_latex(image.stem)}}}}}\n")
            # Add label
            label_id = f"fig:{image.stem}"
            tf.write(f"\\label{{{label_id}}}\n")
            # End figure
            tf.write("\\end{figure}\n")
            # Insert pagebreak
            tf.write("\\pagebreak\n\n")
