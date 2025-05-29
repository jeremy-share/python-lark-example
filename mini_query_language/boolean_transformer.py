from lark import Transformer, v_args, Token

NUMBER_TYPE = int | float

PRIMITIVE_TYPE = str | int | float | bool | None


class BooleanTransformer(Transformer):
    """
    Transform a parsed expression (tree) into an equivalent boolean expression.
    """

    def __init__(self, context: dict[str, PRIMITIVE_TYPE]):
        super().__init__()
        self.context = context

    @v_args(inline=True)
    def field(self, name_token: Token) -> PRIMITIVE_TYPE:
        return self.context.get(name_token.value)

    @staticmethod
    @v_args(inline=True)
    def number(value: NUMBER_TYPE) -> NUMBER_TYPE:
        return value

    @staticmethod
    @v_args(inline=True)
    def float(token: Token) -> float:
        return float(token.value)

    @staticmethod
    @v_args(inline=True)
    def integer(token: Token) -> int:
        return int(token.value)

    @staticmethod
    @v_args(inline=True)
    def string(token: Token) -> str:
        return token.value[1:-1]  # Strip quotes (single or double)

    @staticmethod
    @v_args(inline=True)
    def boolean(value: bool) -> bool:
        return value

    @staticmethod
    @v_args(inline=True)
    def boolean_true() -> bool:
        return True

    @staticmethod
    @v_args(inline=True)
    def boolean_false() -> bool:
        return False

    @staticmethod
    @v_args(inline=True)
    def equal_to_expr(left: NUMBER_TYPE, right: NUMBER_TYPE) -> bool:
        return left == right

    @staticmethod
    @v_args(inline=True)
    def not_equal_to_expr(left: NUMBER_TYPE, right: NUMBER_TYPE) -> bool:
        return left != right

    @staticmethod
    @v_args(inline=True)
    def greater_then_expr(left: NUMBER_TYPE, right: NUMBER_TYPE) -> bool:
        return left > right

    @staticmethod
    @v_args(inline=True)
    def greater_then_equal_to_expr(left: NUMBER_TYPE, right: NUMBER_TYPE) -> bool:
        return left >= right

    @staticmethod
    @v_args(inline=True)
    def less_then_expr(left: NUMBER_TYPE, right: NUMBER_TYPE) -> bool:
        return left < right

    @staticmethod
    @v_args(inline=True)
    def less_then_equal_to_expr(left: NUMBER_TYPE, right: NUMBER_TYPE) -> bool:
        return left <= right

    @staticmethod
    @v_args(inline=True)
    def not_expr(value: bool) -> bool:
        return not value

    @staticmethod
    @v_args(inline=True)
    def and_expr(left: bool, right: bool) -> bool:
        return left and right

    @staticmethod
    @v_args(inline=True)
    def or_expr(left: bool, right: bool) -> bool:
        return left or right

    @staticmethod
    @v_args(inline=True)
    def bracketed_expr(expression_token: bool) -> bool:
        return expression_token
