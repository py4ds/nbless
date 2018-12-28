#!/usr/bin/env python
from nbconvert.exporters import ScriptExporter
from argparse import ArgumentParser
from typing import Optional
from os.path import splitext


def nbcode(input_name: str,
           input_path: str = './',
           output_name: Optional[str] = None,
           output_path: str = './') -> None:

    if not input_path.endswith('/'):
        input_path += '/'

    se = ScriptExporter()
    base, ext = splitext(input_path+input_name)
    script, resources = se.from_filename(input_path+input_name)

    if output_name is None:
        script_fname = base + resources.get('output_extension', '.txt')
        with open(output_path+script_fname, 'wt') as f:
            f.write(script)

    else:
        if not output_path.endswith('/'):
            output_path += '/'
        with open(output_path+output_name, 'wt') as f:
            f.write(script)


def command_line_runner():

    parser = ArgumentParser(
        description='Convert a notebook into code from the command line.')

    parser.add_argument('input_name', help='The filename of the input notebook.')

    parser.add_argument('--input_path', '-i', default='./',
                        help='The filepath to the input notebook.')

    parser.add_argument('--output_name', '-n', default=None,
                        help='The filename of the output code file.')

    parser.add_argument('--output_path', '-o', default='./',
                        help='The filepath where the output file is saved.')


    args = parser.parse_args()
    in_name = args.input_name
    in_path = args.input_path
    out_name = args.output_name
    out_path = args.output_path

    nbcode(input_name=in_name,
           input_path=in_path,
           output_name=out_name,
           output_path=out_path)


if __name__ == "__main__":
    command_line_runner()
