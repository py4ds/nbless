#!/usr/bin/env python
from typing import List
from nbuild import nbuild
from nbexec import nbexec


def nbless(filenames: List,
           nbuild_name: str = 'raw.ipynb',
           nbuild_path: str = './',
           nbexec_name: str = 'out.ipynb',
           nbexec_path: str = './') -> None:

    nbuild(filenames=filenames,
           output_name=nbuild_name,
           output_path=nbuild_path)

    print(f"Created {nbuild_name} in {nbuild_path}")

    if not nbuild_path.endswith('/'):
        nbuild_path += '/'

    nbexec(input_name=nbuild_path+nbuild_name,
           output_name=nbexec_name,
           output_path=nbexec_path)

    print(f"Created {nbexec_name} in {nbexec_path}")


def command_line_runner():

    import argparse

    parser = argparse.ArgumentParser(
          description='Create and execute a notebook from the command line.')

    parser.add_argument('names', nargs='+', help='A series of filenames.')

    parser.add_argument('--raw', '-r', default='raw.ipynb',
                        help='The filename of the unexecuted output notebook.')

    parser.add_argument('--out', '-o', default='out.ipynb',
                        help='The filename of the executed output notebook.')

    parser.add_argument('--path', '-p', default='./',
                        help='The path where the notebooks will be saved.')

    args = parser.parse_args()
    names = args.names
    raw_name = args.raw
    out_name = args.out
    out_path = args.path

    nbless(names,
           nbuild_path=out_path,
           nbuild_name=raw_name,
           nbexec_name=out_name,
           nbexec_path=out_path)


if __name__ == "__main__":
    command_line_runner()
