#!/usr/bin/env python
import nbformat
from typing import List
import argparse


def catrmd(filenames: List,
           output_name: str = "cat.Rmd",
           output_path: str = './') -> None:

    def read_file(filename):
        with open(filename) as f:
            return f.read()


    if not output_path.endswith('/'):
        output_path += '/'

    nbformat.write(nb, output_path+output_name)


def command_line_runner():

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


if __name__ == "__main__":
    command_line_runner()
