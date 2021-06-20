import sys
from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

COOKIECUTTER_ROOT = Path(__file__).parents[1].resolve()


@pytest.fixture
def project_default():
    return {
        "project_name": "Test Project",
        "project_slug": "test-project",
        "source_dir": "test_project",
        "creator": "Some Person",
        "creator_email": "tester@person.com",
        "copyright_year": "2020",
    }


def no_curlies(filepath):
    """
    Make sure no curly braces appear in a file, i.e. was Jinja able to render everything
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = [
        "{{",
        "}}",
        "{%",
        "%}",
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


def test_project_directories(project_default, tmp_path):
    cookiecutter(
        str(COOKIECUTTER_ROOT), no_input=True, extra_context=project_default, output_dir=tmp_path
    )

    out_dir = tmp_path / project_default.get("project_slug")

    EXPECTED_DIRS = [
        out_dir / ".github",
        out_dir / ".github/workflows",
        out_dir / project_default.get("source_dir"),
        out_dir / "tests",
    ]

    for dir in EXPECTED_DIRS:
        assert dir.exists()

    assert not out_dir.joinpath("licenses").exists()


@pytest.mark.parametrize(
    "project",
    [
        {
            "project_slug": "test-project",
            "source_dir": "test_project",
            "creator": "Some Person",
            "creator_email": "tester@person.com",
        },
        {
            "project_name": "Test Project",
            "creator_email": "tester@person.com",
        },
        {
            "project_name": "Test Project",
            "creator": "Some Person",
        },
    ],
)
def test_exit_1(project, tmp_path):
    with pytest.raises(FailedHookException):
        cookiecutter(
            str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path
        )

        assert sys.exit == 1


@pytest.mark.parametrize("license", ["MIT", "GNU General Public License v3.0"])
def test_exit_2(license, tmp_path):
    project = {
        "project_name": "Test Project",
        "creator": "Some Person",
        "creator_email": "tester@person.com",
        "license": license,
    }

    with pytest.raises(FailedHookException):
        cookiecutter(
            str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path
        )

        assert sys.exit == 2


@pytest.mark.parametrize("copyright_year", ["abcd", 123])
def test_exit_3(copyright_year, tmp_path):
    project = {
        "project_name": "Test Project",
        "creator": "Some Person",
        "creator_email": "tester@person.com",
        "license": "MIT",
        "copyright_year": copyright_year,
    }

    with pytest.raises(FailedHookException):
        cookiecutter(
            str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path
        )

        assert sys.exit == 3


@pytest.mark.parametrize("license", ["MIT", "Apache 2.0", "GNU General Public License v3.0"])
def test_license(project_default, license, tmp_path):
    project = project_default
    project["license"] = license

    cookiecutter(str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path)

    file_path = tmp_path.joinpath(project["project_slug"]).joinpath("LICENSE")

    with open(file_path, "r") as f:
        data = f.read()

    license_string_in_file = [s in data for s in license]

    assert file_path.exists()
    assert no_curlies(file_path)
    assert any(license_string_in_file)


def test_no_license(project_default, tmp_path):
    project = project_default
    project["license"] = "No License"

    cookiecutter(str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path)

    assert not tmp_path.joinpath(project["project_slug"]).joinpath("LICENSE").exists()


def test_readme_file(project_default, tmp_path):
    cookiecutter(
        str(COOKIECUTTER_ROOT), no_input=True, extra_context=project_default, output_dir=tmp_path
    )

    out_dir = tmp_path / project_default["project_slug"]

    file_path = out_dir / "README.md"
    assert file_path.exists()
    assert no_curlies(file_path)


def test_tox(project_default, tmp_path):
    cookiecutter(
        str(COOKIECUTTER_ROOT), no_input=True, extra_context=project_default, output_dir=tmp_path
    )

    out_dir = tmp_path / project_default["project_slug"]

    file_path = out_dir / "tox.ini"
    assert file_path.exists()
    assert no_curlies(file_path)


def test_pyproject(project_default, tmp_path):
    cookiecutter(
        str(COOKIECUTTER_ROOT), no_input=True, extra_context=project_default, output_dir=tmp_path
    )

    out_dir = tmp_path / project_default["project_slug"]

    file_path = out_dir / "pyproject.toml"
    assert file_path.exists()
    assert no_curlies(file_path)


def test_pre_commit(project_default, tmp_path):
    cookiecutter(
        str(COOKIECUTTER_ROOT), no_input=True, extra_context=project_default, output_dir=tmp_path
    )

    out_dir = tmp_path / project_default["project_slug"]

    file_path = out_dir / ".pre-commit-config.yaml"
    assert file_path.exists()
    assert no_curlies(file_path)


def test_gitignore(project_default, tmp_path):
    cookiecutter(
        str(COOKIECUTTER_ROOT), no_input=True, extra_context=project_default, output_dir=tmp_path
    )

    out_dir = tmp_path / project_default["project_slug"]

    file_path = out_dir / ".gitignore"
    assert file_path.exists()
    assert no_curlies(file_path)


def test_flake8(project_default, tmp_path):
    cookiecutter(
        str(COOKIECUTTER_ROOT), no_input=True, extra_context=project_default, output_dir=tmp_path
    )

    out_dir = tmp_path / project_default["project_slug"]

    file_path = out_dir / ".flake8"
    assert file_path.exists()
    assert no_curlies(file_path)


def test_workflow_testing(project_default, tmp_path):
    cookiecutter(
        str(COOKIECUTTER_ROOT), no_input=True, extra_context=project_default, output_dir=tmp_path
    )

    out_dir = tmp_path / project_default["project_slug"]

    file_path = out_dir / ".github/workflows/testing.yaml"
    assert file_path.exists()


def test_python_min_version(tmp_path):
    with pytest.raises(FailedHookException):
        project = {
            "project_name": "Test Project",
            "creator": "Some Person",
            "creator_email": "tester@person.com",
            "license": "No License",
            "min_python_version": 3.9,
            "github_action_python_test_versions": "3.8, 3.9",
        }

        cookiecutter(
            str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path
        )

        assert sys.exit == 4


@pytest.mark.parametrize("use_dependabot, expected", [("yes", True), ("no", False)])
def test_use_dependabot(project_default, use_dependabot, expected, tmp_path):
    project = project_default
    project["use_dependabot"] = use_dependabot

    cookiecutter(str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path)

    file_path = tmp_path.joinpath(project["project_slug"]).joinpath(".github") / "dependabot.yaml"

    if expected:
        assert file_path.exists()
        assert no_curlies(file_path)
    else:
        assert not file_path.exists()


@pytest.mark.parametrize("use_continuous_deployment, expected", [("yes", True), ("no", False)])
def test_use_continuous_deployment(project_default, use_continuous_deployment, expected, tmp_path):
    project = project_default
    project["use_continuous_deployment"] = use_continuous_deployment

    cookiecutter(str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path)

    file_path = tmp_path.joinpath(project["project_slug"]).joinpath(
        ".github/workflows/pypi_publish.yaml"
    )

    if expected:
        assert file_path.exists()
    else:
        assert not file_path.exists()


@pytest.mark.parametrize("use_release_drafter, expected", [("yes", True), ("no", False)])
def test_use_release_drafter(project_default, use_release_drafter, expected, tmp_path):
    project = project_default
    project_default["use_release_drafter"] = use_release_drafter

    cookiecutter(str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path)

    file_path_action = tmp_path.joinpath(project["project_slug"]).joinpath(
        ".github/workflows/release_drafter.yaml"
    )
    file_path_action = tmp_path.joinpath(project["project_slug"]).joinpath(
        ".github/release_draft_template.yaml"
    )

    if expected:
        assert file_path_action.exists()
    else:
        assert not file_path_action.exists()


@pytest.mark.parametrize("multi_os_ci", ["yes", "no"])
def test_multi_os_ci(project_default, multi_os_ci, tmp_path):
    project = project_default
    project["multi_os_ci"] = multi_os_ci

    cookiecutter(str(COOKIECUTTER_ROOT), no_input=True, extra_context=project, output_dir=tmp_path)

    file_path = tmp_path.joinpath(project["project_slug"]).joinpath(
        ".github/workflows/testing.yaml"
    )

    assert file_path.exists()
