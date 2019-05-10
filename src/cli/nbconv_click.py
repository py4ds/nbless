from pathlib import Path

import click

from nbless.nbconv import nbconv


@click.command()
@click.argument("in_file")
@click.option("-e", "--exporter", "exporter")
@click.option("-o", "--out_file", "out")
def nbconv_click(in_file: str, exporter: str, out: str) -> None:
    """Convert a notebook into various formats using ``nbformat`` exporters."""
    nb_name, nb = nbconv(in_file, exporter) if exporter else nbconv(in_file)
    Path(out).write_text(nb) if out else Path(nb_name).write_text(nb)
