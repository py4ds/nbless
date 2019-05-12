import sys
from typing import List

import click
import nbformat

from nbless.nbless import nbless


@click.command()
@click.argument("in_files", nargs=-1, required=True,
                type=click.Path(exists=True))
@click.option("-k", "--kernel", "kernel")
@click.option("-o", "--out_file", "out")
def nbless_click(in_files: List[str], kernel: str, out: str) -> None:
    """Create an executed Jupyter notebook from markdown and code files.

    :param in_files: The source files used to create a Jupyter notebook file.
    :param kernel: The programming language used to run the notebook.
    :param out_file: The name of the output Jupyter notebook file.
    """
    nb = nbless(in_files, kernel) if kernel else nbless(in_files)
    if out:
        nbformat.write(nb, out, version=4)
    else:
        sys.stdout.write(nbformat.writes(nb))
