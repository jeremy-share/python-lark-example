from lark import Transformer, v_args, Token

class BooleanTransformer(Transformer[Token, bool]):
    """
    Transform a parsed expression (tree) into an equivalent boolean expression.
    """

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
