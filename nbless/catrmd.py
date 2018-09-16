#!/usr/bin/env python
from typing import List
import argparse


def catrmd(filenames: List[str],
           input_path: str = './',
           output_name: str = "cat.Rmd",
           output_path: str = './') -> None:

    def read_file(filename):
        with open(filename) as f:
            return f.read()

    if not input_path.endswith('/'):
        input_path += '/'

    string_list = ['```{r}\n'+read_file(input_path+name)+'\n```'
                   if name.endswith('.R')
                   else '```{python}\n'+read_file(input_path+name)+'\n```'
                   if name.endswith('.py')
                   else read_file(input_path+name)
                   for name in filenames]

    if not output_path.endswith('/'):
        output_path += '/'

    with open(output_path+output_name, 'wt') as f:
        f.write('\n\n'.join(string_list))


def command_line_runner():

    parser = argparse.ArgumentParser(
        description='Create an R markdown file from the command line.')

    parser.add_argument('names', nargs='+', help='A series of filenames.')

    parser.add_argument('--input_path', '-i', default='./',
                        help='The filepath to the source files.')

    parser.add_argument('--unrendered', '-u', default='unrendered.Rmd',
                        help='The filename of the unrendered output Rmd file.')

    parser.add_argument('--output_path', '-o', default='./',
                        help='The filepath where the output Rmd file is saved.')

    args = parser.parse_args()
    names = args.names
    in_path = args.input_path
    out_name = args.unrendered
    out_path = args.output_path

    catrmd(filenames=names,
           input_path=in_path,
           output_name=out_name,
           output_path=out_path)


if __name__ == "__main__":
    command_line_runner()
