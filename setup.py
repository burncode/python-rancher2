#!/usr/bin/python
from setuptools import setup, find_packages

# Import the module version
from rancher2 import __version__

# Run the setup
setup(
    name             = 'rancher2',
    version          = __version__,
    description      = 'Library for interacting with the Rancher 2 v3 API',
    long_description = open('DESCRIPTION.rst').read(),
    author           = 'David Taylor',
    author_email     = 'djtaylor13@gmail.com',
    url              = 'http://github.com/djtaylor/python-rancher2',
    license          = 'GPLv3',
    install_requires = [],
    entry_points     = {
        'console_scripts': ['rancher2=rancher2:cli_client'],
    },
    packages         = find_packages(),
    keywords         = 'rancher rancher2 v3 api http https',
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals',
    ]
)
