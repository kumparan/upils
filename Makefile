lint:
	poetry run pylint ./upils --fail-under=6

test:lint
	poetry run python -m unittest discover

publish:
	poetry publish --build

format-all-files:
	poetry run black .
	poetry run isort .
