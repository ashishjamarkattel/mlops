# Makefile
SHELL = /bin/bash

target: prerequisites
<TAB> recipe

## Environment
venv:
	python3 -m venv venv
	source venv/Scripts/activate && \
	python3 -m pip install pip steuptools wheel && \
	python3 -m pip install -e .

# && signifies that we want these commands to execute in one shel

.PHONY: help
help:
    @echo "Commands:"
    @echo "venv    : creates a virtual environment."
    @echo "style   : executes style formatting."
    @echo "clean   : cleans all unnecessary files."
