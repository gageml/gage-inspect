from gage_inspect._util import pkg_version


def test_pkg_version():
    pkg_ver = pkg_version("gage_inspect")
    try:
        import tomllib
    except ImportError:
        # Don't have toml support, just assert a not null resp
        assert pkg_ver is not None
    else:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
            assert pkg_ver == data["project"]["version"]
