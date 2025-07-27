import click
from lark.tree import pydot__tree_to_png
from mini_query_language import get_mini_query_language_parser

@click.command()
@click.argument("expression", required=False)
@click.option("--output", "-o", help="Output PNG filename")
def main(expression: str | None, output: str | None) -> None:
    """Generate a PNG of the parse tree for a given EXPRESSION."""
    if not expression:
        expression = click.prompt("Enter an expression", type=str)
    if output is None:
        output = f"tree_{expression.replace(' ', '_')}.png"

    tree = get_mini_query_language_parser().parse(expression)
    pydot__tree_to_png(tree, output)
    print(f"Parse tree saved to {output}")

if __name__ == "__main__":
    main()
