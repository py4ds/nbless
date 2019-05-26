#!/usr/bin/env python
from typing import List, Union
from pathlib import Path

import nbformat


def nbuild(filenames: Union[List[str], List[Path]]) -> nbformat.notebooknode.NotebookNode:
    """Create an unexecuted Jupyter notebook from markdown and code files.

    :param filenames: A list of source file names.
    """
    nb = nbformat.v4.new_notebook()
    if all(isinstance(x, str) for x in filenames):
        nb.cells = [
            nbformat.v4.new_code_cell(Path(name).read_text())
            if name.endswith((".py", ".R"))
            else nbformat.v4.new_markdown_cell(Path(name).read_text())
            for name in filenames
        ]
    elif all(isinstance(x, Path) for x in filenames):
        nb.cells = [
            nbformat.v4.new_code_cell(path.read_text())
            if path.name.endswith((".py", ".R"))
            else nbformat.v4.new_markdown_cell(path.read_text())
            for path in filenames
        ]

    return nb
