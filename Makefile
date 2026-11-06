# Makefile:jeff
#

USER=i8degrees
TAG=$(shell cat .version || echo "1.0.0")
IMAGE=$(USER)/markdown-link-preview-bot

all: build

# Build docker image
build:
	@echo $(IMAGE):$(TAG)
	docker compose build --build-arg VERSION=$(TAG) #-t $(IMAGE):$(TAG)

# Run docker image
run:
	@echo $(IMAGE):$(TAG)
	docker compose up -d

# Restart container
restart:
	@echo $(IMAGE):$(TAG)
	docker compose restart

# Stop container
stop:
	docker compose stop

# Remove container
rm:
	docker compose rm

# Remove container alias
remove:
	docker compose rm

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

