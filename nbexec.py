#!/usr/bin/env python
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def nbexec(input_name: str,
           output_name: str = 'executed.ipynb',
           output_path: str = './',
           kernel_name: str = 'python3') -> None:

    with open(input_name) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(kernel_name=kernel_name)

    ep.preprocess(nb, {'metadata': {'path': output_path}})

    if not output_path.endswith('/'):
        output_path += '/'

    with open(output_path+output_name, 'wt') as f:
        nbformat.write(nb, f)


def command_line_runner():
    import argparse
    parser = argparse.ArgumentParser(
        description='Execute a notebook from the command line.')

    parser.add_argument('source', help='The filename of the input notebook.')

    parser.add_argument('--executed', '-e', default='out.ipynb',
                        help='The filename of the executed output notebook.')

    parser.add_argument('--path', '-p', default='.',
                        help='The filepath where the output notebook is saved.')

    parser.add_argument('--kernel', '-k', default='python3',
                        help='The Jupyter kernel used to execute the notebook')

    args = parser.parse_args()
    in_name = args.source
    out_name = args.executed
    out_path = args.path
    kernel = args.kernel

    nbexec(input_name=in_name,
           output_name=out_name,
           output_path=out_path,
           kernel_name=kernel)


if __name__ == "__main__":
    command_line_runner()
