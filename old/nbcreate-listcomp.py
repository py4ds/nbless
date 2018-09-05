import argparse
import nbformat as nbf

parser = argparse.ArgumentParser(
    description='',
)

parser.add_argument('filenames', metavar='N', type=str, nargs='+', )


def read_file(filename):
    with open(filename) as f:
        return f.read()


nb = nbf.v4.new_notebook()
md_cell = nbf.v4.new_markdown_cell
code_cell = nbf.v4.new_code_cell

nb['cells'] = [code_cell(read_file(name))
               if name.endswith('.py')
               else md_cell(read_file(name))
               for name in filenames]

nbf.write(nb, 'raw.ipynb')
