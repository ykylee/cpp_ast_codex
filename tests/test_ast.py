import os
from cpp_ast_codex.ast_builder import parse_source, parse_path
from cpp_ast_codex.visualize import to_graph
from cpp_ast_codex.text import to_text

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


def test_parse_directory(tmp_path):
    file1 = tmp_path / "a.cpp"
    file2 = tmp_path / "b.cpp"
    file1.write_text("int a(){return 1;}")
    file2.write_text("int b(){return 2;}")
    root = parse_path(tmp_path)
    kinds = [child.kind for child in root.children]
    assert root.kind == "DIRECTORY"
    assert "TRANSLATION_UNIT" in kinds


def test_text_output():
    root = parse_source(SAMPLE_CODE, filename="sample.cpp")
    text = to_text(root)
    assert "TRANSLATION_UNIT" in text
    assert "FUNCTION_DECL" in text

