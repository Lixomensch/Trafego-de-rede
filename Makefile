include .env
.PHONY: pylint isort activeblack format check prepare-commit

#* Python Rules
server:
	python src/backend/app.py

client:
	streamlit run src/frontend/streamlit_app.py

#* Git Rules
isort:
	isort --settings-path=$(MAKE_CONFIG_FILE) $(FORMAT_CHECK_SRC)

pylint:
	pylint --rcfile=$(PYLINT_CONFIG_FILE) $(FORMAT_CHECK_SRC)

activeblack:
	black $(FORMAT_CHECK_SRC)

format: activeblack isort

check: pylint isort

prepare-commit: format check