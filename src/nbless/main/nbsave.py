import nbformat


def nbsave(nb_name: str, nb: nbformat.notebooknode.NotebookNode) -> None:
    """Save an nbformat NotebookNode object as an ipynb file."""
    with open(nb_name, "w") as file:
        nbformat.write(nb, file)
