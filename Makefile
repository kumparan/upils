lint:
	poetry run pylint ./upils --fail-under=6

test:lint
	poetry run python -m unittest discover

publish:
	poetry publish --build

format-all-files:
	poetry run black .
	poetry run isort .

changelog_args=-o CHANGELOG.md -tag-filter-pattern '^v'

changelog:
ifdef version
	$(eval changelog_args=--next-tag $(version) $(changelog_args))
endif
	git-chglog $(changelog_args)