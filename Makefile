# Construcción local (para pruebas)
build:
	docker build -t pibaque:1.0.5 .

# Despliegue del stack en el VPS
deploy:
	docker stack deploy --with-registry-auth -c stack.yml pibaque

# Eliminar el stack
rm:
	docker stack rm pibaque

# Ver estado de los servicios
ps:
	docker service ls

# Reiniciar stack local o en VPS
restart:
	make rm
	sleep 5
	make build
	make deploy
