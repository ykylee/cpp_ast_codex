# cpp_ast_codex

This repository contains tools for analyzing C/C++ source code and generating an Abstract Syntax Tree (AST).

See [SRS.md](SRS.md) for the software requirements collected from GitHub issues.

## Usage

After installing the dependencies (`pip install clang==17.* graphviz` and a system `graphviz` package), run:

```bash
./generate_ast_image.py <source_or_directory> -o output.png
./print_ast.py <source_or_directory>
```

The script parses the given file or all C/C++ files inside a directory using `libclang` and outputs the AST as a PNG image.
`print_ast.py` prints the AST in a textual tree format similar to the `tree` command.

See [docs/text_output.md](docs/text_output.md) for more details on the text output format.

On Windows, install LLVM and ensure `libclang.dll` is available. You can provide
the path explicitly using `--clang-lib` or set the environment variable
`CLANG_LIBRARY_FILE`/`LIBCLANG_PATH` so the tool can locate the library.

## Running tests

Unit tests require `pytest` and ensure parsing and visualization work correctly:

```bash
PYTHONPATH=. pytest -q
```
