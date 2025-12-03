TOPDIR:=$(abspath .)
SRCDIR=$(TOPDIR)/src
PYTHON=$(shell which python)
UV=$(shell which uv)

test:
	$(UV) run pytest --log-cli-level DEBUG

reformat:
	# sort imports and remove unused imports
	$(UV) tool run ruff check --select F401,I --fix
	# reformat
	$(UV) tool run ruff format
	# make an extended check with rules that might be triggered by reformat
	$(UV) tool run ruff check --config ruff-extended.toml

typecheck:
	$(UV) tool run mypy --install-types --non-interactive --pretty --ignore-missing-imports --warn-unused-ignores $(SRCDIR)

update_deps:
	@echo "Updating ALL the dependencies"
	$(UV) lock --upgrade

dev_sync_deps:
	$(UV) sync

build: clean
	$(UV) build

clean:
	rm -rf dist/ build/ *.egg-info src/*.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

tag_version:
	@NEW_VERSION=$$(grep "^version =" pyproject.toml | cut -d'=' -f2 | tr -d '" '); \
	if [ -z "$$NEW_VERSION" ]; then echo "Error: Could not determine new version"; exit 1; fi; \
	echo "Setting version to $$NEW_VERSION"; \
	git add pyproject.toml; \
	git commit -m "Version $$NEW_VERSION"; \
	git tag v$$NEW_VERSION
