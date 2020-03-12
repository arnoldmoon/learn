env ?= config.env
include $(env)

build:
	docker build -t $(IMG_NAME) .

run:
	docker run -it --rm --env-file=./config.env --name="$(CONTAINER_NAME)" $(IMG_NAME)
shell:
	docker run -it --rm --env-file=./config.env --name="$(CONTAINER_NAME)" $(IMG_NAME) /bin/bash

clean:
	docker rmi -f $(IMG_NAME)
