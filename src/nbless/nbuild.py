#!/usr/bin/env python
from typing import List
from pathlib import Path

from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from nbformat.notebooknode import NotebookNode


def nbuild(in_files: List[str]) -> NotebookNode:
    """Create an unexecuted Jupyter notebook from markdown and code files.

    :param in_files: A list of source file names.
    """
    nb = new_notebook()
    nb.cells = [
            new_code_cell(Path(name).read_text())
            if name.endswith((".py", ".R"))
            else new_markdown_cell(Path(name).read_text())
            for name in in_files
        ]

    return nb
