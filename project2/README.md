# Boolean Expression Parser with Precedence (Lark Project 2)

This project demonstrates a simple boolean expression language parser using [Lark](https://github.com/lark-parser/lark) that supports:

- Boolean literals (`true`, `false`)
- Logical operators: `not`, `and`, `or`
- Proper **operator precedence**
- **Parentheses** for explicit grouping

It builds upon the concepts from `project1`, introducing precedence-aware grammar and tree-based evaluation.

---

## 🔍 Supported Language Features

### ✅ Boolean literals
```text
true
false
````

### ✅ Logical operators (with precedence)

| Operator   | Description        | Precedence  |
|------------|--------------------|-------------|
| `not`      | Negation (unary)   | High        |
| `and`      | Logical AND        | Medium      |
| `or`       | Logical OR         | Low         |

### ✅ Parentheses for grouping

```text
true and (false or true)
not (true and false)
```

---

## 🧠 Operator Precedence Examples

| Expression                   | Interpreted As               | Result   |
|------------------------------|------------------------------|----------|
| `true or false and false`    | `true or (false and false)`  | `true`   |
| `not true or false`          | `(not true) or false`        | `false`  |
| `true and false or true`     | `(true and false) or true`   | `true`   |
| `true and (false or true)`   | `true and (false or true)`   | `true`   |

---

## 🛠 Usage

### 🔄 Build the container

```bash
make build
```

### 🐚 Open a shell

```bash
make shell
```

### ✅ Run tests

```bash
make test
```

### 🌳 View parse tree in terminal

```bash
make expression_tree_print expression='not true or false'
```

### 📦 Export parse tree to PNG

```bash
make expression_tree_to_png expression='true and (false or true)'
```

This generates a file like `tree_true_and_(false_or_true).png`.

---

## 🔧 Grammar Overview

The grammar is defined in [`grammar.lark`](./grammar.lark)

## 🧪 How Evaluation Works

Evaluation is handled by a custom [Transformer](./src/boolean_transformer.py), which reduces the tree to a final boolean value.

Example usage:

```python
from src import evaluate

expression = 'true and (false or true)'
result = evaluate(expression)  # => True
```

## 📚 Learning Goals

* Learn how to define operator precedence in Lark
* Understand the structure of recursive descent grammar
* See how parenthesized expressions override default precedence
* Visualize abstract syntax trees (ASTs) to understand evaluation

---

## 📁 Project Structure

```
.
├── grammar.lark                # Lark grammar definition
├── src/
│   ├── __init__.py             # Parser and evaluator
│   └── boolean_transformer.py  # AST transformer logic
├── tests/                      # Pytest test cases
├── main-lark-tree-print.py     # Pretty-prints syntax tree to terminal
├── main-lark-tree-to-png.py    # Exports syntax tree to PNG using Graphviz
├── Makefile                    # Dev tasks (shell, build, test, tree)
└── requirements.in             # Python dependencies
```
