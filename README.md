# Python Cookiecutter Template

[![Tests Status](https://github.com/sanders41/cookiecutter-python/workflows/Testing/badge.svg?branch=main&event=push)](https://github.com/sanders41/cookiecutter-python/actions?query=workflow%3ATesting+branch%3Amain+event%3Apush)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sanders41/cookiecutter-python/main.svg)](https://results.pre-commit.ci/latest/github/sanders41/cookiecutter-python/main)

Note: This project will still work, but is not being actively updated. It is instead recommeded to
use this [Python Project Generator](https://github.com/sanders41/python-project-generator) that
is actively maintained and more feature rich.

Generates a Python project structure with Poetry for package management and github actions for
continuous integration and continuous deployment.

## Dev dependencies that are included

- black
- ruff
- mypy
- pre-commit
- pytest
- pytest-cov

## VS Code settings

If yes is selected for `include_vscode_settings` the generated project will contain a
`.vscode/settings.json` file that will automatically run Black when files are saved.

## How to use

First make sure you have cookiecutter installed. Instructions for installing can be found
[here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html).

Once cookiecutter is installed go to the directory where you want to create the project and run:

```sh
cookiecutter https://github.com/sanders41/cookiecutter-python
```

You will be asked to fill in the following information:

- project_name: The name of the project
- project_slug: The development friendly name of the project.
- source_dir: The name name of the source directory for the project.
- project_description: A short discription of the purpose of the project [Optional]
- creator: The full name of the project creator
- creator_email: The email address for the creator
- license: The license to use for the project. Select "No license" if no license should be included
- copyright_year: The year to use for the copyright year in the license file.
- python_version: The default python version.
- min_python_version: The minimum version of Python that can be used for the project.
- github_action_python_test_versions: The versions of Python that should be used in the CI tests.
- max_line_length: The maximum allowed line length.
- use_dependabot: Adds a GitHub action for dependabot.
- use_continuous_deployment: Adds a workflow for continous deployment to pypi.
- multi_os_ci: If True then CI is setup to run tests on Windows, Mac, and Linux. If False tests are
only run on Linux.

Next create a virtual environment and activate it. These two steps are optional, if you skip them
Poetry will create and use it's own virtual environment.

Create a virtual environment (optional)

```sh
python3 -m venv .venv
```

Activate the virtual environment (optional)

```sh
. .venv/bin/activate
```

Install the dependencies

```sh
poetry install
```

Create a git repositry

```sh
git init
```

Install the pre-commit hooks

```sh
pre-commit install
```

Commit the files to git

```sh
git add .
git commit -am 'Inital commit'
```

Rename the master branch to main. This step is optional and only needs to be done if you haven't set
your global default branch name to main.

```sh
git branch -m master main
```

Now the project is ready to use.
