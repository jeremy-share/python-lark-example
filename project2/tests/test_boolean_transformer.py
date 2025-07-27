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
    ("true and (false or true)", True),
    ("true and false or true", True),
    ("true and (true or false)", True),
    ("true and false or false", False),
    ("true and true or false", True),
    ("true and true or true", True),
    ("false and false or false", False),
    ("true and false or true", True),
    ("true or false and false", True),
    ("true or false and false", True),
    ("not(true or true)", False),
    ("not(false or false)", True),
    ("not(not(false or false))", False),
    ("not(not(not(false or false)))", True),
])
def test_expressions(
        expression: str,
        expected: str,
        lark_parser: Lark,
):
    tree = lark_parser.parse(expression)
    result = BooleanTransformer().transform(tree)
    assert result == expected
