from pathlib import Path
from typing import List

import nbformat
import pytest
import click
from click.testing import CliRunner

from cli import nbless_cli, nbuild_cli, nbexec_cli, nbconv_cli


def make_tempfiles(tmp_path: Path) -> List[str]:
    """Helper function to create a list of pathlib Path objects."""
    md = tmp_path / "intro.md"
    py = tmp_path / "plot.py"
    txt = tmp_path / "discussion.txt"
    md.write_text("# Introduction\nHere's a plot made with the matplotlib.")
    py.write_text(
        "import numpy as np\nimport matplotlib.pyplot as plt\n"
        "N = 50\nx = y = colors = np.random.rand(N)\n"
        "area = np.pi * (15 * np.random.rand(N)) ** 2\n"
        "plt.scatter(x, y, s=area, c=colors, alpha=0.5)\nplt.show()"
    )
    txt.write_text("Discussion\nMatplotlib is verbose, but makes cool plots!")
    return [md.as_posix(), py.as_posix(), txt.as_posix()]


def test_nbless_cli(tmp_path: Path) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('hello.txt', 'w') as f:
            f.write('Hello World!')
        assert Path("hello.txt").read_text() == 'Hello World!'
