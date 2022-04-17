from os import remove
from pathlib import Path

package_name = '{{cookiecutter.project_slug|replace('-', '_')}}'
package_type = '{{ cookiecutter.project_type }}'
package_path = Path.cwd()

if package_type == "library":
    print("[POST GEN HOOK] No need to use __main__.py in library. Removing it.")
    main = package_path / "src" / f"{package_name}" / "__main__.py"
    if main.exists():
        try:
            remove(main)
        except Exception as rm_error:
            print("[POST GEN HOOK] Upps. Can't remove __main__.py. Do it by youself.")
            print(f'[POST GEN HOOK] Error: "{rm_error}"')
