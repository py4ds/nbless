import nbformat


def nbread(filename: str) -> nbformat.notebooknode.NotebookNode:
    with open(filename) as f:
        return nbformat.read(f, as_version=4)
