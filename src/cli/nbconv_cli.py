from pathlib import Path

import click

from nbless.nbconv import nbconv


@click.command()
@click.argument("in_file")
@click.option("-e", "--exporter", "exporter")
@click.option("-o", "--out_file", "out_file")
def nbconv_cli(in_file: str, exporter: str, out_file: str) -> None:
    """Convert a notebook into various formats using ``nbformat`` exporters.

    :param in_file: The name of the input Jupyter notebook file.
    :param exporter: The exporter that determines the output file type.
    :param out_file: The name of the output Jupyter notebook file.
    :note: The exporter type must be 'asciidoc', 'pdf', 'html', 'latex',
           'markdown', 'python', 'rst', 'script', or 'slides'.
           All formats except 'HTML' require pandoc.
           Exporting to pdf requires latex.
    """
    name, contents = nbconv(in_file, exporter, out_file)
    Path(name).write_text(contents)
