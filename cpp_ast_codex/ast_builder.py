import os
import clang.cindex
from ctypes.util import find_library
from dataclasses import dataclass, field
from typing import List, Optional

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
    if clang_lib:
        clang.cindex.Config.set_library_file(clang_lib)
        return

    env = os.environ.get("CLANG_LIBRARY_FILE") or os.environ.get("LIBCLANG_PATH")
    if env:
        if os.path.isdir(env):
            clang.cindex.Config.set_library_path(env)
        else:
            clang.cindex.Config.set_library_file(env)
        return

    for name in ["clang", "clang-17", "clang-18", "clang-19", "libclang"]:
        lib = find_library(name)
        if lib:
            try:
                clang.cindex.Config.set_library_file(lib)
                return
            except Exception:
                pass


def parse_source(code: str, filename: str = "tmp.c", *, clang_lib: Optional[str] = None, clang_args: Optional[List[str]] = None) -> ASTNode:
    _ensure_clang_loaded(clang_lib)
    clang_args = clang_args or []
    index = clang.cindex.Index.create()
    tu = index.parse(filename, args=clang_args, unsaved_files=[(filename, code)], options=0)
    return _create_node(tu.cursor)
