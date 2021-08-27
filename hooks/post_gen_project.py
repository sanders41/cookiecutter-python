import shutil
from pathlib import Path

ROOT_DIR = Path().absolute()
GITHUB_DIR = ROOT_DIR.joinpath(".github")
ACTIONS_DIR = ROOT_DIR.joinpath("actions")


def main() -> None:
    Path(".github/workflows").mkdir(parents=True, exist_ok=True)

    set_license("{{ cookiecutter.license }}")

    if "{{ cookiecutter.include_vscode_settings }}".lower() == "yes":
        shutil.move(ROOT_DIR / "vscode", ROOT_DIR / ".vscode")
    else:
        shutil.rmtree(ROOT_DIR / "vscode")

    use_dependabot = "{{ cookiecutter.use_dependabot }}".lower() == "yes"
    set_dependabot(use_dependabot)

    use_continuous_deployment = "{{ cookiecutter.use_continuous_deployment }}".lower() == "yes"
    set_cd(use_continuous_deployment)

    use_release_drafter = "{{ cookiecutter.use_release_drafter }}".lower() == "yes"
    set_release_drafter(use_release_drafter)

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


def set_release_drafter(use_release_drafter: bool) -> None:
    if use_release_drafter:
        shutil.copy(
            ACTIONS_DIR / "release_draft_template.yaml",
            GITHUB_DIR / "release_draft_template.yaml",
        )
        shutil.copy(
            ACTIONS_DIR / "release_drafter.yaml",
            GITHUB_DIR / "workflows" / "release_drafter.yaml",
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
