# SFPS - Smooth FPS
# BSD 2-Clause License
# Copyright (c) 2024, Ratha SIV

from setuptools import  setup

def get_version_string():
    version_py = "sfps/__init__.py"
    with open(version_py) as version_file:
        for line in version_file.read().splitlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]

def main_setup():

    LICENSE = "BSD-2-Clause"
    DESCRIPTION = "SFPS - Smooth FPS."
    LONG_DESCRIPTION = open("README.md", encoding="utf-8").read()
    PACKAGE_NAME = "sfps"

    setup(
        name=PACKAGE_NAME,
        version=get_version_string(),
        description=DESCRIPTION,
        license=LICENSE,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        keywords=['SFPS', 'FPS', 'Frame rate', 'FPS calculator'],
        url="https://github.com/rathaROG/smooth-fps",
        author="Ratha SIV",
        maintainer="rathaROG",
        include_package_data=True,
        classifiers=['Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'Intended Audience :: Education',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: BSD License',
                     'Programming Language :: Python :: 3',
                     'Topic :: Education',
                     'Topic :: Education :: Testing',
                     'Topic :: Scientific/Engineering',
                     'Topic :: Scientific/Engineering :: Mathematics',
                     'Topic :: Software Development',
                     'Topic :: Software Development :: Libraries',
                     'Operating System :: Microsoft :: Windows',                                  
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS',],
    )

if __name__ == "__main__":
    """
    Recommend using :py:mod:`build` to build the package as it does not 
    mess up your current environment.

    >>> pip install wheel build
    >>> python -m build --sdist
    >>> python -m build --wheel
    """ 
    main_setup()
