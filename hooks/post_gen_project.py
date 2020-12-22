import shutil
from pathlib import Path


def main() -> None:
    set_license("{{cookiecutter.license}}")


def set_license(license: str) -> None:
    root_dir = Path().absolute()
    license_dir = root_dir.joinpath("licenses")

    if license == "MIT":
        shutil.copy(license_dir.joinpath("mit"), root_dir.joinpath("LICENSE"))
    elif license == "Apache 2.0":
        shutil.copy(license_dir.joinpath("apache2"), root_dir.joinpath("LICENSE"))
    elif license == "GNU General Public License v3.0":
        shutil.copy(license_dir.joinpath("gpl3"), root_dir.joinpath("LICENSE"))

    shutil.rmtree(license_dir)


if __name__ == "__main__":
    main()
