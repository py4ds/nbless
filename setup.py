import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbless",
    version="0.2.26",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="Construct, deconstruct, convert, and run Jupyter notebooks.",
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
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'click',
        'jupyter'
    ]
)
