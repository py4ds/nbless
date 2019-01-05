Nbless: a Python package for programmatic Jupyter notebook workflows
====================================================================

Using ``nbless`` you can create and execute `Jupyter
Notebooks <http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html>`__
in

- your terminal or
- your favorite Python environment (e.g. `PyCharm <https://www.jetbrains.com/pycharm/>`__ or `Visual Studio Code <https://code.visualstudio.com/docs/python/python-tutorial>`__).

The ``nbless`` python package consists of 6 functions:

- ``nbuild``, which creates a notebook from python scripts and plain text files, e.g. markdown (``.md``) and text (``.txt``) files.
- ``nbexec``, which runs a notebook from top to bottom and saves an executed version, leaving the source notebook untouched.
- ``nbconv``, which converts a notebook into various formats.
- ``nbless``, which calls ``nbuild`` and ``nbexec`` to create and execute a notebook.
- ``nbsave``, which saves notebook objects as files (Python only, no command line interface)
- ``nbread``, which reads in notebook objects from files (Python only, no command line interface)

All of the above function work for Python *and* R code, with the caveat
that ``nbexec`` and ``nbless`` require the kernel argument to be set to
``ir`` if R code files (``.R``) are included.

If you want to execute a Jupyter notebook that contains both R and
Python code, you will have to put the R code in Python scripts (``.py``)
and use `rpy2 <https://rpy2.readthedocs.io/>`__ with the default kernel
(``python3``).

You can also run the ``nbless`` functions in an R environment using the
``reticulate`` R package.

The ``nb`` functions rely on the ``nbconvert`` and ``nbformat`` modules
that are included with ``jupyter``.

The command line interface relies on the ``click`` library.

Installation
------------

.. code:: sh

    pip install nbless

or clone the `repo <https://github.com/marskar/nbless>`__, e.g.
``git clone https://github.com/marskar/nbless`` and either use locally,
e.g. ``python nbless.py README.md plot.py notes.txt`` or install locally
using setup.py (``python setup.py install``) or ``pip``
(``pip install .``)

Basic usage: terminal
---------------------

Creating a Jupyter notebook with ``nbuild`` in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    nbuild README.md plot.py notes.txt > notebooks/notebook.ipynb

The ``nbuild`` function takes the contents of Python or R code files
(``.py`` or ``.R``) and stores them as `Jupyter Notebook code
cells <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html>`__.
The contents of all other files are stored in `markdown
cells <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html>`__.

Instead of redirecting to a file (``>``), you can use the ``--out_file``
or ``-o`` flag:

.. code:: sh

    nbuild README.md plot.py notes.txt --out_file notebooks/notebook.ipynb
    # Or
    nbuild README.md plot.py notes.txt -o notebooks/notebook.ipynb

You can preview the raw notebook output by running nbuild with only the positional arguments:

.. code:: sh

    nbuild README.md plot.py notes.txt

If you only want to execute a notebook, run ``nbexec`` as described below.

Executing a notebook with ``nbexec`` in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    nbexec notebook.ipynb

The ``nbexec`` command creates a copy of the input notebook, runs it
from top to bottom and saves it. If an ``out_file`` name is not
provided, the new filename will be the original filename with
``_executed.ipynb`` appended to it.

You can provide a more descriptive name for the executed output (``-o``)
notebook:

.. code:: sh

    nbexec notebook.ipynb --out_file executed.ipynb
    # Or
    nbexec notebook.ipynb -o executed.ipynb

You can preview the default output filename and the raw notebook output by running nbexec with only the positional arguments:

.. code:: sh

    nbexec notebook.ipynb

If you want to combine ``nbuild`` and ``nbexec`` in one step, use
``nbless`` as described below.

Creating and executing a Jupyter notebook with ``nbless`` in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run ``nbless`` in your terminal, providing all of the names of the
source files as arguments, e.g.

.. code:: sh

    nbless README.md plot.py notes.txt > output/executed.ipynb

The default name of the first notebook is ``unexecuted.ipynb`` while the
executed notebook is called ``executed.ipynb`` by default.

Instead of redirecting to a file (``>``), you can use the ``--out_file``
or ``-o`` flag:

.. code:: sh

    nbless README.md plot.py notes.txt --out_file output/executed.ipynb
    # Or
    nbless README.md plot.py notes.txt -o output/executed.ipynb

If you do not want an executed version of the notebook, run ``nbuild``
instead of ``nbless``.

Creating a code file with ``nbconv`` in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    nbconv notebook.ipynb

The ``nbconv`` command by default created a python script by extracting
the content from code cells and discarding all output and markdown
content.

In the example above, the output file would be ``notebook.py``, but it
is possible to specify a different filename:

.. code:: sh

    nbconv notebook.ipynb --out_file script.py
    # Or
    nbconv notebook.ipynb -o script.py

You can preview the default output filename and the raw notebook output by running nbconv with only the positional arguments:

.. code:: sh

    nbconv notebook.ipynb


Creating an HTML file with ``nbconv`` in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example below is similar to creating a python script, except it
creates an HTML document, which includes output and the content of
markdown and code cells.

.. code:: sh

    nbconv notebook.ipynb -e html

You can provide a more descriptive name for the output file with the
``--out_file`` or ``-o`` flag:

.. code:: sh

    nbconv notebook.ipynb --out_file report.html
    # Or
    nbconv notebook.ipynb -o report.html

Basic usage: Python environment
-------------------------------

.. code:: python

    # You can import any or all of the functions from the nbless package.

    # You can also import each function individually
    from nbless import nbuild
    from nbless import nbexec
    from nbless import nbless
    from nbless import nbconv
    from nbless import nbsave
    from nbless import nbread

    # The above imports all 6 functions
    # This can also be done with either of the two lines below.
    from nbless import nbuild, nbexec, nbless, nbconv, nbsave, nbread
    from nbless import *

    # Simple individual usage

    # Create notebook.ipynb in notebooks folder from plot.py and notes.txt
    nbsave("notebooks/notebook.ipynb", nbuild(["plot.py", "notes.txt"]))

    # nbexec returns a filename string and a notebook object
    nb_name, nb = nbexec("notebooks/notebook.ipynb")
    nbsave(nb_name, nb)

    # Create notebook_executed.ipynb from notebook.ipynb
    nbsave(*nbexec("notebooks/notebook.ipynb"))

    # Create executed.ipynb from notebook.ipynb in notebooks folder
    nbsave('executed.ipynb', nbexec("notebooks/notebook.ipynb")[1])

    # Or to run both nbuild and nbexec at once, use nbless
    nbsave("output/executed.ipynb", nbless(["plot.py", "notes.txt"]))

    def write_file(filename: str, contents: str) -> None:
        with open(filename, 'w') as f:
            f.write(contents)

    # nbconv returns a filename and file contents as strings
    filename, contents = nbconv("notebooks/notebook.ipynb")
    write_file(filename, contents)

    # Create notebook.py from notebook.ipynb in notebooks folder
    write_file(*nbconv("notebooks/notebook.ipynb"))

    # Create notebook.html from notebook.ipynb in notebooks folder
    write_file(*nbconv("notebooks/notebook.ipynb", "html"))

    # Create script.py from notebook.ipynb in notebooks folder
    write_file('script.py', nbconv("notebooks/notebook.ipynb")[1])

    # Create report.html from notebook.ipynb in notebooks folder
    write_file('report.html', nbconv("notebooks/notebook.ipynb", 'html')[1])

    # Another alternative is to import the package and use it as a namespace.
    import nbless

    # Use nbless as a namespace
    nbsave("notebook.ipynb", nbless.nbuild(["plot.py", "notes.txt"]))
    nbsave(*nbless.nbexec("notebook.ipynb"))
    nbsave('executed.ipynb', nbless.nbexec("notebook.ipynb")[1])
    nbsave("executed.ipynb", nbless.nbless(["plot.py", "notes.txt"]))
    write_file(*nbless.nbconv("notebook.ipynb"))
    write_file(*nbless.nbconv("notebook.ipynb", "html"))
    write_file('script.py', nbless.nbconv("notebook.ipynb")[1])
    write_file('report.html', nbless.nbconv("notebook.ipynb", 'html')[1])

Missing a dependency?
~~~~~~~~~~~~~~~~~~~~~

If you installed via ``pip`` or ``setup.py``, you should have both of
the dependencies (``click`` and ``jupyter``) already. If not, try pip
installing them separately.

.. code:: sh

    pip install jupyter click

Or if you have `Anaconda <https://www.anaconda.com/download/>`__ or
`Miniconda <https://conda.io/miniconda.html>`__ installed, you can run

.. code:: sh

    conda install -yc conda-forge jupyter click

Too many file names to type out?
--------------------------------

You can use the ``ls`` command to assign all of the relevant names in
the current directory to a variable and pass this variable as an
argument to ``nbconvert.py``.

To preserve the order and differentiate files that should be
incorporated into the notebook, I recommend left padding your file names
with zeros (e.g. 01\_intro.md, 02\_figure1.py).

Consider the example below:

.. code:: sh

    touch {01..09}.py
    name_list=`ls 0*.py`
    python nbuild.py `echo $name_list`

In a python environment, I recommend ``os.listdir`` to obtain a list of
all files:

.. code:: python

    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
