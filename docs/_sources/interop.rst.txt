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
If the ``language_info`` key is defined in the Jupyter notebook metadata, ``nbraze`` will try to infer the programming language.

You can also run the Nbless functions in an R environment using the
`reticulate <https://rstudio.github.io/reticulate/>`__ R package.

All Nbless functions and commands rely on the `nbconvert <https://nbconvert.readthedocs.io/>`__ and `nbformat <http://nbformat.readthedocs.io/>`__ modules that are included with the ``jupyter`` Python library.
The command line interface relies on the `click <https://click.palletsprojects.com/>`__ Python library.

