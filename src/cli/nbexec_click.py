import sys

import click
import nbformat

from nbless.nbexec import nbexec


@click.command()
@click.argument("in_file")
@click.option("-k", "--kernel", "kernel")
@click.option("-o", "--out_file", "out")
def nbexec_click(in_file: str, kernel: str, out: str) -> None:
    """Create an executed notebook without modifying the input notebook.

    :param in_file: The name of the input Jupyter notebook file.
    :param kernel: The programming language used to execute the notebook.
    :param out_file: The name of the output Jupyter notebook file.
    """
    nb = nbexec(in_file, kernel) if kernel else nbexec(in_file)
    if out:
        nbformat.write(nb, out, version=4)
    else:
        sys.stdout.write(nbformat.writes(nb))
