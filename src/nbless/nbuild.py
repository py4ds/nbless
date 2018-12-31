#!/usr/bin/env python
from typing import List

import nbformat

from nbless.helpers.read_file import read_file


def nbuild(filenames: List[str]) -> nbformat.notebooknode.NotebookNode:
    """Create a Jupyter notebook from text files and Python or R scripts
    :param filenames: a list of source file names
    """
    nb = nbformat.v4.new_notebook()
    nb["cells"] = [
        nbformat.v4.new_code_cell(read_file(name))
        if name.endswith((".py", ".R"))
        else nbformat.v4.new_markdown_cell(read_file(name))
        for name in filenames
    ]
    return nb
