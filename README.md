# Python Cookiecutter Template

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

```
cookiecutter https://github.com/sanders41/cookiecutter-python
```

You will be asked to fill in the following information:
  -  project_name: The name of the project
  -  project_slug: The development friendly name of the project. By default, based on the project name
  -  source_dir: The name name of the source directory for the project. By default, based on the project name
  -  project_description: A short discription of the purpose of the project [Optional]
  -  creator: The full name of the project creator
  -  creator_email: The email address for the creator
  -  license: The license to use for the project. Select "No license" if no license should be included
  -  copyright_year: The year to use for the copyright year in the license file. Required for MIT and GNU General Public License v3.0 licenses
  -  python_version: The minimum version of Python that can be used for the project. By default 3.9 will be used.
  -  github_action_python_test_versions: The versions of Python that should be used in the CI tests. By default "3.8, 3.9" is used
  -  tox_python_version: The version of Python that tox should use for testing. By default py38, py39 is used
  -  max_line_length: The maximum allowed line length. By default 100 is used

Next create and activate a virtual environment

```
python3 -m venv venv
```

```
. venv/bin/activate
```

With the virtual environment activated install the dependencies

```
poetry install
```

Create a git repositry

```
git init
```

Install the pre-commit hooks

```
pre-commit install
```

Commit the files to git

```
git add .
git commit -am 'Inital commit'
```

Rename the master branch to main

```
git branch -m master main
```

Now the project is ready to use.

## Change log

### 0.1.1

- pre-commit updated to version 2.9.3

### 0.1.2

- min_python_version added to the project creation
- Check to make sure the minimum python version isn't greater than the minimum version used in
  the CI tests
