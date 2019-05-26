#!/usr/bin/env python
from typing import Tuple

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat.notebooknode import NotebookNode


def nbexec(in_file: str, kernel: str = "python3") -> Tuple[str, NotebookNode]:
    """Create an executed notebook without modifying the input notebook.

    :param in_file: The name of the Jupyter notebook file to be executed.
    :param kernel: The programming language used to execute the notebook.
    """
    nb = nbformat.read(in_file, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name=kernel)
    ep.preprocess(nb, {"metadata": {"path": "."}})
    return nb
