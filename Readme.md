
## Usefull commands
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