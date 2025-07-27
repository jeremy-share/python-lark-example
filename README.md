# Mini Query Language Projects (with Lark)

This repository is a collection of progressively more advanced projects demonstrating how to build and evaluate simple
domain-specific languages (DSLs) using [Lark](https://github.com/lark-parser/lark), a Python parsing library.

Each project shows a different level of complexity — starting from basic boolean logic and culminating in a real-world
expression language with comparisons, variable references, parentheses, and full operator precedence.

---

## 📦 Projects Overview

| Project            | Description                                                                                                                                                                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project1`         | A minimal boolean logic parser (true/false, `and`/`or` only). No operator precedence or nesting. Good for demonstrating *flat parsing* and AST processing.                                                                                                     |
| `project999_final` | A full-featured expression language parser supporting field references, comparison operators, parentheses, booleans, numbers, strings, and operator precedence (`not` > `and` > `or`). This mimics common query languages (e.g., feature flags, rule engines). |

---

## ✅ What You’ll Learn

Each project is designed to teach a specific concept:

- **Grammar design** using `.lark` files
- **AST transformation** using `Transformer`
- **Tree inspection** using `Visitor`
- **Left-to-right vs precedence-based parsing**
- **Handling real-world expression use cases** (e.g., `age > 18 and country == "NZ"`)

## 📚 Learning Progression

| Concept                              | `project1`    | `project999_final`       |
|--------------------------------------|---------------|--------------------------|
| Booleans (`true`, `false`)           | ✅             | ✅                        |
| Logical operators (`and`, `or`)      | ✅             | ✅                        |
| Operator precedence                  | ❌ (flat eval) | ✅ (`not` > `and` > `or`) |
| Parentheses                          | ❌             | ✅                        |
| Field references                     | ❌             | ✅                        |
| Comparisons (`==`, `>`, etc)         | ❌             | ✅                        |
| String, number, boolean literals     | ❌             | ✅                        |
| Expression evaluation against a dict | ❌             | ✅                        |
| Variable extraction with Visitor     | ❌             | ✅                        |
| AST visualization                    | ✅             | ✅                        |

## 📄 Related Docs

* [LARK\_SYNTAX\_TREE.md](project999_final/documents/LARK_SYNTAX_TREE.md) — walk-through of how Lark produces syntax
  trees and how they map to evaluation.
* [Lark Official Documentation](https://lark-parser.readthedocs.io/en/latest/)

## 🧪 Example Evaluation

```python
from mini_query_language import evaluate

expression = 'age > 18 and country == "NZ"'
context = {"age": 25, "country": "NZ"}

assert evaluate(expression, context) is True
```

## 📖 License

MIT — see [LICENSE](LICENSE) for details.

