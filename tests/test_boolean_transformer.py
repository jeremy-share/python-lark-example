from typing import Any

import pytest
from lark import Lark

from mini_query_language.boolean_transformer import BooleanTransformer


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
    ("age > 18", {"age": 20}, True),
    ("age <= 18", {"age": 17}, True),
    ("height < 185.5", {"height": 185.9}, False),
    ("days_till_birthday > -1", {"days_till_birthday": 2}, True),
    ("retirement < -99.5", {"retirement": 185.9}, False),
    ("children == 0", {"children": 0}, True),
    ("children == -0", {"children": 0}, True),
    ("height < 185.5", {"height": 110.4}, True),
    ("height <= 185.5", {"height": 185.5}, True),
    ("height >= 110.2", {"height": 110.2}, True),
    ("country == \"NZ\"", {"country": "NZ"}, True),
    ("country != \"AU\"", {"country": "NZ"}, True),
    ("not subscribed", {"subscribed": False}, True),
    ("not subscribed", {"subscribed": True}, False),
    ("not true", {}, False),
    ("not false", {}, True),
    ("not height <= 185.5", {"height": 185.5}, False),
    ("not height >= 110.2", {"height": 110.5}, False),
    ("age > 18 and country == \"NZ\"", {"age": 20, "country": "NZ"}, True),
    ("age > 18 and country == \"AU\"", {"age": 20, "country": "NZ"}, False),
    ("age > 18 or country == \"AU\"", {"age": 16, "country": "NZ"}, False),
    ("(age > 18 or country == \"AU\") and subscribed", {"age": 16, "country": "AU", "subscribed": True}, True),
])
def test_expressions(
        expression: str,
        context: dict[str, Any],
        expected: str,
        lark_parser: Lark,
):
    tree = lark_parser.parse(expression)
    result = BooleanTransformer(context).transform(tree)
    assert result == expected
