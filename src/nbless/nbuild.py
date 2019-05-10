#!/usr/bin/env python
from typing import List
from pathlib import Path

import nbformat


def nbuild(filenames: List[str]) -> nbformat.notebooknode.NotebookNode:
    """Create an unexecuted Jupyter notebook from markdown and code files.

    :param filenames: A list of source file names.
    """
    nb = nbformat.v4.new_notebook()
    nb["cells"] = [
        nbformat.v4.new_code_cell(Path(name).read_text())
        if name.endswith((".py", ".R"))
        else nbformat.v4.new_markdown_cell(Path(name).read_text())
        for name in filenames
    ]
    return nb
