# Python Cookiecutter Template

[![Tests Status](https://github.com/sanders41/cookiecutter-python/workflows/Testing/badge.svg?branch=main&event=push)](https://github.com/sanders41/cookiecutter-python/actions?query=workflow%3ATesting+branch%3Amain+event%3Apush)
[![Lint Status](https://github.com/sanders41/cookiecutter-python/workflows/Linting/badge.svg?branch=main&event=push)](https://github.com/sanders41/cookiecutter-python/actions?query=workflow%3ALinting+branch%3Amain+event%3Apush)

Generates a Python project structure with Poetry for package management and github actions for continuious integration and continuous deployment.

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
- use_dependabot: Adds a GitHub action for dependabot: Default = True
- use_continuous_deployment: Adds a workflow for continous deployment to pypi: Default = False
- multi_os_ci: If True then CI is setup to run tests on Windows, Mac, and Linux. If False tests are only run on Linux: Default = False

Next create a virtual environment and activate it. These two steps are optional, if you skip them Poetry will create and use it's own virtual environment.

Create a virtual environment (optional)

```zsh
python3 -m venv venv
```

Activate the virtual environment (optional)

```zsh
. venv/bin/activate
```

Install the dependencies

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

Rename the master branch to main. This step is optional and only needs to be done if you haven't set your global default branch name to main.

```zsh
git branch -m master main
```

Now the project is ready to use.
