Missing a dependency?
~~~~~~~~~~~~~~~~~~~~~

If you installed via ``pip`` or ``setup.py``, you should have both of
the dependencies (``click`` and ``jupyter``) already. If not, try pip
installing them separately.

.. code:: sh

    pip install jupyter click

If you have `Anaconda <https://www.anaconda.com/download/>`__ or
`Miniconda <https://conda.io/miniconda.html>`__ installed, you can run

.. code:: sh

    conda install -yc conda-forge jupyter click
