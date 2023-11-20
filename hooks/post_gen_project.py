import os

# REMOVE_PATHS = [
# '{% if cookiecutter.packaging != "pip" %}requirements.txt{% endif %}',
# '{% if cookiecutter.packaging != "poetry" %}poetry.lock{% endif %}',
# ]

REMOVE_PATHS = [] # TODO add paths to remove

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
