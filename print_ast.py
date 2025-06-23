#!/usr/bin/env python3
import argparse

from cpp_ast_codex.ast_builder import parse_path
from cpp_ast_codex.text import to_text

DEFAULT_CLANG = None


def main():
    parser = argparse.ArgumentParser(description='Print AST as text for a C/C++ source file or directory')
    parser.add_argument('source', help='Path to C/C++ source file or directory')
    parser.add_argument('--clang-lib', default=DEFAULT_CLANG, help='Path to libclang shared library (optional)')
    parser.add_argument('--clang-args', nargs='*', default=['-std=c++17'], help='Extra arguments for clang parser')
    args = parser.parse_args()

    root = parse_path(args.source, clang_lib=args.clang_lib, clang_args=args.clang_args)
    print(to_text(root))


if __name__ == '__main__':
    main()
