import argparse
import nbformat

parser = argparse.ArgumentParser(
    description='Create a notebook from the command line.')

parser.add_argument('names', nargs='+', help='A series of filenames.')

parser.add_argument('--out', '-o', default='raw.ipynb',
                    help='The filename of the output notebook.')

parser.add_argument('--path', '-p', default='./',
                    help='The filepath where the output notebook is saved.')

args = parser.parse_args()
filenames = args.names
output_filename = args.out
filepath = args.path

if not filepath.endswith('/'):
    filepath += '/'


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

nbformat.write(nb, filepath + output_filename)
