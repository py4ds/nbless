# !/usr/bin/env python
from typing import Dict
from pathlib import Path

import nbformat


def nbraze(filename: str, extension: str = "py") -> Dict[str, str]:
    """Create markdown and code files from a Jupyter notebook.

    :param filenames: The filename of the input jupyter notebook.
    :param extension: The extension for code files.
    """
    nb = nbformat.read(filename, as_version=4)
    filenames = (
        f"{Path(filename).stem}_cell{n}.md"
        if cell.cell_type == "markdown"
        else f"{Path(filename).stem}_cell{n}.{extension}"
        for n, cell in enumerate(nb.cells)
    )
    sources = (
        cell.source
        for cell in nb.cells
    )
    return dict(zip(filenames, sources))
