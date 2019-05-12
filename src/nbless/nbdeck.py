# !/usr/bin/env python
import nbformat


def nbdeck(filename: str) -> nbformat.notebooknode.NotebookNode:
    """ Set up a Jupyter notebook to be viewed as or converted into slides.

    Sets `slide_type` to ``slide`` for markdown cells that start with headers.
    After running ``nbdeck``, you can
    - view Jupyter notebooks on nbviewer or with the RISE extension
    - create an HTML slideshow with ``nbconv`` or ``jupyter nbconvert``.

    :param filename: The name of the input Jupyter notebook file.
    """
    nb = nbformat.read(filename, as_version=4)
    for n, cell in enumerate(nb.cells):
        if cell.cell_type == "markdown" and cell.source.startswith("#"):
            nb.cells[n].metadata = {"slideshow": {"slide_type": "slide"}}
    return nb
