# The `nbless` python package

Using `nbless` you can create and execute [Jupyter Notebooks](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html) in
- your terminal or
- your favorite Python environment (e.g. [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)).

The `nbless` python package consists of 5 functions:
- `nbuild`, which creates a notebook from python scripts and plain text files, e.g. markdown (`.md`) and text (`.txt`) files.
- `nbexec`, which runs a notebook from top to bottom and saves an executed version, leaving the source notebook untouched.
- `nbcode`, which converts a notebook into a code file. The extension is determined by the kernel. Markdown cells become comments.
- `nbless`, which calls `nbuild`, `nbcode`, and `nbexec` to create and execute a notebook.
- `nbhtml`, which converts a notebook into an HTML document.

All of the above function work for Python _and_ R code, with the caveat that nbexec and nbless require the kernel argument to be set to `ir` if R code files (`.R`) are included.

If you want to execute a Jupyter notebook that contains both R and Python code, you will have to put the R code in Python scripts (`.py`) and use [rpy2](https://rpy2.readthedocs.io/) with the default kernel (`python3`).

To run Rmd files that include R and Python code, you will need the `reticulate` R package.

The `nb` functions rely on the `nbconvert` and `nbformat` modules that are included with `jupyter`. The `catrmd` function has no dependencies beyond Python.

## Installation

```sh
pip install nbless
```

or clone the [repo](https://github.com/marskar/nbless), e.g. `git clone https://github.com/marskar/nbless` and either use locally, e.g. `python nbless.py README.md plot.py notes.txt` or install using setup.py, e.g. `python setup.py install`.

## Basic usage: terminal

### Creating a Jupyter notebook with `nbuild` in the terminal

```sh
nbuild README.md plot.py notes.txt
```  

The `nbuild` function takes the contents of Python code files (`.py`) stores them as [Jupyter Notebook code cells](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html). The contents of all other files are stored in [markdown cells](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html).

The default output filename for `nbuild` is `unexecuted.ipynb`. By default, input and output files are located in the current directory (`'./'`).

You can provide a more descriptive filename for the unexecuted notebook (`-u`) and set different input  (`-i`) and output  (`-o`) filepaths:

```sh
nbuild README.md plot.py notes.txt --input_path input_files --output_name raw.ipynb --output_path notebooks/
# Or
nbuild README.md plot.py notes.txt -i input_files -n raw.ipynb -o notebooks/
```

If you only want to execute a notebook, run `nbexec`.

### Executing a notebook with `nbexec` in the terminal


```sh
nbexec raw.ipynb
```

The `nbexec` creates a copy of the input notebook, runs it from top to bottom and saves it. The default name of the first notebook is `unexecuted.ipynb` while the executed notebook is called `executed.ipynb` by default. The default filepath where the notebooks are saved is the current directory (`'./'`).

The default output filename for `nbexec.py` is `executed.ipynb`.  By default, input and output files are located in the current directory (`'./'`).

You can provide a more descriptive filename for the executed notebook (`-e`) and set different input  (`-i`) and output  (`-o`) filepaths:


```sh
nbexec raw.ipynb --input_path input_files --output_name out.ipynb --output_path notebooks/
# Or
nbexec raw.ipynb -i input_files -n out.ipynb -o notebooks/
```

If you want to combine `nbuild` and `nbexec` in one step, use `nbless`.

### Creating and executing a Jupyter notebook with `nbless` in the terminal

Run `nbless` in your terminal, providing all of the names of the source files as arguments, e.g.

```sh
nbless README.md plot.py notes.txt
```

You can provide more descriptive names for the notebooks and set a different path:

```sh
nbless README.md plot.py notes.txt --input_path input_files --nbuild raw.ipynb --nbexec out.ipynb --nbcode code.py --output_path output_files/
# Or
nbless README.md plot.py notes.txt --i input_files -u raw.ipynb -e out.ipynb -c code.py -o output_files/
```  

If you do not want an executed version of the notebook, run `nbuild` instead of `nbless`.

### Creating an HTML file with `nbhtml` in the terminal

The `nbhtml` functions works like `nbcode`. Provide all of the source files as arguments, e.g.

```sh
 header.yml intro.md letters.R notes.txt plot.py
```

The default output filename for `catrmd` is `cat.Rmd`. By default, input and output files are located in the current directory (`'./'`).

You can provide a more descriptive filename for the unrendered Rmd (`-u`) and set different input  (`-i`) and output  (`-o`) filepaths:

```sh
catrmd header.yml intro.md letters.R notes.txt plot.py --unrendered raw.Rmd --output_path rmarkdown/
# Or
catrmd header.yml intro.md letters.R notes.txt plot.py -u raw.Rmd -o rmarkdown/
```


## Basic usage: python environment

```python
# You can import any or all of the functions from the nbless package.

# You can also import each function individually
from nbless import nbuild
from nbless import nbexec
from nbless import nbless
from nbless import nbcode

# The above imports all 4 functions
# This can also be done with either of the two lines below.
from nbless import nbuild, nbexec, nbless, nbcode
from nbless import *

# Another alternative is to import the package and use it as a namespace.
import nbless

#Use individually
nbuild(["README.md", "plot.py", "notes.txt"], output_path="notebooks/")
nbexec("notebooks/raw.ipynb", output_path="notebooks/")

# Or to run both nbuild and nbexec at once, use nbless
nbless(["README.md", "plot.py", "notes.txt"], nbexec_path="notebooks/")

# To make an Rmd file, use catrmd
catrmd(["header.yml", "intro.md", "letters.R", "plot.py", "notes.txt"], output_path="rmarkdown/")

# Use nbless as a namespace
nbless.nbuild(["README.md", "plot.py", "notes.txt"], output_path="notebooks/")
nbless.nbexec("notebooks/raw.ipynb", output_path="notebooks/")
nbless.nbless(["README.md", "plot.py", "notes.txt"], nbexec_path="notebooks/")
nbless.catrmd(["header.yml", "intro.md", "letters.R", "plot.py", "notes.txt"], output_path="rmarkdown/")
```

You can also run the `nbless` functions in an R environment using the `reticulate` R package.

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
