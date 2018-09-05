import nbformat as nbf


def read_file(filename):
    with open(filename) as f:
        return f.read()

readme = read_file('README.md')

plot = read_file('plot.py')

nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell(readme),
    nbf.v4.new_code_cell(plot)
]

nbf.write(nb, 'raw.ipynb')
