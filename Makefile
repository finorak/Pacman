# This will be changed to pac-man.py later on
# AS THE SUBJECT ASK FOR IT.
NAME = main.py

UV = uv
VENV = .venv

install:
	$(UV) sync
	$(UV) pip install ./wheel/mlx-2.4-py3-none-any.whl

run:
	$(UV) run $(NAME)

debug:
	$(UV) run python -m pdb $(NAME)

clean:
	find . -name "*.pyc" -exec rm -rf {} +
	find . -type d \( -name "__pycache__" -o -name ".mypy_cache" \) -exec rm -rf {} +

fclean: clean
	rm -rf $(VENV)

lint:
	$(UV) run flake8 . --exclude=$(VENV)
	$(UV) run mypy mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs --exclude=$(VENV)

lint:
	$(UV) run flake8 . --exclude=$(VENV)
	$(UV) run mypy --strict . --exclude=$(VENV)

re: fclean install

.PHONY: install run fclean re clean debug
