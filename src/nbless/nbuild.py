#!/usr/bin/env python
from typing import List, Union
from pathlib import Path

from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from nbformat.notebooknode import NotebookNode


def nbuild(in_files: Union[List[str], List[Path]]) -> NotebookNode:
    """Create an unexecuted Jupyter notebook from markdown and code files.

    :param in_files: A list of source file names.
    """
    nb = new_notebook()
    if all(isinstance(x, str) for x in in_files):
        nb.cells = [
            new_code_cell(Path(name).read_text())
            if name.endswith((".py", ".R"))
            else new_markdown_cell(Path(name).read_text())
            for name in in_files
        ]
    elif all(isinstance(x, Path) for x in in_files):
        nb.cells = [
            new_code_cell(path.read_text())
            if path.name.endswith((".py", ".R"))
            else new_markdown_cell(path.read_text())
            for path in in_files
        ]
    else:
        print("The in_files argument must be a list of strings or pathlib "
              f"Path objects. The argument you passed was {in_files}.")

    return nb
