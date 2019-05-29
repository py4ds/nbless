from pathlib import Path
from typing import List

import nbformat
# import pytest

from nbless import nbless, nbuild#, nbconv


def make_tempfiles(tmp_path: Path) -> List[str]:
    """Helper function to create a list of pathlib Path objects."""
    md = tmp_path / "intro.md"
    py = tmp_path / "plot.py"
    txt = tmp_path / "discussion.txt"
    md.write_text("# Introduction\nHere's a plot made with the matplotlib.")
    py.write_text("import numpy as np\nimport matplotlib.pyplot as plt\n"
                  "N = 50\nx = y = colors = np.random.rand(N)\n"
                  "area = np.pi * (15 * np.random.rand(N)) ** 2\n"
                  "plt.scatter(x, y, s=area, c=colors, alpha=0.5)\nplt.show()"
                  )
    txt.write_text("Discussion\nMatplotlib is verbose, but makes cool plots!")
    return [md.as_posix(), py.as_posix(), txt.as_posix()]


def make_temp_notebook(tmp_path: Path) -> str:
    """Helper function to create a list of pathlib Path objects."""
    nb = tmp_path / "notebook.ipynb"
    nb.write_text(nbformat.writes(nbuild(make_tempfiles(tmp_path))))
    return nb.as_posix()


def test_nbuild(tmp_path: Path) -> None:
    """Run nbuild() to create a temporary notebook file from 3 tempfiles."""
    for tempfile in make_tempfiles(tmp_path):
        assert nbuild([tempfile]).cells[0].source == Path(tempfile).read_text()


def test_nbless(tmp_path: Path) -> None:
    """Run nbless() to create and execute a temporary notebook file."""
    for tempfile in make_tempfiles(tmp_path):
        assert nbless([tempfile]).cells[0].source == Path(tempfile).read_text()

# Can't get Pandoc to work with Travis

# @pytest.mark.parametrize('not_exporters', ['htm', 'ipython', 'markup'])
# def test_raises(not_exporters, tmp_path: Path) -> None:
#     """Make sure a ValueError is raised if nbconv() gets a bad exporter."""
#     nb = make_temp_notebook(tmp_path)
#     with pytest.raises(ValueError):
#         nbconv(in_file=nb, exporter=not_exporters)


# @pytest.mark.parametrize('exporters', ['html', 'asciidoc', 'rst'])
# def test_nbconv(exporters, tmp_path: Path) -> None:
#     """Convert ``tempfiles`` with each exporter in ``exporters``."""
#     nb = make_temp_notebook(tmp_path)
#     assert nbconv(in_file=nb,
#                   exporter=exporters)[0].endswith("." + exporters)
