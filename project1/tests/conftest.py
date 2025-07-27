import pytest
from lark import Lark

from src import get_language_parser


@pytest.fixture(name="lark_parser", scope="session")
def fixture_lark_parser() -> Lark:
    return get_language_parser()
