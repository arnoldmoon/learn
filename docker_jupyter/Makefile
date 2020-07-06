include ./config.env

build:
	docker build -t $(IMG_NAME)\
				 --build-arg BASE=$(BASE)\
				 --build-arg TAG=$(TAG)\
				 .

run:
	docker run -dit --rm --name "$(CONTAINER_NAME)"\
			   -p 8888:8888\
			   --mount type=bind,src="$(STORAGE)",dst=/home/jovyan/work\
			   -h jupyter\
			   $(IMG_NAME)
shell:
	docker exec -it "$(CONTAINER_NAME)" /bin/bash

stop:
	docker stop "$(CONTAINER_NAME)"

clean:
	docker rmi -f $(IMG_NAME)
