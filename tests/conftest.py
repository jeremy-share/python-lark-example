import pytest
from lark import Lark

from mini_query_language import get_mini_query_language_parser


@pytest.fixture(name="lark_parser", scope="session")
def fixture_lark_parser() -> Lark:
    return get_mini_query_language_parser()
