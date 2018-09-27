#!/usr/bin/env python
import nbformat
from typing import List
from argparse import ArgumentParser


def nbuild(filenames: List[str],
           input_path: str = './',
           output_name: str = "unexecuted.ipynb",
           output_path: str = './') -> None:

    def read_file(filename):
        with open(filename) as f:
            return f.read()

    nb = nbformat.v4.new_notebook()
    md_cell = nbformat.v4.new_markdown_cell
    code_cell = nbformat.v4.new_code_cell

    if not input_path.endswith('/'):
        input_path += '/'

    nb['cells'] = [code_cell(read_file(input_path+name))
                   if name.endswith(('.py', '.R'))
                   else md_cell(read_file(input_path+name))
                   for name in filenames]

    if not output_path.endswith('/'):
        output_path += '/'

    with open(output_path+output_name, 'wt') as f:
        nbformat.write(nb, f)


def command_line_runner():

    parser = ArgumentParser(
        description='Create a notebook from the command line.')

    parser.add_argument('names', nargs='+', help='A series of filenames.')

    parser.add_argument('--input_path', '-i', default='./',
                        help='The filepath to the source files.')

    parser.add_argument('--output_name', '-n', default='unexecuted.ipynb',
                        help='The filename of the unexecuted output notebook.')

    parser.add_argument('--output_path', '-o', default='./',
                        help='The filepath where the output notebook is saved.')

    args = parser.parse_args()
    names = args.names
    in_path = args.input_path
    out_name = args.output_name
    out_path = args.output_path

    nbuild(filenames=names,
           input_path=in_path,
           output_name=out_name,
           output_path=out_path)


if __name__ == "__main__":
    command_line_runner()
