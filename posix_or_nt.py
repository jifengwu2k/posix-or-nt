import os


def posix_or_nt():
    """
    Return the underlying flavor of the operating system:

    - `'posix'` for Unix-like systems (Linux, macOS, etc.).
    - `'nt'`    for Windows.

    On Jython `os.name` is the shadow string `'java'`;
    we call `os.name.getshadow()` to discover the real platform.
    """
    name = os.name

    # Fast path: CPython & PyPy
    if name in ('posix', 'nt'):
        return name

    # Jython and friends
    if name == 'java':
        try:
            shadow = name.getshadow()  # type: ignore[attr-defined]
        except AttributeError as exc:
            raise OSError("`os.name` is 'java' but no shadow value available")

        if shadow in ('posix', 'nt'):
            return shadow

    raise OSError("Unsupported `os.name` value: %r" % name)
