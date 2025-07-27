import click
from src import get_language_parser

def print_tree(node, indent=0):
    spacer = "  " * indent
    if hasattr(node, 'data'):
        print(f"{spacer}{node.data}")
        for child in node.children:
            print_tree(child, indent + 1)
    else:
        print(f"{spacer}{repr(node)}")

@click.command()
@click.argument("expression", required=False)
def main(expression: str | None) -> None:
    """Prints the parse tree for a given EXPRESSION."""
    if not expression:
        expression = click.prompt("Enter an expression", type=str)

    tree = get_language_parser().parse(expression)
    print_tree(tree)


if __name__ == "__main__":
    main()
