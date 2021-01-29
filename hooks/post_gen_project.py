import shutil
from pathlib import Path

ROOT_DIR = Path().absolute()


def main() -> None:
    set_license("{{cookiecutter.license}}")

    use_dependabot = "{{cookiecutter.use_dependabot}}" == "True"
    set_dependabot(use_dependabot)


def set_dependabot(use_dependabot: bool) -> None:
    actions_dir = ROOT_DIR.joinpath("actions")

    if use_dependabot:
        shutil.copy(
            actions_dir.joinpath("dependabot.yaml"),
            ROOT_DIR.joinpath(".github") / "dependabot.yaml",
        )

    shutil.rmtree(actions_dir)


def set_license(license: str) -> None:
    license_dir = ROOT_DIR.joinpath("licenses")

    if license == "MIT":
        shutil.copy(license_dir.joinpath("mit"), ROOT_DIR.joinpath("LICENSE"))
    elif license == "Apache 2.0":
        shutil.copy(license_dir.joinpath("apache2"), ROOT_DIR.joinpath("LICENSE"))
    elif license == "GNU General Public License v3.0":
        shutil.copy(license_dir.joinpath("gpl3"), ROOT_DIR.joinpath("LICENSE"))

    shutil.rmtree(license_dir)


if __name__ == "__main__":
    main()
