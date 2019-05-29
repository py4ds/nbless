Nbless: a Python package for programmatic Jupyter notebook workflows
====================================================================

|Build| |License| |PyPI| |Status| |Updates| |Versions|

Introduction
------------

The ``nbless`` Python package allows you to (de)construct, convert, and execute `Jupyter
Notebooks <http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html>`__
in

- your terminal (e.g. ``bash``, ``zsh``, ``fish``, etc.) or
- your favorite Python environment (e.g. `PyCharm <https://www.jetbrains.com/pycharm/>`__ or `Visual Studio Code <https://code.visualstudio.com/docs/python/python-tutorial>`__).

The ``nbless`` Python package consists of 6 Python functions and shell commands:

- ``nbconv``, which converts a notebook into various formats.
- ``nbdeck``, which prepares a notebook to be viewed as or converted into slides.
- ``nbexec``, which runs a notebook from top to bottom and saves an executed version.
- ``nbless``, which calls ``nbuild`` and ``nbexec`` to create and execute a notebook.
- ``nbraze``, which extracts code and markdown files from a notebook.
- ``nbuild``, which creates a notebook from source files, e.g. Python (`.py`) and R (`.R`) scripts, markdown (``.md``), and text (``.txt``) files.

For a related package that provides programmatic tools for working with `R Markdown <https://rmarkdown.rstudio.com/authoring_quick_tour.html>`__ (Rmd) files,
check out the `Rmdawn Python package <https://marskar.github.io/rmdawn/>`__.

Documentation and code
----------------------

The documentation is hosted at https://marskar.github.io/nbless/.

The code is hosted at https://github.com/marskar/nbless.

Installation
------------

.. code:: sh

    pip install nbless

or clone the `repo <https://github.com/marskar/nbless>`__, e.g.
``git clone https://github.com/marskar/nbless`` and install locally
using setup.py (``python setup.py install``) or ``pip``
(``pip install .``).

R and Python interoperability
-----------------------------

All of the Nbless functions and commands work for Python *and* R code, with the caveat
that ``nbexec`` and ``nbless`` require the kernel argument to be set to
``ir`` if R code files (``.R``) are included.

If you want to execute a Jupyter notebook that contains both R and
Python code, you will have to put the R code in Python scripts (``.py``)
and use the `rpy2 <https://rpy2.readthedocs.io/>`__ Python library with the default kernel
(``python3``).

Code files extracted from code cells with ``nbraze`` must all have the same extension (e.g. `.py`).
The ``language_info`` key is not always defined, so ``nbraze`` does not try to infer the programming language from Jupyter notebook metadata.

You can also run the Nbless functions in an R environment using the
`reticulate <https://rstudio.github.io/reticulate/>`__ R package.

All Nbless functions and commands rely on the `nbconvert <https://nbconvert.readthedocs.io/>`__ and `nbformat <http://nbformat.readthedocs.io/>`__ modules that are included with the ``jupyter`` Python library.
The command line interface relies on the `click <https://click.palletsprojects.com/>`__ Python library.

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

You can preview the raw notebook output by running ``nbuild`` with only the positional arguments:

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

Extracting source files from a Jupyter notebook with ``nbraze`` in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    nbraze notebook.ipynb

The ``nbraze`` function takes the contents of `Jupyter Notebook code cells <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html>`__ and turns them into Python or R code files (``.py`` or ``.R``).
The contents of `markdown cells <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html>`__ are turned into markdown files.

Converting Jupyter notebooks with ``nbconv`` in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Creating HTML slides with ``nbdeck`` and ``nbconv`` in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With ``nbdeck``, you can prepare Jupyter slides from source files (e.g. ``source_file1.md``, ``source_file2.py``) like this:

.. code:: sh

    nbless slide_file* -o slides.ipynb
    nbdeck slides.ipynb -o slides.ipynb
    nbconv slides.ipynb  -e slides -o slides.html


Basic usage: Python environment
-------------------------------

.. code:: python

    import nbformat

    # You can import any or all of the functions from the nbless package.

    # You can also import each function individually
    from nbless import nbuild
    from nbless import nbexec
    from nbless import nbless
    from nbless import nbconv
    from nbless import nbdeck
    from nbless import nbraze

    # The above imports all 6 functions
    # This can also be done with either of the two lines below.
    from nbless import nbuild, nbexec, nbless, nbconv, nbdeck, nbraze
    from nbless import *

    # Simple individual usage

    # Create notebook.ipynb in notebooks folder from plot.py and notes.txt
    # nbuild() returns a notebook object
    nbformat.write(nbuild(["plot.py", "notes.txt"]), "notebook.ipynb", version=4)

    # Create source files from notebook.ipynb in notebooks folder
    # nbraze() returns None, instead it creates markdown and code files
	nbraze("notebook.ipynb")
    # The default code file for nbraze is Python
	nbraze("notebook.ipynb", extension="py")
    # It is also possible to create R files
	nbraze("notebook.ipynb", extension="R")
    # nbraze() cannot handle notebooks with a mix of different languages

    # Create notebook_executed.ipynb from notebook.ipynb
    # nbexec() returns a notebook object
    nbformat.write(nbexec("notebook.ipynb"), "notebook.ipynb", version=4)

    # Or to run both nbuild and nbexec at once, use nbless
    # nbless() returns a notebook object
    nbformat.write(nbless(["plot.py", "notes.txt"]), "notebook.ipynb", version=4)

    # Create notebook.py from notebook.ipynb in notebooks folder
    # nbconv() returns a filename and file contents as strings
    def write_file(filename: str, contents: str) -> None:
        with open(filename, 'w') as f:
            f.write(contents)

    filename, contents = nbconv("notebooks/notebook.ipynb")
    write_file(filename, contents)
    write_file(*nbconv("notebooks/notebook.ipynb"))

    # Create notebook.html from notebook.ipynb in notebooks folder
    write_file(*nbconv("notebooks/notebook.ipynb", "html"))

    # Create script.py from notebook.ipynb in notebooks folder
    write_file('script.py', nbconv("notebooks/notebook.ipynb")[1])

    # Create report.html from notebook.ipynb in notebooks folder
    write_file('report.html', nbconv("notebooks/notebook.ipynb", 'html')[1])

    # Create HTML slides from notebook.ipynb in notebooks folder
    # nbdeck() returns a filename and file contents as strings
    nbformat.write(nbdeck("notebook.ipynb"), "slides.ipynb", version=4)
    filename, contents = nbconv("slides.ipynb", "slides")
    write_file(filename, contents)
    write_file(*nbconv("notebooks/notebook.ipynb", "slides"))

    # Another alternative is to import the package and use it as a namespace.
    import nbless

    # Use nbless as a namespace
    nbformat.write("notebook.ipynb", nbless.nbuild(["plot.py", "notes.txt"]), version=4)
    nbformat.write(*nbless.nbexec("notebook.ipynb"), version=4)
    nbformat.write('executed.ipynb', nbless.nbexec("notebook.ipynb")[1], version=4)
    nbformat.write("executed.ipynb", nbless.nbless(["plot.py", "notes.txt"]), version=4)
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

The easiest way to handle large numbers of files is to use the ``*`` wildcard in the shell.

.. code:: sh

    nbuild source_file* -o notebook.ipynb

You can use the ``ls`` command to assign all of the relevant names in
the current directory to a variable and pass this variable as an
argument to ``nbconvert.py``.

Consider the example below:

.. code:: sh

    touch {01..09}.py
    name_list=`ls 0*.py`
    python nbuild.py `echo $name_list`

In Python environments, ``os.listdir`` can provide a list of
all files:

.. code:: python

    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

To preserve the order and differentiate files that should be
incorporated into the notebook, it may be helpful to left pad file names
with zeros (e.g. ``01\_intro.md``, ``02\_figure1.R``).
This works well for R scripts, but Python files that start with numbers cannot be imported.

Related projects
----------------

- `pandoc <https://pandoc.org/MANUAL.html#creating-jupyter-notebooks-with-pandoc>`__
- `jupytext <https://github.com/mwouts/jupytext>`__
- `notedown <https://github.com/aaren/notedown>`__

Next Steps
----------

Currently, notebook metadata is lost when using ``nbraze``/``nbuild``/``nbless``.

- Enable ``nbuild``/``nbless`` to accept metadata via a ``metadata.json`` file.
- Enable ``nbraze`` to output metadata via a ``metadata.json`` file.

.. |Build| image:: https://travis-ci.org/marskar/nbless.svg?branch=master
   :target: https://travis-ci.org/marskar/nbless
.. |License| image:: https://img.shields.io/badge/License-MIT-brightgreen.svg
   :target: https://opensource.org/licenses/MIT
.. |PyPI| image:: https://img.shields.io/pypi/v/nbless.svg
   :target: https://pypi.python.org/pypi/nbless
.. |Status| image:: https://www.repostatus.org/badges/latest/active.svg
   :alt: Project Status: Active – The project has reached a stable, usable state and is being actively developed.
   :target: https://www.repostatus.org/#active
.. |Updates| image:: https://pyup.io/repos/github/marskar/nbless/shield.svg
   :target: https://pyup.io/repos/github/marskar/nbless/
.. |Versions| image:: https://img.shields.io/pypi/pyversions/nbless.svg
   :alt: PyPI - Python Version
   :target: https://www.python.org/downloads/
