from importlib.metadata import version

# Change here if project is renamed and does not equal the package name
dist_name = "aleph-pytezos"
__version__ = version(dist_name)

__all__ = ["__version__"]
