UID := $(shell id -u $(USER))
GID := $(shell id -g $(USER))

all: bin

bin:
	env UID=$(UID) GID=$(GID) docker compose run --rm dbt7-bin-rocky8;

clean:
	rm build/*.rpm
