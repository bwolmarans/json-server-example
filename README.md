```
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ minikube start
😄  minikube v1.28.0 on Ubuntu 22.04
🎉  minikube 1.29.0 is available! Download it: https://github.com/kubernetes/minikube/releases/tag/v1.29.0
💡  To disable this notice, run: 'minikube config set WantUpdateNotification false'

✨  Automatically selected the docker driver. Other choices: ssh, none
📌  Using Docker driver with root privileges
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.25.3 on Docker 20.10.20 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: default-storageclass, storage-provisioner
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ k apply -f
ingress.yaml                 ingress2.yaml                widgets-app-deployment.yaml
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ k apply -f widgets-app-deployment.yaml
deployment.apps/widgets-debugger created
deployment.apps/widgets-frontend created
service/widgets-frontend created
deployment.apps/widgets-widget created
service/widgets-widget created
deployment.apps/widgets-quantity created
service/widgets-quantity created
deployment.apps/widgets-warehouse created
service/widgets-warehouse created
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ k get svc -A
NAMESPACE     NAME                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                  AGE
default       kubernetes          ClusterIP   10.96.0.1       <none>        443/TCP                  20s
default       widgets-frontend    ClusterIP   10.111.76.24    <none>        80/TCP                   4s
default       widgets-quantity    ClusterIP   10.103.232.76   <none>        3001/TCP                 4s
default       widgets-warehouse   ClusterIP   10.111.6.203    <none>        3002/TCP                 4s
default       widgets-widget      ClusterIP   10.100.1.96     <none>        3000/TCP                 4s
kube-system   kube-dns            ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP,9153/TCP   18s
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ k get deployment -A
NAMESPACE     NAME                READY   UP-TO-DATE   AVAILABLE   AGE
default       widgets-debugger    0/1     1            0           22s
default       widgets-frontend    0/1     1            0           22s
default       widgets-quantity    0/1     1            0           22s
default       widgets-warehouse   0/1     1            0           22s
default       widgets-widget      0/1     1            0           22s
kube-system   coredns             1/1     1            1           36s
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ k expose deployment widgets-frontend --type=NodePort --port=80
Error from server (AlreadyExists): services "widgets-frontend" already exists
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ k delete svc widgets-frontend
service "widgets-frontend" deleted
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ k expose deployment widgets-frontend --type=NodePort --port=80
service/widgets-frontend exposed
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ k get svc
NAME                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes          ClusterIP   10.96.0.1       <none>        443/TCP        83s
widgets-frontend    NodePort    10.99.36.197    <none>        80:32425/TCP   5s
widgets-quantity    ClusterIP   10.103.232.76   <none>        3001/TCP       67s
widgets-warehouse   ClusterIP   10.111.6.203    <none>        3002/TCP       67s
widgets-widget      ClusterIP   10.100.1.96     <none>        3000/TCP       67s
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ minikube service widgets-frontend --url
http://192.168.49.2:32425
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ curl http://192.168.49.2:32425
Thank you for checking the Widgets inventory. Happy Selling!
{
  "id": 4,
  "name": "hinges"
}
{
  "id": 4,
  "name": "4"
}
 {
  "id": 3,
  "name": "Plano"
}
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$ curl http://192.168.49.2:32425
Thank you for checking the Widgets inventory. Happy Selling!
{
  "id": 2,
  "name": "bolts"
}
{
  "id": 3,
  "name": "3"
}
 {
  "id": 2,
  "name": "Secaucus"
}
ubuntu@ip-172-31-52-46:~/widgets-app/k8s-manifests$


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
