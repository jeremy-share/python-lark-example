import os

from lark import Lark

from src.boolean_transformer import BooleanTransformer


def get_language_parser() -> Lark:
    project_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/..")
    with open(f"{project_dir}/grammar.lark") as f:
        grammar = f.read()
    return Lark(grammar, start="start", parser="lalr")


def evaluate(expression: str) -> bool:
    lark_parser = get_language_parser()
    tree = lark_parser.parse(expression)
    result = BooleanTransformer().transform(tree)
    return result
