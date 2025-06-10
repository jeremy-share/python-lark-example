# Mini Query Language Parser (with Lark)

This is a sample project to demonstrate how to use [Lark](https://github.com/lark-parser/lark) to parse and evaluate a
made-up language.

This mini language supports boolean logic, comparisons, parentheses, and literals.

It's designed to showcase how to build a parser with operator precedence and evaluate the result against a data object
(e.g., a dictionary).

## ✨ Example Expressions

`age > 18 and country == "NZ"`
`subscribed == true or (age <= 13 and parental_consent == true)`
`not (status == "inactive")`

## 🧠 Human-Readable Language Rules

1. Fields:
   
    Fields are identifiers such as age, status, or country.
    
    They represent keys in a data dictionary that the expression is evaluated against.

    `age, status, subscribed`


2. Literals:
You can compare fields against the following types of literal values:

   * Strings
   
     Either double-quoted (`"NZ"`) or single-quoted (`'NZ'`)
   
     Supports basic escape sequences (in double quotes) and minimal escaping (in single quotes).

     ```text
     country == "NZ"
     status == 'inactive'
     ```

   * Numbers
     * Integers (e.g., `42`, `-10`)
     * Floats (e.g., `3.14`, `-0.01`)
    ```text
    age > 18
    score >= 99.5
    ```

   * Booleans
   
   Case-sensitive true or false (must be lowercase)

    ```text
    subscribed == true
    not verified
    ```

## 🧠 Human-Readable Language Rules

This language is designed to express logical conditions over structured data, like Python dictionaries. Here's what you can do:

---

### 1. **Fields**
Fields are identifiers such as `age`, `status`, or `country`.  
They represent keys in a data dictionary that the expression is evaluated against.

Example:
```text
age, status, subscribed
```

---

### 2. **Literals**

You can compare fields against the following types of **literal values**:

- **Strings**  
  Either double-quoted (`"NZ"`) or single-quoted (`'NZ'`)  
  Supports basic escape sequences (in double quotes) and minimal escaping (in single quotes).

  ```text
  country == "NZ"
  status == 'inactive'
  ```

- **Numbers**
    - **Integers** (e.g., `42`, `-10`)
    - **Floats** (e.g., `3.14`, `-0.01`)

  ```text
  age > 18
  score >= 99.5
  ```

- **Booleans**  
  Case-sensitive `true` or `false` (must be lowercase)

  ```text
  subscribed == true
  not verified
  ```

---

### 3. **Comparison Operators**

Compare two expressions using:

| Operator | Meaning             |
|----------|---------------------|
| `==`     | Equal to            |
| `!=`     | Not equal to        |
| `<`      | Less than           |
| `<=`     | Less than or equal  |
| `>`      | Greater than        |
| `>=`     | Greater or equal    |

Comparisons can be between any two **factors**, which may be:
- A field
- A literal (string, number, boolean)
- A grouped expression (e.g., `(x > 5)`)

Example:
```text
age >= 16
status != 'inactive'
score == 100.0
```

---

### 4. **Logical Operators**

You can build complex conditions using:

- `and`: both sides must be true
- `or`: at least one side must be true
- `not`: negates the following expression

Examples:
```text
age > 18 and country == "NZ"
not subscribed
```

---

### 5. **Parentheses**

Group expressions to override default precedence:

```text
(age < 13 or age > 65) and consent == true
not (status == 'inactive' or expired)
```

---

### 6. **Operator Precedence (Binding Strength)**

In order from **strongest** to **weakest**:

1. `not` (unary)
2. `and`
3. `or`

This means:
```text
true and false or true
```
is interpreted as:
```text
(true and false) or true
```

Use parentheses to make evaluation order explicit.


---

## 🧪 Evaluator Behavior

Once parsed, expressions can be evaluated against Python dictionaries. For example:

```python
from mini_query_language import get_mini_query_language_parser
from mini_query_language.boolean_transformer import BooleanTransformer

expression = 'age > 18 and country == "NZ"'
context = {"age": 25, "country": "NZ"}

lark_parser = get_mini_query_language_parser()
tree = lark_parser.parse(expression)
result = BooleanTransformer(context).transform(tree)  # => True
```

or simply

```python
from mini_query_language import evaluate

expression = 'age > 18 and country == "NZ"'
context = {"age": 25, "country": "NZ"} 
evaluate(expression, context)  # => True

```

## 📄 How it works?

Checkout:
* [LARK_SYNTAX_TREE.md](documents/LARK_SYNTAX_TREE.md)
* https://lark-parser.readthedocs.io/en/stable/

## ✅ Why This Project?

This project is a good starting point for learning how to:

- Design a custom grammar
- Parse expressions with operator precedence
- Build and evaluate an abstract syntax tree (AST)
- Apply rules to structured data
