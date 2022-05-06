import sys


def validate():
    exit_one_checks = [
        ("{{ cookiecutter.project_name }}", "project name"),
        ("{{ cookiecutter.creator }}", "creator"),
        ("{{ cookiecutter.creator_email }}", "creator email address"),
        ("{{ cookiecutter.license }}", "license"),
    ]

    for check in exit_one_checks:
        exit_one(check[0], check[1])

    license = "{{ cookiecutter.license }}"
    copyright_year = "{{ cookiecutter.copyright_year }}"

    if license == "MIT" and not copyright_year.strip():
        print("You must specify a copyright year for the MIT license")  # noqa: T201
        sys.exit(2)

    if license == "GNU General Public License v3.0" and not copyright_year.strip():
        print(  # noqa: T201
            "You must specify a copyright year for the GNU General Public License v3.0"
        )
        sys.exit(2)

    year_error_msg = "The copyright year entered is not a valid year"
    if copyright_year.strip() and len(copyright_year) != 4:
        print(year_error_msg)  # noqa: T201
        sys.exit(3)
    if len(copyright_year) == 4:
        try:
            int(copyright_year)
        except ValueError:
            print(year_error_msg)  # noqa: T201
            sys.exit(3)

    min_python_version = "{{ cookiecutter.min_python_version }}"
    github_action_python_test_versions = [
        x.strip() for x in "{{ cookiecutter.github_action_python_test_versions }}".split(",")
    ]
    test_version_checks = [
        [int(y) for y in x.split(".")] for x in github_action_python_test_versions
    ]
    test_version_checks.sort(key=lambda x: (x[0], x[1]))
    min_python_version_split = [int(x) for x in min_python_version.split(".")]

    if (
        test_version_checks[0][0] < min_python_version_split[0]
        or test_version_checks[0][0] == min_python_version_split[0]
        and test_version_checks[0][1] < min_python_version_split[1]
    ):
        print(  # noqa: T201
            "The minimum Python version is greater than the lowest version used in the github actions tests"  # noqa: E501
        )
        sys.exit(4)


def exit_one(text_check, field_name):
    if not text_check.strip():
        print(f"You must specify a {field_name} to use this template.")  # noqa: T201
        sys.exit(1)


if __name__ == "__main__":
    validate()
