import sys
from typing import List

import click

from nbless import nbless, nbsave
import nbformat


@click.command()
@click.argument("in_files", nargs=-1)
@click.option("-o", "--out_file", "out_file")
def nbless_click(in_files: List[str], out: str) -> None:
    nb = nbless(in_files)
    nbsave(out, nb) if out else sys.stdout.write(nbformat.writes(nb))
