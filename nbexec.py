import argparse
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

parser = argparse.ArgumentParser(
    description='Execute a notebook from the command line.')

parser.add_argument('source', help='The filename of the input notebook.')

parser.add_argument('--out', '-o', default='output.ipynb',
                    help='The filename of the output notebook.')

parser.add_argument('--path', '-p', default='.',
                    help='The filepath where the output notebook is saved.')

args = parser.parse_args()
input_filename = args.source
output_filename = args.out
filepath = args.path

if not filepath.endswith('/'):
    filepath += '/'

with open(input_filename) as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor()

ep.preprocess(nb, {'metadata': {'path': filepath}})

with open(filepath + output_filename, 'wt') as f:
    nbformat.write(nb, f)