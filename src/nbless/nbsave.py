import nbformat


def nbsave(filename: str, nb: nbformat.notebooknode.NotebookNode) -> None:
    """Save an nbformat NotebookNode object as an ipynb file.

    :param filename: The name of the Jupyter notebook file to be saved.
    :param nb: The ``NotebookNode`` object to be saved to a file.
    """
    with open(filename, "w") as file:
        nbformat.write(nb, file)
