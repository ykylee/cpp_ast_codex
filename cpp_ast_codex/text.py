from .ast_builder import ASTNode


def _to_lines(node: ASTNode, prefix: str, is_last: bool) -> list[str]:
    connector = "└── " if is_last else "├── "
    line = f"{prefix}{connector}{node.kind}: {node.spelling}".rstrip()
    lines = [line]
    child_prefix = prefix + ("    " if is_last else "│   ")
    for i, child in enumerate(node.children):
        lines.extend(_to_lines(child, child_prefix, i == len(node.children) - 1))
    return lines


def to_text(node: ASTNode) -> str:
    """Return a textual tree representation of the AST."""
    return "\n".join(_to_lines(node, prefix="", is_last=True))
