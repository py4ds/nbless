#!/usr/bin/env python
from nbconvert.preprocessors import ExecutePreprocessor
from nbless import nbread
from nbless.helpers import get_base
from nbless.cli import nbexec_click


def nbexec(nb_name: str) -> Tuple[str, nbformat.notebooknode.NotebookNode]:
    """Create an executed notebook without modifying the input notebook.
    :param nb_name: The name of the input notebook"""
    base, nb = get_base(nb_name), nbread(nb_name)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': '.'}})
    return base + '_executed.ipynb', nb


if __name__ == "__main__":
    nbexec_click()
