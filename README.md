# Deterministic text normaliser

A dependency-free Python command-line tool that converts text into a stable lowercase, hyphen-separated ASCII identifier.

## Usage

```console
$ python normalise.py "Hello, World!"
hello-world
```

The command exits with a non-zero status and writes an error to standard error when the input cannot produce an identifier:

```console
$ python normalise.py "***"
error: normalisation produced an empty result
```

## Tests

```console
python -m unittest discover -s tests -v
```
