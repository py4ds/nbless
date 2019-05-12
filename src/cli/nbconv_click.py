from pathlib import Path

import click

from nbless.nbconv import nbconv


@click.command()
@click.argument("in_file")
@click.option("-e", "--exporter", "exporter")
@click.option("-o", "--out_file", "out")
def nbconv_click(in_file: str, exporter: str, out: str) -> None:
    """Convert a notebook into various formats using ``nbformat`` exporters.

    :param in_file: The name of the input Jupyter notebook file.
    :param exporter: The exporter that determines the output file type.
    :param out_file: The name of the output Jupyter notebook file.
    :note: The exporter type must be 'asciidoc', 'pdf', 'html', 'latex',
           'markdown', 'python', 'rst', 'script', or 'slides'.
           pdf requires latex, 'notebook' does nothing,
           slides need to served (not self-contained).
    """
    name, contents = nbconv(in_file, exporter) if exporter else nbconv(in_file)
    if out:
        Path(out).write_text(contents)
    else:
        Path(name).write_text(contents)
