import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbless",
    version="0.2.34",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="Construct, deconstruct, convert, and run Jupyter notebooks.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/marskar/nbless",
    package_dir={"": "src"},
    packages=setuptools.find_packages('src'),
    entry_points={
        'console_scripts': [
            'nbless = cli.nbless_cli:nbless_cli',
            'nbuild = cli.nbuild_cli:nbuild_cli',
            'nbraze = cli.nbraze_cli:nbraze_cli',
            'nbdeck = cli.nbdeck_cli:nbdeck_cli',
            'nbexec = cli.nbexec_cli:nbexec_cli',
            'nbconv = cli.nbconv_cli:nbconv_cli',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'click',
        'jupyter',
        'pypandoc'
    ],
    python_requires='>=3.6'
)
