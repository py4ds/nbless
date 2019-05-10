import nbformat


def nbsave(filename: str, nb: nbformat.notebooknode.NotebookNode) -> None:
    """Save an nbformat NotebookNode object as an ipynb file.

    :param filename: The filename of the output notebook.
    :param nb: The ``NotebookNode`` object to be saved to a file.
    """
    with open(filename, "w") as file:
        nbformat.write(nb, file)
