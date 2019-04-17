#!/usr/bin/env python
from typing import List

from nbconvert.preprocessors import ExecutePreprocessor
from nbformat.notebooknode import NotebookNode

from nbless.main.nbuild import nbuild


def nbless(filenames: List[str], kernel: str = "python3") -> NotebookNode:
    """Create an executed Jupyter notebook from markdown and code files.

    :param filenames: A list of markdown and code file names.
    :param kernel: The programming language used to run the notebook.
    """
    nb = nbuild(filenames)
    ep = ExecutePreprocessor(timeout=600, kernel_name=kernel)
    ep.preprocess(nb, {"metadata": {"path": "."}})
    return nb
