import click

from nbless import nbconv

from nbless.helpers.write_file import write_file


@click.command()
@click.argument("in_file")
@click.option("-e", "--exporter", "exporter")
@click.option("-o", "--out_file", "out_file")
def nbconv_click(in_file: str, exporter: str, out: str) -> None:
    nb_name, nb = nbconv(in_file, exporter) if exporter else nbconv(in_file)
    write_file(out, nb) if out else write_file(nb_name, nb)
