from collections import Counter

from lark import Visitor, v_args, Tree


class VariableCollectorVisitor(Visitor):
    """
    Takes a parsed expression (tree) and extracts all the variables with counts.
    """

    def __init__(self):
        self.variables = Counter()

    @v_args(inline=True)
    def field(self, name_branch: Tree):
        self.variables[name_branch.children[0].value] += 1

    def get_variables(self) -> set[str]:
        return set(self.variables.keys())

    def get_variables_count(self) -> dict[str, int]:
        return dict(self.variables)
