import os
from typing import Any

from lark import Lark

from mini_query_language.boolean_transformer import BooleanTransformer


def get_mini_query_language_parser() -> Lark:
    project_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/..")
    with open(f"{project_dir}/mini_query_language.lark") as f:
        grammar = f.read()
    return Lark(grammar, start="start", parser="lalr")


def evaluate(expression: str, context: dict[str, Any] | None = None) -> bool:
    context = {} if context is None else context
    lark_parser = get_mini_query_language_parser()
    tree = lark_parser.parse(expression)
    result = BooleanTransformer(context).transform(tree)
    return result
