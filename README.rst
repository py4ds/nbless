Nbless: a Python package for programmatic Jupyter notebook workflows
====================================================================


|Build| |Chat| |Coverage| |License| |PyPI| |Python versions| |PyUp| |Repo status|

Introduction
------------

The ``nbless`` Python package allows you to (de)construct, convert, and execute `Jupyter
Notebooks <http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html>`__
in

- your terminal (e.g. ``bash``, ``zsh``, ``fish``, etc.) or
- your favorite Python environment (e.g. `PyCharm <https://www.jetbrains.com/pycharm/>`__ or `Visual Studio Code <https://code.visualstudio.com/docs/python/python-tutorial>`__).

The ``nbless`` Python package consists of 6 Python functions and shell commands:

- nbconv_, which converts a notebook into various formats.
- nbdeck_, which prepares a notebook to be viewed as or converted into slides.
- nbexec_, which runs a notebook from top to bottom and saves an executed version.
- nbless_, which calls ``nbuild`` and ``nbexec`` to create and execute a notebook.
- nbraze_, which extracts code and markdown files from a notebook.
- nbuild_, which creates a notebook from source files, e.g. Python (`.py`) and R (`.R`) scripts, markdown (``.md``), and text (``.txt``) files.

For a related package that provides programmatic tools for working with `R Markdown <https://rmarkdown.rstudio.com/authoring_quick_tour.html>`__ (Rmd) files,
check out the `Rmdawn Python package <https://py4ds.github.io/rmdawn/>`__.

Documentation and code
----------------------

The documentation is hosted at https://py4ds.github.io/nbless/.

The code is hosted at https://github.com/py4ds/nbless.

Installation
------------

.. code:: sh

    pip install nbless

or clone the `repo <https://github.com/py4ds/nbless>`__, e.g.
``git clone https://github.com/py4ds/nbless`` and install locally
using setup.py (``python setup.py install``) or ``pip``
(``pip install .``).

Usage
-----

.. _nbconv:

Converting Jupyter notebooks with ``nbconv``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``nbconv`` shell command and Python function can export a
notebook to many different formats using the ``nbconvert`` library.
Converting to all formats except HTML requires pandoc.
Exporting to PDF requires LaTeX.

The supported exporters are

    - asciidoc
    - pdf
    - html
    - latex
    - markdown
    - python
    - rst
    - script
    - slides

For example, ``nbconv`` can create a python script by extracting
the content from code cells and discarding all output and markdown
content.

.. code:: sh

    nbconv notebook.ipynb --exporter python
    # Or
    nbconv notebook.ipynb -e python


In the example above, the output file would be ``notebook.py``, but you can
provide a more descriptive name for the output file with the ``--out_file`` or
``-o`` flag:

.. code:: sh

    nbconv notebook.ipynb --out_file script.py
    # Or
    nbconv notebook.ipynb -o script.py

If the ``exporter`` is not provided, ``nbconv`` will try to infer the exporter type
from the ``out_file`` extension.

If neither the ``exporter`` or ``out_file`` arguments are provided, the exporter will be set to html.

.. code:: sh

    nbconv notebook.ipynb

.. code:: python

    from pathlib import Path
    import nbformat
    from nbless import nbconv

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


.. _nbdeck:

Creating HTML slides with ``nbdeck`` and ``nbconv``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With ``nbdeck``, you can prepare Jupyter slides from source files (e.g. ``source_file1.md``, ``source_file2.py``) like this:

.. code:: sh

    nbless slide_file* -o slides.ipynb
    nbdeck slides.ipynb -o slides.ipynb
    nbconv slides.ipynb  -e slides -o slides.html

.. _nbexec:

Executing a notebook with ``nbexec``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


.. _nbless:

Creating and executing a Jupyter notebook with ``nbless``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. _nbraze:

Extracting source files from a Jupyter notebook with ``nbraze``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    nbraze notebook.ipynb

The ``nbraze`` function takes the contents of `Jupyter Notebook code cells <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html>`__ and turns them into Python or R code files (``.py`` or ``.R``).
The contents of `markdown cells <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html>`__ are turned into markdown files.


.. _nbuild:

Creating a Jupyter notebook with ``nbuild``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The ``nbuild`` shell command and Python function takes the contents of Python or R code files
(``.py`` or ``.R``) and stores them as `Jupyter Notebook code
cells <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html>`__.
The contents of all other files are stored in `markdown
cells <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html>`__.

.. code:: sh

    nbuild README.md plot.py notes.txt > notebooks/notebook.ipynb


Instead of redirecting to a file (``>``), you can use the ``--out_file``
or ``-o`` flag:

.. code:: sh

    nbuild README.md plot.py notes.txt --out_file notebooks/notebook.ipynb
    # Or
    nbuild README.md plot.py notes.txt -o notebooks/notebook.ipynb

You can preview the raw notebook output by running ``nbuild`` with only the positional arguments:

.. code:: sh

    nbuild README.md plot.py notes.txt

The ``nbuild`` Python function does create a file on its own. To create a notebook file, use the ``nbformat`` library.

.. code:: python

    import nbformat
    from nbless import nbuild

    # Create notebook.ipynb from plot.py and notes.txt
    nb = nbuild(["plot.py", "notes.txt"])
    nbformat.write(nb, "notebook.ipynb")

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

.. |Build| image:: https://travis-ci.org/py4ds/nbless.svg?branch=master
   :target: https://travis-ci.org/py4ds/nbless
.. |Chat| image:: https://badges.gitter.im/py4ds/nbless.svg
   :alt: Join the chat at https://gitter.im/py4ds/nbless
   :target: https://gitter.im/py4ds/nbless?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Coverage| image:: https://img.shields.io/codecov/c/gh/py4ds/nbless.svg
   :target: https://codecov.io/gh/py4ds/nbless
.. |License| image:: https://img.shields.io/badge/License-MIT-purple.svg
   :target: https://opensource.org/licenses/MIT
.. |PyPI| image:: https://img.shields.io/pypi/v/nbless.svg
   :target: https://pypi.python.org/pypi/nbless
.. |Repo status| image:: https://www.repostatus.org/badges/latest/active.svg
   :alt: Project Status: Active – The project has reached a stable, usable state and is being actively developed.
   :target: https://www.repostatus.org/#active
.. |PyUp| image:: https://pyup.io/repos/github/py4ds/nbless/shield.svg
   :target: https://pyup.io/repos/github/py4ds/nbless/
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/nbless.svg
   :alt: PyPI - Python Version
   :target: https://www.python.org/downloads/
