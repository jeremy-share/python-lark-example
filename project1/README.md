# Simple Boolean Language Parser (with Lark)

This is a minimal parser project using [Lark](https://github.com/lark-parser/lark) to demonstrate how to parse and evaluate simple boolean expressions written in a custom DSL (domain-specific language).

This project is a learning-focused introduction to building your own parser and transformer — great for teaching how a parser works without the complexities of operator precedence, parentheses, or nested expressions.

---

## ✅ What This Project Supports

The grammar supports:

- **Boolean literals**: `true`, `false`
- **Logical operators**: `and`, `or`
- **Flat expressions only** (evaluated left to right, no parentheses or operator precedence)

Example valid expressions:
```text
true
false
true and false
true or false and true  # evaluated left to right!
````

---

## ❌ What This Project Does *Not* Support

* Parentheses or nesting
* Operator precedence (`and` does NOT bind tighter than `or`)
* Field references, comparisons, or other data types

The goal is to keep the grammar and AST transformation as **simple and transparent** as possible.

---

## 🛠️ Usage

### Shell access

Start a shell in the container:

```bash
make shell
```

### Run tests

```bash
make test
```

### Visualize parse tree

Print to console:

```bash
make expression_tree_print expression='true and false or true'
```

```bash
make expression_tree_to_png expression='true or false and false'
```

The PNG file will be saved as something like:

```bash
tree_true_or_false_and_false.png
```

## 🧠 Implementation Details

### Evaluation Logic

* The `BooleanTransformer` processes the expression **from left to right**.
* Logical operators are applied in the order they appear — this is intentional to show what happens *without* precedence.

## 📚 Learning Goals

* Understand how to define a simple grammar in Lark
* Parse an input string into a syntax tree
* Transform that tree into a Python boolean expression
* Learn why *operator precedence* matters by seeing what happens when it's missing
