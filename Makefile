lint:
	poetry run pylint ./upils --fail-under=6

test:lint
	poetry run python -m unittest discover