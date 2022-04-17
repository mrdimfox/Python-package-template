from {{cookiecutter.project_slug|replace('-', '_')}} import lib_fun


def test_lib_fun():
    assert lib_fun() == 0
