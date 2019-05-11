import click

from nbless.nbexec import nbexec
from nbless.nbsave import nbsave


@click.command()
@click.argument("in_file")
@click.option("-k", "--kernel", "kernel")
@click.option("-o", "--out_file", "out")
def nbexec_click(in_file: str, kernel: str, out: str) -> None:
    """Create an executed notebook without modifying the input notebook."""
    nb_name, nb = nbexec(in_file, kernel) if kernel else nbexec(in_file)
    nbsave(out, nb) if out else nbsave(nb_name, nb)
