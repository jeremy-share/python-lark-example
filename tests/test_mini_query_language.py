from typing import Any

import pytest

from mini_query_language import evaluate


@pytest.mark.parametrize("expression,context,expected", [
    ("true", {}, True),
    ("false", {}, False),
    # Full tests are in test_boolean_transformer.py
])
def test_expressions(
        expression: str,
        context: dict[str, Any],
        expected: str,
):
    assert evaluate(expression) == expected
