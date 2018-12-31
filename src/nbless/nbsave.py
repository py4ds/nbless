import nbformat


def nbsave(nb_name: str, nb: nbformat.notebooknode.NotebookNode) -> None:
    with open(nb_name, "w") as file:
        nbformat.write(nb, file)
