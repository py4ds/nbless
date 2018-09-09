from packages.nbless.nbuild import nbuild
from packages.nbless.nbexec import nbexec
from packages.nbless.nbless import nbless
nbuild(["packages/nbless/README.md", "packages/nbless/plot.py", "packages/nbless/notes.txt"], output_path="packages/nbless/notebooks")
nbexec("packages/nbless/notebooks/raw.ipynb", output_path="packages/nbless/notebooks")
nbless(["packages/nbless/README.md", "packages/nbless/plot.py", "packages/nbless/notes.txt"], nbexec_path="packages/nbless/notebooks")
