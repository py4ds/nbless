from pathlib import Path
from typing import List

import nbformat
import pytest
import click

from nbless.cli import nbless_cli, nbuild_cli, nbexec_cli, nbconv_cli


def test_nbless_cli():


