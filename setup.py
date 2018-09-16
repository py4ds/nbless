import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbless",
    version="0.0.7",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="Create Jupyter notebooks from Markdown and Python scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marskar/nbless",
    scripts=['nbless.py', 'nbuild.py', 'nbexec.py'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

