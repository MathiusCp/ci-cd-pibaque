build:
	docker build -t pibaque:1.0.5 .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml pibaque

rm:
	docker stack rm pibaque

ps:
	docker service ls

restart:
	make rm
	sleep 5
	make build
	make deploy