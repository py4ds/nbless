#!/usr/bin/env python
import nbformat
from typing import List

from nbless.helpers import read_file

from nbless.cli import nbuild_click



def nbuild(filenames: List[str]) -> nbformat.notebooknode.NotebookNode:
    """Create a Jupyter notebook from text files and Python or R scripts
    :param filenames: a list of source file names
    """
    nb = nbformat.v4.new_notebook()
    nb['cells'] = [nbformat.v4.new_code_cell(read_file(name))
                   if name.endswith(('.py', '.R'))
                   else nbformat.v4.new_markdown_cell(read_file(name))
                   for name in filenames]
    return nb



if __name__ == "__main__":
    nbuild_click()
