from setuptools import find_packages, setup

import tracks

with open("./README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    author = 'Patrick Gillan',
    author_email = "pgillan@minorimpact.com",
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        ],
    description = '',
    entry_points = { "console_scripts": [ "tracks = tracks.tracks:main" ] },
    install_requires = ["minorimpact"],
    license = 'GPLv3',
    long_description = readme,
    long_description_content_type = "text/markdown",
    name = 'tracks',
    packages = find_packages(),
    py_modules = ["tracks"],
    setup_requires = [],
    tests_require = [],
    url = "https://github.com/pgillan145/tracks",
    version = '0.0.6'
)
