## Limit pods per instance 
https://github.com/awslabs/amazon-eks-ami/blob/master/files/eni-max-pods.txt

## Usefull commands
**Update Kubectl**
```bash
aws eks update-kubeconfig --region us-east-1 --name eksctl-test 
```

```bash
kubectl get all #Get all resources in the cluster
kubectl apply -f nginx-deployment-withrolling.yaml #Creates a deployment with the file 
kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080 #Creates a hard deployment
kubectl get pods #Check current state of all pods in the cluster
kubectl get services #Checks current state of all services in the cluster
kubectl delete pod/testdeploy-6c69b6bd77-kjrjw #or
kubectl delete pod/testdeploy-6c69b6bd77-kjrjw #Deletes a specific pod
kubectl get rs #Get the replica set
kubectl delete rs testdeploy-6c69b6bd77 #Deletes a replica set

# After deleting a pod or replicaset K8S should replace it/them automatically

kubectl describe pods #Describes advanced data of pods
kubectl describe deployment #Describes starte of deployment
kubectl get rs --watch #If we add "--watch" argument it will refresh the output on every change

# inside the master node
kubectl get ns #get namespaces 
# NAME              STATUS   AGE
# default           Active   19m
# kube-node-lease   Active   19m
# kube-public       Active   19m
# kube-system       Active   19m
kubectl get pods -n kube-system #get pods of kube-system

```


**Create EKS cluster with eksctl**
```bash
eksctl create cluster --name eksctl-test --nodegroup-name ng-default --node-type t3.micro --nodes 2
```

**Create EKS cluster with yaml file**
```bash
eksctl create cluster --config-file=eksctl-create-cluster.yaml
```

**Update NodeGroup with eksctl and yaml file**
```bash
eks create nodegroup --config-file=eksctl-create-ng.yaml
```

**Delete EKS cluster**
```bash
eksctl delete cluster --name eksctl-test 
```

# Deployment 
## EC2 Manually
**Use Nginx**
Intall nginx
```bash
sudo yum install nginx
```

modify server config in  /etc/nginx/nginx.conf file
```bash
server {
    listen       80;
    listen       [::]:80;
    server_name  _;
    location / {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
    }

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;
}
```

restart nginx server
```bash
sudo service nginx restart
```

**Run using pm2, uvicorn and gunicorn**
install node and npm
```bash
sudo yum install nodejs
```
run with pm2 gunicorn and vunicorn
```bash
pm2 start "gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app" --name hello_world
```

## Docker
Get access to ECR
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

build image
**Linux**
```bash
docker build -t fastapi-docker .
```
**Mac with M1 chip**
```bash
docker buildx build --platform=linux/amd64 -t fastapi-docker .
```
transform to a valid image name
```bash
docker tag fastapi-docker:latest <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/fastapi-docker:latest
```
sent image to ECR
```bash
docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/fastapi-docker:latest
```
Install docker on ec2
```bash
sudo yum install docker
```
Run docker
```bash
sudo service docker start
```
Get access to ECR from instance 
```bash
aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```
Get image from ECR
```bash
sudo docker pull <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/fastapi-docker
```

Run Docker on port 80 without nginx
```bash
sudo docker run -p 80:8000 <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/fastapi-docker:latest
```


**Extra: You can have a load balancer with nginx with many app running at the same time**

```bash
upstream api {
    server localhost:8000;
    server localhost:8001;
    server localhost:8002;
}

server {
    listen       80;
    listen       [::]:80;
    server_name  _;
    location / {
        proxy_pass http://api;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
    }
}
```