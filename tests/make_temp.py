from pathlib import Path
from typing import List

import nbformat

from nbless import nbuild


def make_tempfiles(tmp_path: Path) -> List[str]:
    """Helper function to create a list of pathlib Path objects."""
    md = tmp_path / "intro.md"
    py = tmp_path / "plot.py"
    txt = tmp_path / "discussion.txt"
    md.write_text("# Background\nMatplotlib is a Python plotting library.")
    py.write_text(
        "import numpy as np\nimport matplotlib.pyplot as plt\n"
        "N = 50\nx = y = colors = np.random.rand(N)\n"
        "area = np.pi * (15 * np.random.rand(N)) ** 2\n"
        "plt.scatter(x, y, s=area, c=colors, alpha=0.5)\nplt.show()"
    )
    txt.write_text("# Discussion\nMatplotlib is verbose, but makes cool plots!")
    return [md.as_posix(), py.as_posix(), txt.as_posix()]


def make_temp_notebook(tmp_path: Path) -> str:
    """Helper function to create a list of pathlib Path objects."""
    nb = tmp_path / "notebook.ipynb"
    nb.write_text(nbformat.writes(nbuild(make_tempfiles(tmp_path))))
    return nb.as_posix()
