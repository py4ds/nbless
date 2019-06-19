import sys

import click
import nbformat

from nbless.nbdeck import nbdeck


@click.command()
@click.argument("in_file")
@click.option("-o", "--out_file", "out_file")
def nbdeck_cli(in_file: str, out_file: str) -> None:
    """Set up a notebook to be viewed as or converted into slides.

    :param in_file: The name of the input Jupyter notebook file.
    :param out_file: The name of the output Jupyter notebook file.
    """
    nb = nbdeck(in_file)
    if out_file:
        nbformat.write(nb, out_file, version=4)
    else:
        sys.stdout.write(nbformat.writes(nb))
