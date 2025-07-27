# Lark Syntax Tree

## Boolean Tree Example

When Lark parses an expression, it produces a syntax tree. In our Mini Query Language, all expressions ultimately evaluate to a boolean — meaning that the tree can be "folded" inward from the leaves to produce a `True` or `False` result.

Take the expression:

```text
false or true and true
```

This is parsed into the following tree:

![tree_false_or_true_and_true.png](images/tree_false_or_true_and_true.png)

Operator Precedence: Just like in BEDMAS (order of operations), logical operators have precedence. In our language, `and` binds more tightly than `or`, so the tree evaluates the `and` branch first and becomes:

![tree_false_or_true.png](images/tree_false_or_true.png)

Now `false or true` is evaluated, leaving us with:

![tree_true.png](images/tree_true.png)

---

## Extending the Tree with Comparisons

Since the Mini Query Language is built on boolean logic, other constructs (like comparisons) are also treated as boolean expressions.

For example, take:

```text
country == "New Zealand" and true or false
```

This is parsed into:

![tree_country_==_New_Zealand_and_true_or_false.png](images/tree_country_%3D%3D_New_Zealand_and_true_or_false.png)

### Evaluation Depends on Context

If `country != "New Zealand"`, then the comparison is false, and the tree simplifies to:

```text
false and true or false
```

![tree_false_and_true_or_false.png](images/tree_false_and_true_or_false.png)

If `country == "New Zealand"`, then the comparison is true, and the tree becomes:

```text
true and true or false
```

![tree_true_and_true_or_false.png](images/tree_true_and_true_or_false.png)

And so on!

---

## Summary

- Lark builds structured syntax trees based on grammar rules and precedence.
- The Mini Query Language evaluates expressions from the leaves up.
- Precedence rules are baked into the grammar (e.g., `and` binds tighter than `or`).
- Comparisons like `==` become booleans that slot into logical expressions.

Visualizing the trees helps explain **why** an expression evaluates the way it does, and makes operator precedence obvious.
