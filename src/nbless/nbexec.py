#!/usr/bin/env python
from pathlib import Path
from typing import Tuple

from nbconvert.preprocessors import ExecutePreprocessor
from nbformat.notebooknode import NotebookNode

from nbless.nbread import nbread


def nbexec(nb_name: str, kernel: str = "python3") -> Tuple[str, NotebookNode]:
    """Create an executed notebook without modifying the input notebook.

    :param nb_name: The ``NotebookNode`` object to be executed.
    :param kernel: The programming language used to execute the notebook.
    """
    stem, nb = Path(nb_name).stem, nbread(nb_name)
    ep = ExecutePreprocessor(timeout=600, kernel_name=kernel)
    ep.preprocess(nb, {"metadata": {"path": "."}})
    return stem + "_executed.ipynb", nb
