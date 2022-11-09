.DEFAULT_GOAL := help
help:
	@perl -nle'print $& if m{^[a-zA-Z_-|.]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

format: ## Format Python
	black --exclude="/(dist|build|__pycache__|venv|\.git)/" .
