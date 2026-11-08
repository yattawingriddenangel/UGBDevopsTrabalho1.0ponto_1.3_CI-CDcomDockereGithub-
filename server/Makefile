SHELL := /bin/bash

VERSION ?= latest

include .env
export

.PHONY: deploy login pull up down status logs

deploy: login pull up
	@echo ""
	@echo "Deploy concluido!"
	@echo "Imagem: $(IMAGE_NAME):$(VERSION)"

login:
	@echo "Autenticando no GHCR..."
	@echo "$(GHCR_TOKEN)" | docker login ghcr.io -u "$(GHCR_USER)" --password-stdin

pull:
	@echo "Baixando $(IMAGE_NAME):$(VERSION)..."
	@VERSION="$(VERSION)" docker compose pull

up:
	@echo "Subindo a versao $(VERSION)..."
	@VERSION="$(VERSION)" docker compose up -d

down:
	@docker compose down

status:
	@docker compose ps

logs:
	@docker compose logs -f
