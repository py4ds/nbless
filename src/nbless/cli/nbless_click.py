import sys
from typing import List

import click

from nbless.main import nbless, nbsave
import nbformat


@click.command()
@click.argument("in_files", nargs=-1, required=True,
                type=click.Path(exists=True))
@click.option("-o", "--out_file", "out")
def nbless_click(in_files: List[str], out: str) -> None:
    """Create an executed Jupyter notebook from markdown and code files."""
    nb = nbless.nbless(in_files)
    nbsave.nbsave(out, nb) if out else sys.stdout.write(nbformat.writes(nb))
