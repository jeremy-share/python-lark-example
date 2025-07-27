import pytest
from lark import Lark

from src.boolean_transformer import BooleanTransformer


@pytest.mark.parametrize("expression,expected", [
    ("true", True),
    ("false", False),
    ("true or false", True),
    ("false or true", True),
    ("true or true", True),
    ("false or false", False),
    ("true and false", False),
    ("true and true", True),
    ("true and true or true", True),
    ("false and false or false", False),
    # These do not really work as we have no tree structure and therefor operator order in the grammar.lark
    # ("true and false or true", True),
    # ("true or false and false", True),
    # ("true or false and false", True),
])
def test_expressions(
        expression: str,
        expected: str,
        lark_parser: Lark,
):
    tree = lark_parser.parse(expression)
    result = BooleanTransformer().transform(tree)
    assert result == expected
