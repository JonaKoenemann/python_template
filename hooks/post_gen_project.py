# https://github.com/cookiecutter/cookiecutter/issues/723
# https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/post_gen_project.py#L4

import os
import shutil
import sys
import subprocess
import yaml

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
MANIFEST = os.path.join(PROJECT_DIRECTORY, "manifest.yaml")


def delete_resources_for_disabled_features():
    with open(MANIFEST) as manifest_file:
        manifest = yaml.load(manifest_file, yaml.SafeLoader)
        for feature in manifest["features"]:
            if feature["enabled"] == "false":
                print(f"removing resources for disabled feature {feature['name']}")
                for resource in feature["resources"]:
                    delete_resource(resource)
    print("cleanup complete, removing manifest...")
    delete_resource(MANIFEST)


def delete_resource(resource_name):
    resource = os.path.join(PROJECT_DIRECTORY, resource_name)
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


def init_repo():
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


def setup_pre_commits():
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


if __name__ == "__main__":
    use_pre_commits = "{{ cookiecutter.use_pre_commits }}"
    print(use_pre_commits, type(use_pre_commits))
    delete_resources_for_disabled_features()
    init_repo()
    if "{{ cookiecutter.use_pre_commits }}" == "true":
        setup_pre_commits()
    # create .env file
    file = open(".env", "w")
    file.close()
