#!/usr/bin/env python
from pathlib import Path
from typing import Tuple, Union

from nbconvert.exporters.base import get_exporter


def nbconv(filename: Union[str, Path], exporter: str = "python") -> Tuple[str, str]:
    """Convert a notebook into various formats using ``nbformat`` exporters.

    :param filename: The name of the input notebook file.
    :param exporter: The exporter that determines the output file type.
    :note: The exporter type must be 'asciidoc', 'pdf', 'html', 'latex',
           'markdown', 'python', 'rst', 'script', or 'slides'.
           pdf requires latex, 'notebook' does nothing,
           slides need to served (not self-contained).
    """
    contents, resources = get_exporter(exporter)().from_filename(
            filename.name if isinstance(filename, Path) else filename
            )
    out_name = Path(filename).stem + resources.get("output_extension", ".txt")
    return out_name, contents
