#!/usr/bin/env python
from typing import List

from nbconvert.preprocessors import ExecutePreprocessor
from nbformat.notebooknode import NotebookNode

from nbless.nbuild import nbuild


def nbless(in_files: List[str], kernel: str = "python3") -> NotebookNode:
    """Create an executed Jupyter notebook from markdown and code files.

    :param in_files: A list of names of markdown and code files.
    :param kernel: The programming language used to run the notebook.
    """
    nb = nbuild(in_files)
    ep = ExecutePreprocessor(timeout=600, kernel_name=kernel)
    ep.preprocess(nb, {"metadata": {"path": "."}})
    return nb
