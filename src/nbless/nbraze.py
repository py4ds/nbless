# !/usr/bin/env python
from typing import Dict
from pathlib import Path

import nbformat


def nbraze(in_file: str, extension: str = "py") -> Dict[str, str]:
    """Create markdown and code files from a Jupyter notebook.

    :param in_file: The name of the input Jupyter notebook file.
    :param extension: The extension for code files.
    """
    nb = nbformat.read(in_file, as_version=4)
    filenames = (
        f"{Path(in_file).stem}_cell{n}.md"
        if cell.cell_type == "markdown"
        else f"{Path(in_file).stem}_cell{n}.{extension}"
        for n, cell in enumerate(nb.cells)
    )
    sources = (
        cell.source
        for cell in nb.cells
    )
    return dict(zip(filenames, sources))
