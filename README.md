# Python Cookiecutter Template

[![Tests Status](https://github.com/sanders41/cookiecutter-python/workflows/Testing/badge.svg?branch=main&event=push)](https://github.com/sanders41/cookiecutter-python/actions?query=workflow%3ATesting+branch%3Amain+event%3Apush)
[![Lint Status](https://github.com/sanders41/cookiecutter-python/workflows/Linting/badge.svg?branch=main&event=push)](https://github.com/sanders41/cookiecutter-python/actions?query=workflow%3ALinting+branch%3Amain+event%3Apush)

Generates a Python project structure with Poetry for package management and github actions for continuious integration.

## Dev dependencies that are included

- black
- flake8
- isort
- mypy
- pre-commit
- pytest
- pytest-cov
- tox

## How to use

First make sure you have cookiecutter installed. Instructions for installing can be found [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html).

Once cookiecutter is installed go to the directory where you want to create the project and run:

```zsh
cookiecutter https://github.com/sanders41/cookiecutter-python
```

You will be asked to fill in the following information:

- project_name: The name of the project
- project_slug: The development friendly name of the project. By default, based on the project name
- source_dir: The name name of the source directory for the project. By default, based on the project name
- project_description: A short discription of the purpose of the project [Optional]
- creator: The full name of the project creator
- creator_email: The email address for the creator
- license: The license to use for the project. Select "No license" if no license should be included
- copyright_year: The year to use for the copyright year in the license file. Required for MIT and GNU General Public License v3.0 licenses
- python_version: The minimum version of Python that can be used for the project. By default 3.9 will be used.
- github_action_python_test_versions: The versions of Python that should be used in the CI tests. By default "3.8, 3.9" is used
- tox_python_version: The version of Python that tox should use for testing. By default py38, py39 is used
- max_line_length: The maximum allowed line length. By default 100 is used

Next create a virtual environment

```zsh
python3 -m venv venv
```

And activate the newly created virtual environment

```zsh
. venv/bin/activate
```

With the virtual environment activated install the dependencies

```zsh
poetry install
```

Create a git repositry

```zsh
git init
```

Install the pre-commit hooks

```zsh
pre-commit install
```

Commit the files to git

```zsh
git add .
git commit -am 'Inital commit'
```

Rename the master branch to main

```zsh
git branch -m master main
```

Now the project is ready to use.

## Change log

### 0.2.1

- Bumping tox to ^3.21.4

### 0.2.0

- Adding the options to use Dependabot

### 0.1.13

- pre-commit updated to ^2.10.0

### 0.1.12

- pytest updated to ^6.2.2

### 0.1.11

- mypy updated to 0.800

### 0.1.10

- pytest-cov updated to ^2.11.1
- tox updated to ^3.21.2

### 0.1.9

- Python version added to name attribute in python setup for the testing CI action

### 0.1.8

- Update tox to version 3.21.1

### 0.1.7

- Update tox to version 3.21.0

### 0.1.6

- Added .DS_Store and .swp files to gitignore

### 0.1.5

- Fixed mypy directory in linting action
- Updated isort version in pre-commmit-config

### 0.1.4

- Updated isort version

### 0.1.3

- mypy check added to the default github actions linting checks

### 0.1.2

- min_python_version added to the project creation
- Check to make sure the minimum python version isn't greater than the minimum version used in
  the CI tests

### 0.1.1

- pre-commit updated to version 2.9.3
