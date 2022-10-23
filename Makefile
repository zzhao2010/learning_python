install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py libs

test:
	python -m pytest -vv --cov=libs test_*.py

format:
	black *.py libs/*.py

all: install lint test format