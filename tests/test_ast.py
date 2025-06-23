import os
from cpp_ast_codex.ast_builder import parse_source
from cpp_ast_codex.visualize import to_graph

SAMPLE_CODE = """\
int add(int a, int b) {
    return a + b;
}

int main() {
    return add(1, 2);
}
"""

def test_parse_root_translation_unit():
    root = parse_source(SAMPLE_CODE, filename="sample.cpp")
    assert root.kind == "TRANSLATION_UNIT"
    kinds = [child.kind for child in root.children]
    assert "FUNCTION_DECL" in kinds

def test_graph_generation(tmp_path):
    root = parse_source(SAMPLE_CODE, filename="sample.cpp")
    graph = to_graph(root)
    output = tmp_path / "ast"
    graph.format = 'png'
    graph.render(filename=str(output), cleanup=True)
    assert os.path.exists(str(output) + '.png')

