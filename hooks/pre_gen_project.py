import sys


def validate():
    project_name = "{{ cookiecutter.project_name }}"
    creator = "{{ cookiecutter.creator }}"
    creator_email = "{{ cookiecutter.creator_email }}"
    license = "{{ cookiecutter.license }}"
    copyright_year = "{{ cookiecutter.copyright_year }}"

    if not project_name.strip():
        print("You must specify a project name to use this template.")  # noqa: T001
        sys.exit(1)

    if not creator.strip():
        print("You must specify a creator to use this template.")  # noqa: T001
        sys.exit(1)

    if not creator_email.strip():
        print("You must specify a creator email address to use this template.")  # noqa: T001
        sys.exit(1)

    if license == "MIT" and not copyright_year.strip():
        print("You must specify a copyright year for the MIT license")  # noqa: T001
        sys.exit(2)

    if license == "GNU General Public License v3.0" and not copyright_year.strip():
        print(  # noqa: T001
            "You must specify a copyright year for the GNU General Public License v3.0"
        )
        sys.exit(2)

    year_error_msg = "The copyright year entered is not a valid year"
    if copyright_year.strip() and len(copyright_year) != 4:
        print(year_error_msg)  # noqa: T001
        sys.exit(3)
    if len(copyright_year) == 4:
        try:
            int(copyright_year)
        except ValueError:
            print(year_error_msg)  # noqa: T001
            sys.exit(3)


if __name__ == "__main__":
    validate()
