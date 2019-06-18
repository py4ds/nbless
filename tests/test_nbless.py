from pathlib import Path

import pytest
from tests.make_temp import make_tempfiles, make_temp_notebook

from nbless import nbless, nbuild, nbexec, nbconv, nbraze, nbdeck


def test_nbuild_one_cell(tmp_path: Path) -> None:
    """Run nbuild() to create 3 temporary notebook files from 3 tempfiles."""
    for tempfile in make_tempfiles(tmp_path):
        assert nbuild([tempfile]).cells[0].source == Path(tempfile).read_text()


def test_nbless_one_cell(tmp_path: Path) -> None:
    """Run nbless() to create and execute three notebook files."""
    for tempfile in make_tempfiles(tmp_path):
        assert nbless([tempfile]).cells[0].source == Path(tempfile).read_text()


def test_nbuild_three_cells(tmp_path: Path) -> None:
    """Run nbuild() to create a temporary notebook file from 3 tempfiles."""
    files = make_tempfiles(tmp_path)
    cells = nbuild(files).cells
    assert [c.cell_type for c in cells] == ["markdown", "code", "markdown"]
    for cell, tempfile in zip(cells, files):
        assert cell.source == Path(tempfile).read_text()


def test_nbless_three_cells(tmp_path: Path) -> None:
    """Run nbless() to create and execute a 3-cell notebook file."""
    files = make_tempfiles(tmp_path)
    cells = nbless(files).cells
    assert [c.cell_type for c in cells] == ["markdown", "code", "markdown"]
    for cell, tempfile in zip(cells, files):
        assert cell.source == Path(tempfile).read_text()


def test_nbexec(tmp_path: Path) -> None:
    """Run nbexec() to execute a temporary notebook file."""
    for cell in nbexec(make_temp_notebook(tmp_path)).cells:
        if cell.cell_type == "code":
            assert cell.execution_count
            for output in cell.outputs:
                assert output


@pytest.mark.parametrize("not_exporters", ["htm", "ipython", "markup"])
def test_raises(not_exporters, tmp_path: Path) -> None:
    """Make sure a ValueError is raised if nbconv() gets a bad exporter."""
    nb = make_temp_notebook(tmp_path)
    with pytest.raises(ValueError):
        nbconv(in_file=nb, exporter=not_exporters)


@pytest.mark.parametrize("exporters", ["html", "asciidoc", "rst"])
def test_nbconv(exporters, tmp_path: Path) -> None:
    """Convert ``tempfiles`` with each exporter in ``exporters``."""
    nb = make_temp_notebook(tmp_path)
    assert nbconv(in_file=nb, exporter=exporters)[0].endswith("." + exporters)


def test_nbraze(tmp_path: Path):
    """Extract code and markdown files from the cells of an input notebook."""
    fdict = nbraze(make_temp_notebook(tmp_path))
    assert [Path(f).suffix for f in fdict] == [".md", ".py", ".md"]
    assert fdict["notebook_cell0.md"].startswith("# Background\nMatplotlib")
    assert fdict["notebook_cell1.py"].startswith("import numpy as np\n")
    assert fdict["notebook_cell2.md"].startswith("# Discussion\nMatplotlib")


def test_nbdeck(tmp_path: Path):
    """ Set up a Jupyter notebook to be viewed as or converted into slides."""
    cells = nbdeck(make_temp_notebook(tmp_path)).cells
    c = 0
    for cell in cells:
        if cell.cell_type == "markdown" and cell.source.startswith("#"):
            c += 1
            assert cell.metadata.slideshow == {"slide_type": "slide"}
    assert c == 2
    assert len(cells) == 3
