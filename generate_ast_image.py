#!/usr/bin/env python3
import argparse

from cpp_ast_codex.ast_builder import parse_path
from cpp_ast_codex.visualize import to_graph

DEFAULT_CLANG = None

def main():
    parser = argparse.ArgumentParser(description='Generate AST image from C/C++ source file or directory')
    parser.add_argument('source', help='Path to C/C++ source file or directory')
    parser.add_argument('-o', '--output', default='ast.png', help='Output image path (PNG)')
    parser.add_argument('--clang-lib', default=DEFAULT_CLANG, help='Path to libclang shared library (optional)')
    parser.add_argument('--clang-args', nargs='*', default=['-std=c++17'], help='Extra arguments for clang parser')
    args = parser.parse_args()

    root = parse_path(args.source, clang_lib=args.clang_lib, clang_args=args.clang_args)
    graph = to_graph(root)
    graph.format = 'png'
    graph.render(filename=args.output, cleanup=True)
    print(f'AST image saved to {args.output}')

if __name__ == '__main__':
    main()
