import click

from nbless.nbdeck import nbdeck
from nbless.nbsave import nbsave


@click.command()
@click.argument("in_file")
@click.option("-o", "--out_file", "out")
def nbdeck_click(in_file: str, out: str) -> None:
    """Set up a notebook to be viewed as or converted into slides."""
    nbsave(out, nbdeck(in_file)) if out else nbsave(in_file, nbdeck(in_file))
