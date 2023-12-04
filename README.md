## Python template 

This repository contains a cookiecutter python project template.  
You can either use a data science structure or a structure for a project with a gui. You can also combine the two.  
In addition to a fixed folder structure, the template provides the following optional features:
- Python packaging and dependency management with poetry
- pre-commit hooks
- Sphinx documentation

## How to use the template

To use the template, simply call the following command in your desired folder, e.g. GitHub:  

```sh
cookiecutter https://github.com/JonaKoenemann/python_template.git
```
Then some questions are asked that are needed for the template. After the answer, a project is automatically created and an inital commit is created in the desired GitHub repository.

## Project Organization

The project structure when using all features is as follows:

    ├── assets             <- Folder for storing assets like images 
    ├── data               <- Folder for storing your data 
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks
    |
    ├── src                <- Source code for use in this project
    │   ├── data           <- Scripts to download or generate data
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │                     predictions
    │   ├── pages          <- Contains your application views
    │   ├── style          <- Contains all style related code 
    │   ├── utils          <- This folder is for storing all utility functions, such as auth, 
    |   |                     theme, handleApiError, etc.
    │   ├── visualization  <- Scripts to create visualizations 
    |   └── widgets        <- Contains custom widgets 
    │
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    └── 

## Commit conventions

In addition to a good project structure, it is recommended to create proper git commit messages. To ensure that these are consistent, the following approach is suggested:

Each commit message consists of a short descriptive text of the change and two tags. the first tag describes where a change was made and the second tag describes what the commit is about.  

The following tags are proposed:

### Tag 1:

- DAT   -> data related, e.g. database management
- DOC   -> documentation related
- DEP   -> dependency related
- DPLY  -> deployment related
- FEAT  -> feature related
- MOD   -> model related
- NBK   -> notebook related
- ORG   -> organization related, e.g. project structure
- UI    -> user interface related

## Tag 2:

- BFX   -> bug fix
- DEL   -> deletion
- DOCS  -> documentation added or changed
- ENH   -> enhancement, e.g. performance enhancement
- FEAT  -> new feature

A possible commit with this approach could therefore be:

DAT:FEAT added methods for database connection

## Useful links

- [Cookiecutter documentation](https://cookiecutter.readthedocs.io/_/downloads/en/stable/pdf/)
- [Poetry](https://python-poetry.org/)
- [pre-commit hooks](https://pre-commit.com/)
- [Sphinx](https://www.sphinx-doc.org/en/master/)
