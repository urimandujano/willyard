.PHONY: help

define HELPTEXT
Run "make <target>" where <target> is one of
 help:		to print this message
 test:		to run the test suite
 worker: 	to run the willyard worker
endef
export HELPTEXT

help:
	@echo "$$HELPTEXT"

test:
	poetry run pytest --cov=willyard

worker:
	poetry run python willyard/worker/main.py
