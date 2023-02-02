```
wolmarans@86P93D3:~$ h ecr
 3745  aws ecr get-login-password --region us-west-2
 3746  aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 645783638046.dkr.ecr.us-west-2.amazonaws.com
 3747  docker tag json_server_example:latest 645783638046.dkr.ecr.us-west-2.amazonaws.com/json_server_example:latest
 3755  docker tag json_server_example:latest 645783638046.dkr.ecr.us-west-2.amazonaws.com/json_server_example:latest
 3756  docker push 645783638046.dkr.ecr.us-west-2.amazonaws.com/json_server_example:latest
 3835  docker push 645783638046.dkr.ecr.us-west-2.amazonaws.com/json_server_example:latest
 4055  history | grep ecr

docker build -t widgets-api-quantity .

etc..


ubuntu@ip-172-31-52-46:~/src/widgets-api/quantity$ docker images
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
widgets-api-warehouse           latest    4606f1198651   2 weeks ago     187MB
widgets-api-quantity            latest    43150bba90a3   2 weeks ago     187MB
widgets-api-widgets             latest    4cefd4983d28   2 weeks ago     187MB

docker run -idp 3000:80 widgets-api-warehouse
docker run -idp 3001:80 widgets-api-blah
docker run -idp 3002:80 widgets-api-blah

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
