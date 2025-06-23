import os
import clang.cindex
from ctypes.util import find_library
from dataclasses import dataclass, field
from typing import List, Optional, Union
from pathlib import Path

_clang_loaded = False

@dataclass
class ASTNode:
    kind: str
    spelling: str
    children: List['ASTNode'] = field(default_factory=list)


def _create_node(cursor: clang.cindex.Cursor) -> ASTNode:
    node = ASTNode(kind=cursor.kind.name, spelling=cursor.spelling or cursor.displayname)
    for child in cursor.get_children():
        node.children.append(_create_node(child))
    return node


def _ensure_clang_loaded(clang_lib: Optional[str]) -> None:
    global _clang_loaded
    if _clang_loaded:
        return

    if clang_lib:
        clang.cindex.Config.set_library_file(clang_lib)
        _clang_loaded = True
        return

    env = os.environ.get("CLANG_LIBRARY_FILE") or os.environ.get("LIBCLANG_PATH")
    if env:
        if os.path.isdir(env):
            clang.cindex.Config.set_library_path(env)
        else:
            clang.cindex.Config.set_library_file(env)
        _clang_loaded = True
        return

    for name in ["clang", "clang-17", "clang-18", "clang-19", "libclang"]:
        lib = find_library(name)
        if lib:
            try:
                clang.cindex.Config.set_library_file(lib)
                _clang_loaded = True
                return
            except Exception:
                pass


def parse_source(code: str, filename: str = "tmp.c", *, clang_lib: Optional[str] = None, clang_args: Optional[List[str]] = None) -> ASTNode:
    _ensure_clang_loaded(clang_lib)
    clang_args = clang_args or []
    index = clang.cindex.Index.create()
    tu = index.parse(filename, args=clang_args, unsaved_files=[(filename, code)], options=0)
    return _create_node(tu.cursor)


def parse_file(path: Union[str, Path], *, clang_lib: Optional[str] = None, clang_args: Optional[List[str]] = None) -> ASTNode:
    """Parse a single file on disk and return its AST."""
    path = Path(path)
    code = path.read_text()
    return parse_source(code, filename=str(path), clang_lib=clang_lib, clang_args=clang_args)


def parse_directory(path: Union[str, Path], *, clang_lib: Optional[str] = None, clang_args: Optional[List[str]] = None) -> ASTNode:
    """Parse all C/C++ source files inside ``path`` and return a combined AST."""
    directory = Path(path)
    root = ASTNode(kind="DIRECTORY", spelling=str(directory))
    for file in sorted(directory.rglob("*")):
        if file.suffix.lower() in {".c", ".cc", ".cpp", ".cxx", ".h", ".hpp", ".hh", ".hxx"} and file.is_file():
            root.children.append(parse_file(file, clang_lib=clang_lib, clang_args=clang_args))
    return root


def parse_path(path: Union[str, Path], *, clang_lib: Optional[str] = None, clang_args: Optional[List[str]] = None) -> ASTNode:
    """Parse a single file or directory and return an AST."""
    p = Path(path)
    if p.is_dir():
        return parse_directory(p, clang_lib=clang_lib, clang_args=clang_args)
    if p.is_file():
        return parse_file(p, clang_lib=clang_lib, clang_args=clang_args)
    raise FileNotFoundError(path)
