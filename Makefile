# This is our project's Makefile

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Say hello
.PHONY: install_cowsay
install_coway:
	pip install cowsay

.PHONY: hello
hello: install_cowsay ## Say our team name
	cowsay "Go team A+Sync!"
