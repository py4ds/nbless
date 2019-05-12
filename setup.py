import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbless",
    version="0.2.22",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="Create Jupyter notebooks from Markdown and Python scripts.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/marskar/nbless",
    package_dir={"": "src"},
    packages=setuptools.find_packages('src'),
    # scripts=['nbless.py', 'nbuild.py', 'nbexec.py'],
    entry_points={
        'console_scripts': [
            'nbless = cli.nbless_click:nbless_click',
            'nbuild = cli.nbuild_click:nbuild_click',
            'nbraze = cli.nbraze_click:nbraze_click',
            'nbdeck = cli.nbdeck_click:nbdeck_click',
            'nbexec = cli.nbexec_click:nbexec_click',
            'nbconv = cli.nbconv_click:nbconv_click',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'click',
        'jupyter'
    ]
)
