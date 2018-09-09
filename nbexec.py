import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def nbexec(input_name: str,
           output_name: str = 'out.ipynb',
           output_path: str = './') -> None:

    with open(input_name) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor()

    ep.preprocess(nb, {'metadata': {'path': output_path}})

    if not output_path.endswith('/'):
        output_path += '/'

    with open(output_path+output_name, 'wt') as f:
        nbformat.write(nb, f)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='Execute a notebook from the command line.')

    parser.add_argument('source', help='The filename of the input notebook.')

    parser.add_argument('--out', '-o', default='out.ipynb',
                        help='The filename of the output notebook.')

    parser.add_argument('--path', '-p', default='.',
                        help='The filepath where the output notebook is saved.')

    args = parser.parse_args()
    in_name = args.source
    out_name = args.out
    out_path = args.path

    nbexec(input_name=in_name,
           output_name=out_name,
           output_path=out_path)
