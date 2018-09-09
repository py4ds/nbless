# Create and execute a Jupyter notebook in the terminal

## Step 1. Create a notebook

Run `nbcreate.py` script in your terminal, providing all of the names of the source files as arguments, e.g.

```sh
python nbuild.py README.md plot.py notes.txt
```  

The default output filename is `raw.ipynb`. The default output filepath is the current directory (`'.'`). 

You can provide more descriptive names for the name and path:
    
```sh
python nbuild.py README.md plot.py -o not_executed.ipynb -p notebooks/
```  

## Step 2. Execute the notebook

Run the following command in your terminal:
    
```sh
python nbexec.py raw.ipynb
```

The default output filename is `out.ipynb`. The default output filepath is the current directory (`'.'`). 

You can provide more descriptive names for the output name (`-o`) and path (`-p`):

```sh
python nbexec.py raw.ipynb -o executed.ipynb -p notebooks/
```

## Missing a dependency?

If you installed [Anaconda](https://www.anaconda.com/download/), you should already have all of the dependencies (`python`, `nbformat`, and `nbconvert`).

If not, or if you have [Miniconda](https://conda.io/miniconda.html) installed, run 
 
```sh
conda install -yc conda-forge jupyter
```

If you have any other Python installation, run

```sh
pip install jupyter
```

## Too many file names to type out?

You can use the `ls` command to assign all of the relevant names in the current directory to a variable and pass this variable as an argument to `nbconvert.py`.
 
To preserve the order and differentiate files that should be incorporated into the notebook, I recommend left padding your file names with zeros (e.g. 01_intro.md, 02_figure1.py).
 
Consider the example below:

```sh
touch {01..09}.py
name_list=`ls 0*.py`
python nbuild.py `echo $name_list`
```
