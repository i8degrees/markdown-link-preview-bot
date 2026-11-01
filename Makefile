
VERSION=$(shell cat .version || echo "1.0.0")

all: build

# Build docker image
build:
	@echo STUB $(VERSION)

# Run docker image
run:
	@echo STUB

