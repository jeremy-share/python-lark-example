from lark import Transformer, v_args, Token

class TokenCounter(Visitor_Recursive[Token]):
    """
    Counts various tokens
    """

    def __init__(self):
        self.count_boolean = 0
        self.count_boolean_true = 0
        self.count_boolean_false = 0

    @staticmethod
    @v_args(inline=True)
    def boolean(value: bool) -> None:
        self.count_boolean += 1

    @staticmethod
    @v_args(inline=True)
    def boolean_true() -> None:
        self.count_boolean_true += 1

    @staticmethod
    @v_args(inline=True)
    def boolean_false() -> None:
        self.count_boolean_false += 1
