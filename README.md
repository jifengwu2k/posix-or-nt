# posix-or-nt

Determine whether the current Python interpreter is running on a POSIX-like or Windows NT platform---even when `os.name` is `java` (Jython).

## Features

-   Single import: `from posix_or_nt import posix_or_nt`
-   Returns `'posix'` or `'nt'` across CPython, PyPy, and Jython.
-   Supports Python 2+
-   Zero dependencies

## Installation

```
pip install posix-or-nt
```

## Quickstart

```
>>> from posix_or_nt import posix_or_nt
>>> posix_or_nt()
'posix'   # or 'nt'
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

MIT License. See [LICENSE](LICENSE) for more information.
