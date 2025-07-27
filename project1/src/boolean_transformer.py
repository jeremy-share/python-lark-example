from lark import Transformer, v_args, Token

class BooleanTransformer(Transformer):
    """
    Transform a parsed expression (tree) into an equivalent boolean expression.
    """
    @staticmethod
    @v_args(inline=True)
    def boolean(value: bool) -> bool:
        return value

    @staticmethod
    @v_args(inline=True)
    def boolean_false() -> bool:
        return False

    @staticmethod
    @v_args(inline=True)
    def boolean_true() -> bool:
        return True

    @staticmethod
    def expr(args: list[bool | Token]) -> bool:
        # Start with the first operand
        result = args[0]

        # Process alternating operator / operand pairs
        for i in range(1, len(args), 2):
            op = args[i]
            right = args[i + 1]

            if op == Token("BOOL_OP", "and"):
                result = result and right
            elif op == Token("BOOL_OP", "or"):
                result = result or right
            else:
                raise ValueError(f"Unknown operator: {op}")

        return result
