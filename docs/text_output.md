# Text Output Module

`cpp_ast_codex/text.py` provides a simple textual tree representation of the AST produced by `ast_builder`.

```
└── TRANSLATION_UNIT: sample.cpp
    ├── FUNCTION_DECL: add
    │   └── COMPOUND_STMT:
    │       └── RETURN_STMT:
    └── FUNCTION_DECL: main
```

Use the `print_ast.py` script to generate this view from the command line:

```bash
./print_ast.py samples/hello.cpp
```
