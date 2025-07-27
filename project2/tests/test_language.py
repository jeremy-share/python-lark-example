import pytest

from src import evaluate


@pytest.mark.parametrize("expression,expected", [
    ("true", True),
    ("false", False),
    # Full tests are in test_boolean_transformer.py
])
def test_expressions(
    expression: str,
    expected: str,
):
    assert evaluate(expression) == expected
