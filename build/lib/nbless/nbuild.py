import nbformat
from typing import List


def nbuild(filenames: List,
           output_name: str = "raw.ipynb",
           output_path: str = './') -> None:

    def read_file(filename):
        with open(filename) as f:
            return f.read()

    nb = nbformat.v4.new_notebook()
    md_cell = nbformat.v4.new_markdown_cell
    code_cell = nbformat.v4.new_code_cell

    nb['cells'] = [code_cell(read_file(name))
                   if name.endswith('.py')
                   else md_cell(read_file(name))
                   for name in filenames]

    if not output_path.endswith('/'):
        output_path += '/'

    nbformat.write(nb, output_path+output_name)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Create a notebook from the command line.')

    parser.add_argument('names', nargs='+', help='A series of filenames.')

    parser.add_argument('--out', '-o', default='raw.ipynb',
                        help='The filename of the output notebook.')

    parser.add_argument('--path', '-p', default='./',
                        help='The path where the output notebook is saved.')

    args = parser.parse_args()
    names = args.names
    out_name = args.out
    out_path = args.path

    nbuild(filenames=names,
           output_name=out_name,
           output_path=out_path)
