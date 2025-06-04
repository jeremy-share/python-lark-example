import pytest
from lark import Lark

from mini_query_language.variable_collector_visitor import VariableCollectorVisitor


@pytest.mark.parametrize("expression,variables,variables_count", [
    ("true", set(), {}),
    ("false", set(), {}),
    ("true or false", set(), {}),
    ("true and false or true", set(), {}),
    ("true and (false or true)", set(), {}),
    ("true or false and false", set(), {}),
    ("subscribed", {"subscribed"}, {"subscribed": 1}),
    ("subscribed or (age <= 20 and not subscribed)", {"subscribed", "age"}, {"subscribed": 2, "age": 1}),
    ("age > 18", {"age"}, {"age": 1}),
    ("height < 185.5", {"height"}, {"height": 1}),
    ("days_till_birthday > -1", {"days_till_birthday"}, {"days_till_birthday": 1}),
    ("retirement < -99.5", {"retirement"}, {"retirement": 1}),
    ("country == \"NZ\"", {"country"}, {"country": 1}),
    ("not subscribed", {"subscribed"}, {"subscribed": 1}),
    (
        "(age > 18 or country == \"AU\") and subscribed",
        {"age", "country", "subscribed"},
        {"age": 1, "country": 1, "subscribed": 1}
    ),
    (
        "((age > 18 or country == \"AU\") and subscribed) or (country == \"EU\" and age > 20) or (age > 25)",
        {"age", "country", "subscribed"},
        {"age": 3, "country": 2, "subscribed": 1}
    ),
])
def test_expressions(
    expression: str,
    variables: set[str],
    variables_count: dict[str, int],
    lark_parser: Lark,
):
    tree = lark_parser.parse(expression)
    variable_collector_visitor = VariableCollectorVisitor()
    variable_collector_visitor.visit(tree)
    assert variable_collector_visitor.get_variables() == variables
    assert variable_collector_visitor.get_variables_count() == variables_count
