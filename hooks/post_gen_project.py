import shutil
from pathlib import Path

ROOT_DIR = Path().absolute()
ACTIONS_DIR = ROOT_DIR.joinpath("actions")
GITHUB_DIR = ROOT_DIR.joinpath(".github")


def main() -> None:
    set_license("{{ cookiecutter.license }}")

    use_dependabot = "{{ cookiecutter.use_dependabot }}".lower() == "yes"
    set_dependabot(use_dependabot)

    use_continuous_deployment = "{{ cookiecutter.use_continuous_deployment }}".lower() == "yes"
    set_cd(use_continuous_deployment)

    multi_os_ci = "{{ cookiecutter.multi_os_ci }}".lower() == "yes"
    set_multi_os_ci(multi_os_ci)

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


def set_multi_os_ci(multi_os_ci: bool) -> None:
    if multi_os_ci:
        shutil.copy(ACTIONS_DIR / "testing_all_os.yaml", GITHUB_DIR / "workflows" / "testing.yaml")
    else:
        shutil.copy(
            ACTIONS_DIR / "testing_linux_only.yaml", GITHUB_DIR / "workflows" / "testing.yaml"
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
