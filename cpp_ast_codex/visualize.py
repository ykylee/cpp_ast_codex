from .ast_builder import ASTNode
import graphviz


def _add_nodes(dot: graphviz.Digraph, node: ASTNode, parent_id: str):
    node_id = str(id(node))
    label = f"{node.kind}\n{node.spelling}".strip()
    dot.node(node_id, label)
    if parent_id:
        dot.edge(parent_id, node_id)
    for child in node.children:
        _add_nodes(dot, child, node_id)


def to_graph(node: ASTNode) -> graphviz.Digraph:
    dot = graphviz.Digraph()
    _add_nodes(dot, node, parent_id='')
    return dot
