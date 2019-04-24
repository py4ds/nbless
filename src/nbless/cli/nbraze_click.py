import click

from nbless.main import nbraze


@click.command()
@click.argument("in_file", required=True,
                type=click.Path(exists=True))
@click.option("-e", "--extension", "ext", default="py")
def nbraze_click(in_file: str, ext: str) -> None:
    """Create markdown and code files from a Jupyter notebook."""
    name_source_dict = nbraze.nbraze(in_file, ext)
    for name, source in name_source_dict.items():
        with open(name, 'w') as file:
            file.write(source)
        print(f"Saved {name}")
