#!/usr/bin/env python
from pathlib import Path
from typing import Tuple

from nbconvert.exporters.base import get_exporter


def nbconv(in_file: str, exporter: str = '', out: str = '') -> Tuple[str, str]:
    """Convert a notebook into various formats using ``nbformat`` exporters.

    :param in_file: The name of the input notebook file.
    :param out: The name of the output file.
    :param exporter: The exporter that determines the output file type.
    :return: A 2-tuple of the output file's 1) name and 2) contents.
    :note: The exporter type must be 'asciidoc', 'pdf', 'html', 'latex',
           'markdown', 'python', 'rst', 'script', or 'slides'.
           All formats except 'HTML' require pandoc.
           Exporting to pdf requires latex.
    """
    in_path = Path(in_file)
    if not exporter:
        ext_exp_dict = {
            ".asciidoc": "asciidoc",
            ".adoc": "asciidoc",
            ".asc": "asciidoc",
            ".pdf": "pdf",
            ".html": "html",
            ".tex": "latex",
            ".md": "markdown",
            ".py": "python",
            ".R": "script",
            ".rst": "rst",
        }
        if in_path.suffix in ext_exp_dict:
            exporter = ext_exp_dict[in_path.suffix]
        else:
            print("Unable to infer exporter type!")
    contents, resources = get_exporter(exporter)().from_filename(in_file)
    if not out:
        name = in_path.stem + resources.get("output_extension", ".txt")
        return name, contents
    else:
        return out, contents
