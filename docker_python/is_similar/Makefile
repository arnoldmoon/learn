include ./config.env

build:
	docker build -t $(IMG_NAME)\
	             --build-arg PROG_NAME=$(PROG_NAME)\
	             --build-arg BASE=$(BASE)\
	             --build-arg TAG=$(TAG)\
	             .

run:
	docker run -it --rm --name="$(CONTAINER_NAME)" $(IMG_NAME)
shell:
	docker run -it --rm --name="$(CONTAINER_NAME)" $(IMG_NAME) /bin/bash

clean:
	docker rmi -f $(IMG_NAME)
