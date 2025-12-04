## --------------------------------- Development relevant commands ---------------------------------

.PHONY: help  ## Display this message
help:
	@grep -E \
		'^.PHONY: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".PHONY: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'


## ---------------------------------- Display available commands ----------------------------------

.PHONY: build  ## Build the project via docker
build:
	docker build --no-cache -t playground .

.PHONY: run  ## Run jupyter notebook editor
run:
	docker run -it --rm -p 8888:8888 -v .:/home/jovyan/work --name sandbox playground

.PHONY: clean  ## Clean repo of unversioned files
clean:
	rm .coverage
