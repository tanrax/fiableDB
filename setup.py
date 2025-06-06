from setuptools import setup

setup(
    name="fiabledb",
    py_modules=["fiabledb"],
    version="1.0.0",
    python_requires=">3.7",
    description=" Immutable NoSQL database in a plain file ",
    author="Andros Fenollosa",
    author_email="andros@fenollosa.email",
    url="https://github.com/tanrax/fiableDB",
    keywords=["database", "immutable", "nosql", "json"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    entry_points="",
)
