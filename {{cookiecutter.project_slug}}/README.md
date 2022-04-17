# {{cookiecutter.project_name}}

{{cookiecutter.package_description}}

## Developments

Use conda to create a Python virtual environment:

```bash
conda env create -f conda.yaml
conda activate {{cookiecutter.project_slug}}
```

Use VS Code launch configuration "Launch '{{cookiecutter.project_slug}}
package'" to debug package.
