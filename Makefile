# This will be changed to pac-man.py later on
# AS THE SUBJECT ASK FOR IT.
NAME = main.py

UV = uv
VENV = .venv

PYTHON = $(BIN_DIR)/python
MYPY = $(BIN_DIR)/mypy
FLAKE = $(BIN_DIR)/flake8

install:
	$(UV) sync
	$(UV) pip install wheel/mlx-2.2-py3-none-any.whl

run:
	$(UV) run python $(NAME)

debug:
	$(UV) run python -m pdb $(NAME)

clean:
	find . -name "*.pyc" -exec rm -rf {} +
	find . -type d \( -name "__pycache__" -o -name ".mypy_cache" \) -exec rm -rf {} +

fclean: clean
	rm -rf $(VENV)

re: fclean install

.PHONY: install run fclean re clean debug
