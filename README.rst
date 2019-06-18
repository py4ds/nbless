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

The ``nbconv`` shell command can export a
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

Unlike the shell command,
the ``nbconv`` Python function does not create a file on its own.
To create a converted file with Python, use the ``pathlib`` library.

.. code:: python

    from pathlib import Path
    from nbless import nbconv

    # Create notebook.py from notebook.ipynb
    filename, contents = nbconv("notebook.ipynb", "python")
    Path(filename).write_text(contents)

    # Create report.html from notebook.ipynb
    filename, contents = nbconv("notebook.ipynb", "html")
    Path('report.html').write_text(contents)

.. _nbdeck:

Creating HTML slides with ``nbdeck`` and ``nbconv``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With ``nbdeck``, you can prepare HTML slides from a Jupyter notebook.

.. code:: sh

    nbdeck notebook.ipynb -o slides.ipynb
    nbconv slides.ipynb  -e slides -o slides.html

You can run ``nbdeck`` without ``nbconv``,
if you do not want to create HTML slides and instead want to use
`nbviewer <https://nbviewer.jupyter.org/>`__ or the
`RISE extension <https://github.com/damianavila/RISE#rise>`__.
If an ``out_file`` name is not provided, the notebook file contents will be
printed.
You can provide a more descriptive name for the executed output notebook with
the ``--out_file`` or ``-o`` flag or by redirecting the output to a file with
``>``.

.. code:: sh

    nbdeck notebook.ipynb --out_file slides.ipynb
    # Or
    nbdeck notebook.ipynb -o slides.ipynb
    # Or
    nbdeck notebook.ipynb > slides.ipynb

Unlike the shell command,
the ``nbdeck`` Python function does not create a file on its own.
To create a converted file, use the ``nbformat`` and  ``pathlib`` libraries.

.. code:: python

    import nbformat
    from nbless import nbconv, nbdeck

    # Create HTML slides from notebook.ipynb in notebooks folder
    nbformat.write(nbdeck("notebook.ipynb"), "slides.ipynb")
    filename, contents = nbconv("slides.ipynb", "slides")
    Path(filename).write_text(contents)

.. _nbexec:

Executing a notebook with ``nbexec``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``nbexec`` command runs the input notebook from top to bottom.
If an ``out_file`` name is not provided, the executed notebook contents will be
printed.

.. code:: sh

    nbexec notebook.ipynb

You can provide a more descriptive name for the executed output notebook with
the ``--out_file`` or ``-o`` flag or by redirecting the output to a file with
``>``.

.. code:: sh

    nbexec notebook.ipynb --out_file executed.ipynb
    # Or
    nbexec notebook.ipynb -o executed.ipynb
    # Or
    nbexec notebook.ipynb > executed.ipynb

The default kernel is ``python3``, but it is possible to specify the kernel
that will be used to run notebook with the ``--kernel`` or ``-k`` flag.

.. code:: sh

    nbexec notebook.ipynb --kernel ir --out_file notebook.ipynb
    # Or
    nbexec notebook.ipynb -k ir -o notebook.ipynb

You can preview the default output filename and the raw notebook output by
running ``nbexec`` with only the positional argument:

.. code:: sh

    nbexec notebook.ipynb

Unlike the shell command,
the ``nbexec`` Python function does not create a file on its own.
To create a notebook file, use the ``nbformat`` library.

.. code:: python

    import nbformat
    from nbless import nbexec

    # Create notebook.ipynb from notebook.ipynb
	nb = nbexec("notebook.ipynb")
    nbformat.write(nb, "executed.ipynb")
	Rnb = nbexec("Rnotebook.ipynb")
    nbformat.write(Rnb, "Rexecuted.ipynb", kernel="ir")

.. _nbless:

Creating and executing a Jupyter notebook with ``nbless``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``nbless`` shell command executes a notebook created from code and markdown/text files.

.. code:: sh

    nbless README.md plot.py notes.txt > executed.ipynb

The default kernel is ``python3``, but it is possible to specify the kernel that will be used to run notebook with the
``--kernel`` or ``-k`` flag.

.. code:: sh

    nbless README.md plot.py notes.txt --kernel ir > Rnotebook.ipynb
    # Or
    nbless README.md plot.py notes.txt -k ir > Rnotebook.ipynb

Instead of redirecting to a file (``>``), you can use the ``--out_file``
or ``-o`` flag:

.. code:: sh

    nbless README.md plot.py notes.txt --out_file executed.ipynb
    # Or
    nbless README.md plot.py notes.txt -o executed.ipynb

Unlike the shell command,
the ``nbless`` Python function does not create a file on its own.
To create a notebook file, use the ``nbformat`` library.

.. code:: python

    import nbformat
    from nbless import nbless

    # Build and execute a notebook with nbless
	nb = nbless(["plot.py", "notes.txt"])
    nbformat.write(nb, "executed.ipynb")
	Rnb = nbless(["plot.R", "notes.txt"], kernel="ir")
    nbformat.write(Rnb, "Rexecuted.ipynb")

.. _nbraze:

Extracting source files from a Jupyter notebook with ``nbraze``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``nbraze`` shell command takes the contents of `Jupyter Notebook code cells
<https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html>`__
and turns them into code files, e.g. Python or R code files (``.py`` or
``.R``). The contents of `markdown cells
<https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html>`__
are turned into markdown files.

.. code:: sh

    nbraze notebook.ipynb

The default code file extension for ``nbraze`` is ``py``, but it is possible to
set the file extension with the ``--extension`` or ``-e`` flag. If the
``language_info`` key is defined in the Jupyter notebook metadata, ``nbraze``
can try to infer the code file extension from the programming language.

.. code:: sh

    nbraze notebook.ipynb --extension R
    nbraze notebook.ipynb -e js

.. code:: python

    from nbless import nbraze

    # Create source files from notebook.ipynb
	nbraze("notebook.ipynb")
	nbraze("notebook.ipynb", extension="R")

.. _nbuild:

Creating a Jupyter notebook with ``nbuild``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``nbuild`` shell command takes the contents of Python or R code files
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

The ``nbuild`` Python function does not create a file on its own.
To create a notebook file, use the ``nbformat`` library.

.. code:: python

    import nbformat
    from nbless import nbuild

    # Create notebook.ipynb from plot.py and notes.txt
    nb = nbuild(["plot.py", "notes.txt"])
    nbformat.write(nb, "notebook.ipynb")

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
