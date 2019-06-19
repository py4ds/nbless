import click

from nbless.nbraze import nbraze


@click.command()
@click.argument("in_file", required=True, type=click.Path(exists=True))
@click.option("-e", "--extension", "extension", default="py")
def nbraze_cli(in_file: str, extension: str) -> None:
    """Create markdown and code files from a Jupyter notebook.

    :param in_file: The name of the input Jupyter notebook file.
    :param extension: The extension for code files.
    """
    name_source_dict = nbraze(in_file, extension)
    for name, source in name_source_dict.items():
        with open(name, "w") as file:
            file.write(source)
        print(f"Saved {name}")
