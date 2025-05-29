shell:
	docker compose run --rm -it mini_query_language bash

build:
	docker compose build

test:
	docker compose run --rm -it mini_query_language pytest tests/
