# https://github.com/cookiecutter/cookiecutter/issues/723
# https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/post_gen_project.py#L4

import os
import shutil
import sys
import subprocess
import yaml

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
MANIFEST = os.path.join(PROJECT_DIRECTORY, "manifest.yaml")


def delete_resources_for_disabled_features() -> None:
    """Deletes the ressources of the disabled features."""
    with open(MANIFEST) as manifest_file:
        manifest = yaml.load(manifest_file, yaml.SafeLoader)
        for feature in manifest["features"]:
            if feature["enabled"] == "false":
                print(f"removing resources for disabled feature {feature['name']}")
                for resource in feature["resources"]:
                    delete_resource(resource)
    print("cleanup complete, removing manifest...")
    delete_resource(MANIFEST)


def delete_resource(resource_name: str) -> None:
    """Deletes teh given file or directory.

    Args:
        resource_name (str): file or directory to remove
    """
    resource = os.path.join(PROJECT_DIRECTORY, resource_name)
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


def init_repo():
    """Initializes the GitHub repository.

    Raises:
        RuntimeError: If the initialization failed, a RuntimeError will be raised.
    """
    try:
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", "initial commit"], check=True)
        subprocess.run(
            ["git", "branch", "-M", "{{ cookiecutter.branch_name }}"], check=True
        )
        subprocess.run(
            ["git", "remote", "add", "origin", "{{ cookiecutter.repo_url }}"],
            check=True,
        )
        subprocess.run(
            ["git", "push", "-u", "origin", "{{ cookiecutter.branch_name }}"],
            check=True,
        )
    except:
        raise RuntimeError("Could not init and push repo.")


def setup_pre_commits() -> None:
    """Sets up the pre-commits.

    Raises:
        RuntimeError: If pip is not installed, a RuntimeError will be raised.
        RuntimeError: If the installation of the pre-commit hooks fails, a RuntimeError
                      will be raised.
    """
    print("Setting up pre-commits.")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "--version"]
        )  # check if pip is installed
    except:
        raise RuntimeError("Pip is not installed.")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "pre-commit"], check=True
        )
        subprocess.run(["pre-commit", "install", "--install-hooks"], check=True)
    except:
        raise RuntimeError("Could not install pre-commit hooks.")


def update_readme():
    """Updates the README.md according to the selected features."""
    lines = []
    gui_indicators = [
        "Folder for storing assets like images",
        "Contains your application views",
        "Contains all style related code",
        "Contains custom widgets",
    ]
    data_science_indicators = [
        "Trained and serialized models, model predictions, or model summaries",
        "Scripts to turn raw data into features for modeling",
        "Scripts to train models and then use trained models to make",
        "Scripts to create visualizations",
    ]

    # read file
    with open(os.path.join(PROJECT_DIRECTORY, "README.md"), "r") as file:
        lines = file.readlines()

    # Write file
    with open(os.path.join(PROJECT_DIRECTORY, "README.md"), "w") as file:
        for line in lines:
            if (
                not "{{ cookiecutter.use_pre_commits }}"
                and "Configuration file for the pre-commits" in line
                or not "{{ cookiecutter.use_sphinx_documentation }}"
                and "A default Sphinx project; see sphinx-doc.org for details" in line
                or not "{{ cookiecutter.include_gui_structure }}"
                and any(indicator in line for indicator in gui_indicators)
                or not "{{ cookiecutter.include_data_science_structure }}"
                and any(indicator in line for indicator in data_science_indicators)
            ):
                pass  # skip line
            else:
                file.write(line)


def create_venv() -> None:
    """Creates a virtual environment

    Raises:
        RuntimeError: If no virtual environment can be created, a RuntimeError will be raised.
    """
    try:
        print("Start creating virtual environment.")
        subprocess.run(["python", "-m", "venv", "venv"], check=True)
        print("Successfully created virtual environment.")
    except:
        raise RuntimeError("Could not create virtual environment")


if __name__ == "__main__":
    update_readme()
    delete_resources_for_disabled_features()
    init_repo()
    if "{{ cookiecutter.create_venv }}":
        create_venv()
    if "{{ cookiecutter.use_pre_commits }}":
        setup_pre_commits()
    # create .env file
    file = open(".env", "w")
    file.close()
