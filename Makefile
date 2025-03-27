TOPDIR:=	$(abspath .)
SRCDIR=		$(TOPDIR)/src
SOURCE=		$(SRCDIR)/ciso_aac

reformat:
	# sort imports and remove unused imports
	uv tool run ruff check --select F401,I --fix
	# reformat
	uv tool run ruff format
	# make an extended check with rules that might be triggered by reformat
	uv tool run ruff check

typecheck:
	MYPYPATH=$(SRCDIR) uv tool run mypy -p ciso_aac

update_deps:
	@echo "Updating ALL the dependencies"
	uv lock --upgrade

dev_sync_deps:
	uv sync

clean:
	rm -rf .pytest_cache .coverage .mypy_cache .cache .eggs
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

regenerate_source: ciso-aa.yaml
	uv tool run openapi-python-client generate --meta none --overwrite --path ciso-aa.yaml --output-path src/ciso_aac
