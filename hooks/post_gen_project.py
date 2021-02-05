import shutil
from pathlib import Path

ROOT_DIR = Path().absolute()
ACTIONS_DIR = ROOT_DIR.joinpath("actions")
GITHUB_DIR = ROOT_DIR.joinpath(".github")


def main() -> None:
    set_license("{{cookiecutter.license}}")

    use_dependabot = "{{cookiecutter.use_dependabot}}" == "True"
    set_dependabot(use_dependabot)

    use_continuous_deployment = "{{cookiecutter.use_continuous_deployment}}" == "True"
    set_cd(use_continuous_deployment)

    shutil.rmtree(ACTIONS_DIR)


def set_cd(use_continuous_deployment: bool) -> None:
    if use_continuous_deployment:
        shutil.copy(
            ACTIONS_DIR / "pypi_publish.yaml",
            GITHUB_DIR / "workflows" / "pypi_publish.yaml",
        )


def set_dependabot(use_dependabot: bool) -> None:
    if use_dependabot:
        shutil.copy(
            ACTIONS_DIR / "dependabot.yaml",
            GITHUB_DIR / "dependabot.yaml",
        )


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
