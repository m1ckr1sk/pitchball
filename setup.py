import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pitchball",
    version="0.1.0",
    author="Mike Butt",
    author_email="mikeb@python.org",
    description="A package for simulating volleyball",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mickrisk/pitchball",
    packages=setuptools.find_packages(),
    package_data={'pitchball': ['*.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0 or later (GPL-3.0-or-later)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "names"
    ]
)