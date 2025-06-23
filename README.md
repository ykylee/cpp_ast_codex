# cpp_ast_codex

This repository contains tools for analyzing C/C++ source code and generating an Abstract Syntax Tree (AST).

See [SRS.md](SRS.md) for the software requirements collected from GitHub issues.

## Usage

After installing the dependencies (`pip install clang==17.* graphviz` and a system `graphviz` package), run:

```bash
./generate_ast_image.py <source_file.c> -o output.png
```

The script parses the source file using `libclang` and outputs the AST as a PNG image.

On Windows, install LLVM and ensure `libclang.dll` is available. You can provide
the path explicitly using `--clang-lib` or set the environment variable
`CLANG_LIBRARY_FILE`/`LIBCLANG_PATH` so the tool can locate the library.

## Running tests

Unit tests require `pytest` and ensure parsing and visualization work correctly:

```bash
PYTHONPATH=. pytest -q
```
