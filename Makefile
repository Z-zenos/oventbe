run:
	uvicorn src.main:app --reload

lint:
	poetry run pre-commit run --all
