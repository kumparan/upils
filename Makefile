lint:
	poetry run pylint ./kum_utils --fail-under=6

test:
	poetry run python -m unittest discover