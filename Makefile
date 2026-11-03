# Makefile:jeff
#

USER="i8degrees"
TAG=$(shell cat .version || echo "1.0.0")
IMAGE="$(USER)/discord-bot"

all: build

# Build docker image
# TODO(JEFF): Add the VERSION argument to the build for proper version
# tracking.
build:
	@echo $(IMAGE):$(TAG)
	docker compose build

# Run docker image
run:
	@echo $(IMAGE):$(TAG)
	docker compose up -d

# Restart container
restart:
	@echo $(IMAGE):$(TAG)
	docker compose restart

# Follow the logging output of the container
logs:
	@echo $(IMAGE):$(TAG)
	docker compose logs -f

# Push container to public registry
push:
	@echo $(IMAGE):$(TAG)
	docker compose push

# Pull a pre-built container image
pull:
	@echo $(IMAGE):$(TAG)
	docker compose pull

