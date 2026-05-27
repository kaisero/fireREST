try:
    from importlib.metadata import version, PackageNotFoundError

    __version__ = version('fireREST')
except PackageNotFoundError:
    # package not installed (e.g. running directly from source)
    __version__ = '1.3.0'
