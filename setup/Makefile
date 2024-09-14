user=$$(whoami)
uid=$$(id -u $(user))
gid=$$(id -g $(user))

.PHONY: cs4200/image

all: cs4200/image

cs4200/image:
	docker build . -t $@ --build-arg developer=$(user) --build-arg uid=$(uid) --build-arg gid=$(gid)
