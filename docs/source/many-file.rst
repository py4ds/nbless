Too many file names to type out?
--------------------------------

The easiest way to handle large numbers of files is to use the ``*`` wildcard in the shell.

.. code:: sh

    nbuild source_file* -o notebook.ipynb

You can use the ``ls`` command to assign all of the relevant names in
the current directory to a variable and pass this variable as an
argument.

Consider the example below:

.. code:: sh

    touch {01..09}.py
    name_list=`ls 0*.py`
    nbuild `echo $name_list`

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
