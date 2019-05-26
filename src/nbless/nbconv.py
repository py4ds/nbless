#!/usr/bin/env python
from pathlib import Path
from typing import List, Union

from nbconvert.exporters.base import get_exporter


def nbconv(in_file: Union[str, Path], exporter: str = "python") -> List[str]:
    """Convert a notebook into various formats using ``nbformat`` exporters.

    :param in_file: The name of the input notebook file.
    :param exporter: The exporter that determines the output file type.
    :note: The exporter type must be 'asciidoc', 'pdf', 'html', 'latex',
           'markdown', 'python', 'rst', 'script', or 'slides'.
           pdf requires latex, 'notebook' does nothing,
           slides need to served (not self-contained).
    """
    if isinstance(in_file, Path):
        contents, resources = get_exporter(exporter)().from_file(in_file.open())
    elif isinstance(in_file, str):
        contents, resources = get_exporter(exporter)().from_filename(in_file)
    else:
        print("The in_file argument must be a string or pathlib Path object.")
    out_name = Path(in_file).stem + resources.get("output_extension", ".txt")
    return [out_name, contents]
