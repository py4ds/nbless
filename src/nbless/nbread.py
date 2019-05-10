import nbformat


def nbread(filename: str) -> nbformat.notebooknode.NotebookNode:
    """Read in a notebook file as an ``nbformat`` ``NotebookNode`` object.

    :param filename: The filename of the notebook to be read in.
    """
    with open(filename) as f:
        return nbformat.read(f, as_version=4)
