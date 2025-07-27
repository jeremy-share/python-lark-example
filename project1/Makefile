shell:
	docker compose run --rm -it app bash

build:
	docker compose build

test:
	docker compose run --rm -it app pytest tests/

expression_tree_to_png:
	docker compose run --user="`id -u`" --rm -it app \
		python main-lark-tree-to-png.py "$(expression)"

expression_tree_print:
	docker compose run --user="`id -u`" --rm -it app \
		python main-lark-tree-print.py "$(expression)"
