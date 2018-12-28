#!/usr/bin/env python
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from argparse import ArgumentParser
#from typing import Optional
#from os.path import splitext



def nbexec(input_name: str,
           input_path: str = './',
           output_name: str = 'executed.ipynb',
           output_path: str = './',
           kernel_name: str = 'python3') -> None:

    if not input_path.endswith('/'):
        input_path += '/'

    with open(input_path+input_name) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name=kernel_name)

    ep.preprocess(nb, {'metadata': {'path': output_path}})

    if not output_path.endswith('/'):
        output_path += '/'

    with open(output_path+output_name, 'wt') as f:
        nbformat.write(nb, f)


def command_line_runner():

    parser = ArgumentParser(
        description='Execute a notebook from the command line.')

    parser.add_argument('input_name', help='The filename of the input notebook.')

    parser.add_argument('--input_path', '-i', default='./',
                        help='The filepath to the input notebook.')

    parser.add_argument('--output_name', '-n', default='executed.ipynb',
                        help='The filename of the executed output notebook.')

    parser.add_argument('--output_path', '-o', default='./',
                        help='The filepath where the output notebook is saved.')

    parser.add_argument('--kernel', '-k', default='python3',
                        help='The Jupyter kernel used to execute the notebook.')

    args = parser.parse_args()
    in_name = args.input_name
    in_path = args.input_path
    out_name = args.output_name
    out_path = args.output_path
    kernel = args.kernel

    nbexec(input_name=in_name,
           input_path=in_path,
           output_name=out_name,
           output_path=out_path,
           kernel_name=kernel)


if __name__ == "__main__":
    command_line_runner()
