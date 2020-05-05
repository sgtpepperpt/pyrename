import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrename",
    version="0.1.0",
    author="Guilherme Borges",
    author_email="guilherme@guilhermeborges.net",
    description="Very simple file renamer in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sgtpepperpt/pyrename",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    scripts=['pyrename']
)
