import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbless",
    version="0.1.1",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="Create Jupyter notebooks from Markdown and Python scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marskar/nbless",
    packages=setuptools.find_packages(),
    #scripts=['nbless.py', 'nbuild.py', 'nbexec.py'],
    entry_points={
        'console_scripts': [
            'nbless = nbless.nbless:command_line_runner',
            'nbuild = nbless.nbuild:command_line_runner',
            'nbexec = nbless.nbexec:command_line_runner',
            'nbcode = nbless.nbcode:command_line_runner',
            'nbhtml = nbless.nbhtml:command_line_runner',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
        install_requires=[
        'jupyter'
    ]
)

