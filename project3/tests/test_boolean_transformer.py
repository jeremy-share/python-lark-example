
import pytest
from lark import Lark

from src.boolean_transformer import BooleanTransformer


@pytest.mark.parametrize("expression,context,expected", [
    ("true", {}, True),
    ("false", {}, False),
    ("true or false", {}, True),
    ("true and false or true", {}, True),
    ("true and (false or true)", {}, True),
    ("true or false and false", {}, True),
    ("true or false and false", {}, True),
    ("(true or false) and false", {}, False),
    ("subscribed", {"subscribed": True}, True),
    ("subscribed", {"subscribed": False}, False),
    ("not subscribed", {"subscribed": False}, True),
    ("not subscribed", {"subscribed": True}, False),
    ("not true", {}, False),
    ("not false", {}, True),
])
def test_expressions(
    expression: str,
    context: dict[str, bool],
    expected: str,
    lark_parser: Lark,
):
    tree = lark_parser.parse(expression)
    result = BooleanTransformer(context).transform(tree)
    assert result == expected
