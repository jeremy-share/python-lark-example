# Boolean Expression Language with Variables (Lark Project 3)

This project builds on top of earlier expression parsers by introducing **variables** that represent booleans.

It uses [Lark](https://github.com/lark-parser/lark) to parse and evaluate simple logical expressions that include:

- `true`, `false` literals
- `not`, `and`, `or` operators (with proper precedence)
- **Variables** like `subscribed`, `is_admin`, etc., resolved against a provided context (`dict`)

---

## ✅ What This Project Supports

- ✅ Boolean literals (`true`, `false`)
- ✅ Unary `not`, binary `and`, `or`
- ✅ Parentheses for grouping
- ✅ Variables (`age_verified`, `is_admin`, etc.)
- ✅ Context-based evaluation (`{"is_admin": True}`)

---

## 🧪 Example Expressions

| Expression                        | Evaluated Against                                  | Result  |
|-----------------------------------|----------------------------------------------------|---------|
| `true`                            | `{}`                                               | `True`  |
| `subscribed`                      | `{"subscribed": True}`                             | `True`  |
| `not subscribed`                  | `{"subscribed": False}`                            | `True`  |
| `subscribed and is_admin`         | `{"subscribed": True, "is_admin": True}`           | `True`  |
| `subscribed and not is_admin`     | `{"subscribed": True, "is_admin": False}`          | `True`  |
| `true or false and false`         | `{}`                                               | `True`  |
| `(true or false) and false`       | `{}`                                               | `False` |


## 🧠 Operator Precedence

From strongest to weakest:

1. `not`
2. `and`
3. `or`

Use parentheses to override evaluation order.

---

## 🧪 Running the Project

### 🔧 Build the container

```bash
make build
```

### 🐚 Start a shell

```bash
make shell
```

### ✅ Run tests

```bash
make test
```

### 📤 Visualize the syntax tree

```bash
make expression_tree_print expression='not subscribed or true'
```

Or generate a PNG:

```bash
make expression_tree_to_png expression='(subscribed or is_admin) and not suspended'
```

## 🧰 Example Usage in Code

```python
from src import evaluate

ctx = {"subscribed": True, "is_admin": False}
assert evaluate("subscribed and not is_admin", ctx)
```

## 🧭 Project Structure

```
.
├── grammar.lark                # Lark grammar file
├── src/
│   ├── __init__.py             # Parser + evaluation interface
│   └── boolean_transformer.py  # Lark Transformer for evaluation
├── tests/                      # Pytest test cases
├── main-lark-tree-print.py     # Pretty-prints parse tree
├── main-lark-tree-to-png.py    # Renders parse tree to PNG (Graphviz)
├── Makefile                    # Dev tasks: test, shell, build, visualizers
└── requirements.in             # Python dependencies
```
