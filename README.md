```
docker build -t widgets-api-quantity .

etc..


ubuntu@ip-172-31-52-46:~/src/widgets-api/quantity$ docker images
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
widgets-api-warehouse           latest    4606f1198651   2 weeks ago     187MB
widgets-api-quantity            latest    43150bba90a3   2 weeks ago     187MB
widgets-api-widgets             latest    4cefd4983d28   2 weeks ago     187MB


ubuntu@ip-172-31-52-46:~/src/widgets-api/quantity$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS             PORTS                                   NAMES
09e77e37e48e   4606f1198651   "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3002->80/tcp, :::3002->80/tcp   zen_haibt
c94356fb0bb3   4cefd4983d28   "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3001->80/tcp, :::3001->80/tcp   adoring_almeida
48cdadf0d144   43150bba90a3   "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:3000->80/tcp, :::3000->80/tcp   intelligent_hawking



ubuntu@ip-172-31-52-46:~/src/widgets-api$ python3 client.py
{
  "id": 2,
  "name": "2"
}
{
  "id": 1,
  "name": "nuts"
}
{
  "id": 3,
  "name": "Plano"
}
```
