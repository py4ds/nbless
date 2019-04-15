import nbformat


def nbread(filename: str) -> nbformat.notebooknode.NotebookNode:
    """Read in a notebook as an nbformat NotebookNode object."""
    with open(filename) as f:
        return nbformat.read(f, as_version=4)
