#!/usr/bin/env python
from typing import Tuple

from nbconvert.exporters.base import get_exporter

from nbless.helpers.get_stem import get_stem


def nbconv(nb_name: str, exporter: str = "python") -> Tuple[str, str]:
    """Convert a notebook into various formats using ``nbformat`` exporters.

    :param input_name: The name of the input notebook.
    :param exporter: The exporter that determines the output file type.
    :note: The exporter type must be 'asciidoc', 'pdf', 'html', 'latex',
           'markdown', 'python', 'rst', 'script', or 'slides'.
           pdf requires latex, 'notebook' does nothing,
           slides need to served (not self-contained).
    """
    contents, resources = get_exporter(exporter)().from_filename(nb_name)
    out_name = get_stem(nb_name) + resources.get("output_extension", ".txt")
    return out_name, contents
