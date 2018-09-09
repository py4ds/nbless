from nbuild import nbuild
from nbexec import nbexec
from nbless import nbless
nbuild(["README.md", "plot.py", "notes.txt"], output_path="notebooks/")
nbexec("notebooks/raw.ipynb", output_path="notebooks/")
nbless(["README.md", "plot.py", "notes.txt"], nbexec_path="notebooks/")
