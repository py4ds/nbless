from pathlib import Path
from typing import List

import nbformat
import pytest
from click.testing import CliRunner

from cli import nbless_cli, nbuild_cli, nbexec_cli, nbconv_cli
from nbless import nbuild


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


def make_temp_notebook(tmp_path: Path) -> str:
    """Helper function to create a list of pathlib Path objects."""
    nb = tmp_path / "notebook.ipynb"
    nb.write_text(nbformat.writes(nbuild(make_tempfiles(tmp_path))))
    return nb.as_posix()


def test_nbless_cli(tmp_path: Path) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        files = make_tempfiles(tmp_path)
        result = runner.invoke(nbless_cli.nbless_cli, files)
        cells = nbformat.reads(result.output, as_version=4).cells
        assert result.exit_code == 0
        assert [c.cell_type for c in cells] == ["markdown", "code", "markdown"]
        for cell, tempfile in zip(cells, files):
            assert cell.source == Path(tempfile).read_text()


def test_nbuild_cli(tmp_path: Path) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        files = make_tempfiles(tmp_path)
        result = runner.invoke(nbuild_cli.nbuild_cli, files)
        cells = nbformat.reads(result.output, as_version=4).cells
        assert result.exit_code == 0
        assert [c.cell_type for c in cells] == ["markdown", "code", "markdown"]
        for cell, tempfile in zip(cells, files):
            assert cell.source == Path(tempfile).read_text()


def test_nbexec_cli(tmp_path: Path) -> None:
    """Run nbexec() to execute a temporary notebook file."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        nb = make_temp_notebook(tmp_path)
        result = runner.invoke(nbexec_cli.nbexec_cli, nb)
        cells = nbformat.reads(result.output, as_version=4).cells
        for cell in cells:
            if cell.cell_type == "code":
                assert cell.execution_count
                for output in cell.outputs:
                    assert output


def test_nbconv_cli(tmp_path: Path) -> None:
    """Convert ``tempfiles`` with each exporter in ``exporters``."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        nb = make_temp_notebook(tmp_path)
        runner.invoke(nbconv_cli.nbconv_cli, [nb, '-e', 'html'])
        assert Path('notebook.html').read_text().startswith('<!DOCTYPE html>\n')
        runner.invoke(nbconv_cli.nbconv_cli, [nb, '-o', 'report.html'])
        assert Path('report.html').read_text().startswith('<!DOCTYPE html>\n')
        runner.invoke(nbconv_cli.nbconv_cli, [nb, '-o', 'report.adoc'])
        assert Path('report.adoc').read_text().startswith('\n[[introduction]]')
