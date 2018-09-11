# The `nbless` python package

Using `nbless` you can create and execute Jupyter notebooks in
- your terminal or
- your favorite Python environment (e.g. PyCharm or Visual Studio Code).

The `nbless` python package consists of 3 functions:
- `nbuild`, which creates a notebook from python scripts and plain text files, e.g. markdown (`.md`) and text (`.txt`) files.
- `nbexec`, which runs a notebook from top to bottom and saves an executed version, leaving the source notebook untouched.
- `nbless`, which calls `nbuild` and `nbexec` to create and execute a notebook.

These functions rely on the `nbconvert` and `nbformat` modules that are included with `jupyter`.

## Basic usage: terminal

### Creating and executing a notebook with `nbless` in the terminal

Run `nbless.py` script in your terminal, providing all of the names of the source files as arguments, e.g.

```sh
python nbless.py README.md plot.py notes.txt
```

First, the contents of Python code files (`.py`) are stored as Jupyter notebook code cells, while the contents of all other files are stored in markdown cells.

Then, the newly created notebook is copied, run from top to bottom and saved. The default name of the first notebook is `raw.ipynb` while the executed notebook is called `out.ipynb` by default output. The default filepath where the notebooks are saved is the current directory (`'./'`).

You can provide more descriptive names for the notebooks and set a different path:

```sh
python nbless.py README.md plot.py notes.txt --raw unexecuted --out executed.ipynb --path notebooks/
# Or
python nbless.py README.md plot.py notes.txt -r not_executed.ipynb -o executed.ipynb -p notebooks/
```  

### Creating a notebook with `nbuild` in the terminal

If you do not want an executed version of the notebook, run `nbuild.py` instead of `nbless.py`.

```sh
python nbuild.py README.md plot.py notes.txt
```  

The default output filename for `nbuild` is `raw.ipynb`. The default output filepath is the current directory (`'./'`).

You can provide a more descriptive filename (`-o`) and set a different path (`-p`):

```sh
python nbuild.py README.md plot.py -o not_executed.ipynb -p notebooks/
# Or
python nbuild.py README.md plot.py --out not_executed.ipynb --path notebooks/
```  

If you only want to execute a notebook, run `nbexec.py`.

```sh
python nbexec.py raw.ipynb
```

The default output filename for `nbexec.py` is `out.ipynb`. The default output filepath is the current directory (`'.'`).

You can provide more descriptive names for the output name (`-o`) and path (`-p`):

```sh
python nbexec.py raw.ipynb -o executed.ipynb -p notebooks/
# Or
python nbexec.py raw.ipynb --out executed.ipynb --path notebooks/
```

## Basic usage: python environment

```python
from nbuild import nbuild
from nbexec import nbexec
from nbless import nbless

nbuild(["README.md", "plot.py", "notes.txt"], output_path="notebooks/")
nbexec("notebooks/raw.ipynb", output_path="notebooks/")

# Or to run both nbuild and nbexec at once, use nbless
nbless(["README.md", "plot.py", "notes.txt"], nbexec_path="notebooks/")
```

### Missing a dependency?

If you installed [Anaconda](https://www.anaconda.com/download/), you should already have all of the dependencies (`python`, `nbformat`, and `nbconvert`).

If not, or if you have [Miniconda](https://conda.io/miniconda.html) installed, run

```sh
conda install -yc conda-forge jupyter
```

If you have any other Python installation, run

```sh
pip install jupyter
```

## Too many file names to type out?

You can use the `ls` command to assign all of the relevant names in the current directory to a variable and pass this variable as an argument to `nbconvert.py`.

To preserve the order and differentiate files that should be incorporated into the notebook, I recommend left padding your file names with zeros (e.g. 01_intro.md, 02_figure1.py).

Consider the example below:

```sh
touch {01..09}.py
name_list=`ls 0*.py`
python nbuild.py `echo $name_list`
```

In a python environment, I recommend `os.listdir` to obtain a list of all files:
```python
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
```