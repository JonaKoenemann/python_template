# https://github.com/cookiecutter/cookiecutter/issues/723
# https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/post_gen_project.py#L4

import os
import shutil
import yaml

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
MANIFEST = os.path.join(PROJECT_DIRECTORY, "manifest.yaml")

def delete_resources_for_disabled_features():
    with open(MANIFEST) as manifest_file:
        manifest = yaml.load(manifest_file, yaml.SafeLoader)
        for feature in manifest['features']:
            if not feature['enabled']:
                print(f"removing resources for disabled feature {feature['name']}")
                for resource in feature['resources']:
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

if __name__ == "__main__":
    delete_resources_for_disabled_features()
