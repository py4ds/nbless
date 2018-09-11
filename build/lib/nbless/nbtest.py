# You can import any or all of the functions from the nbless package.
# The above imports all 3 functions and is the same as the line below.
# You can also import each function individually
from nbuild import nbuild
from nbexec import nbexec
from nbless import nbless
nbuild(["README.md", "plot.py", "notes.txt"], output_path="notebooks/")
nbexec("notebooks/raw.ipynb", output_path="notebooks/")
nbless(["README.md", "plot.py", "notes.txt"], nbexec_path="notebooks/")
# Another alternative is to import the package and use it as a namespace.
import nbless

nbless.nbuild(["README.md", "plot.py", "notes.txt"], output_path="notebooks/")
nbless.nbexec("notebooks/raw.ipynb", output_path="notebooks/")
nbless.nbless(["README.md", "plot.py", "notes.txt"], nbexec_path="notebooks/")
