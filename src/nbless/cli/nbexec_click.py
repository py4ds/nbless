import click

from nbless import nbexec, nbsave


@click.command()
@click.argument('in_file')
@click.option('-o', '--out_file', 'out_file')
def nbexec_click(in_file: str, out_file: str) -> None:
    nb_name, nb = nbexec.nbexec(in_file)
    nbsave.nbsave(out_file, nb) if out_file else nbsave.nbsave(nb_name, nb)
