# Contributing

## Where to start

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

The best place to start is to check the [issues](https://github.com/sanders41/cookiecutter-python/issues)
for something that interests you.

## Bug Reports

Please include:
1. A short, self-contained Python snippet reproducing the problem. You can format the code by using
[GitHub markdown](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github). For example:


```
cookiecutter https://github.com/sanders41/cookiecutter-python
```

1. Explain what is currently happening and what you expect instead.

## Working on the code

### Fork the project

In order to work on the project you will need your own fork. Do do this click the "Fork" button on
this project.

Once the project is forked clone it to your local machine:

```
git clone https://github.com/your-user-name/cookiecutter-python.git
cd cookiecutter-python
git remote add upstream https://github.com/sanders41/cookiecutter-python.git
```

This creates the directory cookiecutter-python and connects your repository to the upstream (main project) repository.

### Working with the code

Note: This project uses Poetry to manage dependencies. If you do not already have Poetry installed
you will need to install it with the instuctions here https://python-poetry.org/docs/#installation

Once you have cloned your fork of the repository you will want to create a virtual environment. Once
you are in the cookiecutter-python directory create and activate the virtual environment. This step
is slightly different for Mac/Linux and Windows.

Mac/Linux

```
# Create the environment
python3 -m venv venv

# Activate the environment
. venv/bin/activate
```

Windows

```
# Create the environment
python -m venv venv

#Activate the environment. Use activate.bat for cmd.exe
venv\Scripts\Activate.ps1
```

Once your virtual environmennt is setup the requirements need to be installed.

```
poetry install
```

### Creating a branch

You want your main branch to reflect only production-ready code, so create a feature branch for
making your changes. For example:

```
git checkout -b my-new-feature
```

This changes your working directory to the my-new-feature branch. Keep any changes in this branch
specific to one bug or feature so the purpose is clear. You can have many my-new-features and switch
in between them using the git checkout command.

When creating this branch, make sure your main branch is up to date with the latest upstream
main version. To update your local main branch, you can do:

```
git checkout main
git pull upstream main --ff-only
```

### Code Standards and tests (isort, flake8, black, pytest, and pre-commit)

cookiecutter-python uses [isort](https://pycqa.github.io/isort/),
[Flake8](https://flake8.pycqa.org/en/latest/), and [Black](https://github.com/psf/black), and to ensure consistant code formmating.

You can run linting on your code at any time with:

```
# Run isort
isort tests

# Run black
black tests

# Run flake8
flake8 test
```

It is also suggested that you setup [pre-commit](https://pre-commit.com/) in order to run linting
when you commit changes to you branch. To setup pre-commit for this project run:

```
pre-commit install
```

After this pre-commit will automatically run any time you check in code to your branches. You can
also run pre-commit at any time with:

```
pre-commit run --all
```

### Testing

This project uses [pytest](https://docs.pytest.org/en/stable/) for testing. Please ensure that any additions/changes
you make to the code have tests to go along with them. To run the test suite run

```
pytest
```

## Commiting your code

Once you have made changes to the code on your branch you can see which files have changed by
running:

```
git status
```

If new files were created that and are not tracked by git they can be added by running:

```
git add .
```

Now you can commit your changes in your local repository:

```
git commit -am 'Some short helpful message to describe your changes'
```

If you setup pre-commit and any of the tests fail the commit will be cancelled and you will need to
fix any errors. Once the errors are fixed you can run the same git commit command again.


## Push your changes

Once your changes are ready and all linting/tests are passing you can push your changes to your
forked repositry:

```
git push origin my-new-feature
```

origin is the default name of your remote repositry on GitHub. You can see all of your remote
repositories by running:

```
git remote -v
```

## Making a Pull Request

After pushing your code to origin it is now on GitHub but not yet part of the cookiecutter-python
project. When you’re ready to ask for a code review, file a pull request. Before you do, once again
make sure that you have followed all the guidelines outlined in this document regarding code style and
tests. You should also double check your branch changes
against the branch it was based on by:

1. Navigating to your repository on GitHub
2. Click on Branches
3. Click on the Compare button for your feature branch
4. Select the base and compare branches, if necessary. This will be main and my-new-feature,
5. respectively.

### Make the pull request

If everything looks good, you are ready to make a pull request. This is how you let the maintainers
of the cookiecutter-python project know you have code ready to be reviewed. To submit the pull request:

1. Navigate to your repository on GitHub
2. Click on the Pull Request button
3. You can then click on Commits and Files Changed to make sure everything looks okay one last time
4. Write a description of your changes in the Preview Discussion tab
5. Click Send Pull Request

This request then goes to the repository maintainers, and they will review the code.


### Updating your pull request

Changes to your code may be needed based on the review of your pull request. If this is the case you
can make them in your branch, add a new commit to that branch, push it to GitHub, and the pull
request will be automatically updated. Pushing them to GitHub again is done by:

```
git push origin my-new-feature
```

This will automatically update your pull request with the latest code and restart the Continuous
Integration tests.

Another reason you might need to update your pull request is to solve conflicts with changes that
have been merged into the main branch since you opened your pull request.

To do this, you need to “merge upstream main” in your branch:

```
git checkout my-new-feature
git fetch upstream
git merge upstream/main
```

If there are no conflicts (or they could be fixed automatically), a file with a default commit
message will open, and you can simply save and quit this file.

After the feature branch has been update locally, you can now update your pull request by pushing to
the branch on GitHub:

```
git push origin my-new-feature
```

## Delete your merged branch (optional)

Once your feature branch is accepted into upstream, you’ll probably want to get rid of the branch.
First, merge upstream main into your branch so git knows it is safe to delete your branch:

```
git fetch upstream
git checkout main
git merge upstream/main
```

Then you can do:

```
git branch -d my-new-feature
```

Make sure you use a lower-case -d, or else git won’t warn you if your feature branch has not
actually been merged.

The branch will still exist on GitHub, so to delete it there do:

```
git push origin --delete my-new-feature
```
