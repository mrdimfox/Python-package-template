from setuptools import setup
from setuptools import find_namespace_packages as find_packages

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    description="{{cookiecutter.package_description}}",
    url="{{cookiecutter.package_url}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}"
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">={{cookiecutter.python_version}}, <4",
    classifiers=[],
    install_requires=[],
    extras_require={
        "dev": [
            "wemake-python-styleguide",
            "mypy",
            "black",
        ],
        "tests": [
            "pytest",
        ],
    },
    {%- if cookiecutter.project_type == "executable" -%}
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}}={{cookiecutter.project_slug|replace('-', '_')}}.__main__:main"
        ]
    },
    {%- endif -%}
    package_data={
        "{{cookiecutter.project_slug|replace('-', '_')}}": [""]
    },
    project_urls={
        "Source": "{{cookiecutter.package_url}}",
    },
)
