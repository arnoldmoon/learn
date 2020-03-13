include ./config.env

build:
	docker build -t $(IMG_NAME)\
	             --build-arg BASE=$(BASE)\
	             --build-arg TAG=$(TAG)\
	             .

run:
	docker run -dit --rm --name "$(CONTAINER_NAME)"\
	           -p 8080:8080\
	           -p 1666:1666\
                   --mount src=$(STORAGE),dst=/data\
	           -h perforce\
	           $(IMG_NAME)
shell:
	docker exec -it "$(CONTAINER_NAME)" /bin/bash

clean:
	docker rmi -f $(IMG_NAME)
	docker volume rm $(STORAGE)
