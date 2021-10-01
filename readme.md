# Raymond Perry pcf-dev-track
Taking into consideration the various modules and courses we have taken in this programme
I came up with this piece of work that touches on most of the concepts we've learned over the last few weeks.
This piece of work deploys a web application into an kubernetes cluster in aws leveraging technologies
such as Terraform, Docker, Kubernetes, Aws (Security Groups, IAM, VPC, EC2, AutoScaling, EKS).

Hope you guys enjoy this, the application itself is just a python flask application
that calculates blood pressure, the deployment is where the focus is.
Let me know if there is anything here that may not work for you.

## Steps Taken:
1. Build a Docker image from a Dockerfile and push it to Docker Hub for further use.
2. Pull a Docker container to act as a management console to create the underlying infrastructure and deploy the application, using Aws CLI and Terraform.
3. Create VPC, Security Groups, EKS Cluster, etc, and deploy a web application using terraform from the created management host.

## Pull git repository
```
git@github.com:rayperry9/dev-track.git
```

## SKIP: Build & Push Docker Image
**This step has already been completed and pushed to the docker hub, you may skip this and proceed as the terraform scrips will pull it from docker hub
If you wish to replicate this, you can run these commands in the same directory as the Dockerfile but sub out my user name "x00113281" for your own
and then make sure to go to the main.tf and replace the image name with your own one. But if you want to skip this part you can and the terraform script
will just pull my created image from docker hub.
```
# Building docker image locally
docker build --tag=x00113281/bpcalculator:latest .

# Pushing docker image to Docker Hub
docker push x00113281/bpcalculator
```


## Creating Management Console
```
# In a local terminal, change directory to the cloned git repository for the next step here to work
# Run Amazon CLI from a pulled Docker container copying the current working directory into the container
docker run -it --rm -v ${PWD}:/work -w /work --entrypoint /bin/sh amazon/aws-cli:2.0.43

# Ensure your pwd is in the container
sh-4.2# ls -ltr
total 4
drwxr-xr-x 7 root root  224 Oct  1 13:26 Application
drwxr-xr-x 5 root root  160 Oct  1 13:27 terraform
-rw-r--r-- 1 root root 3168 Oct  1 13:31 readme.md

cd

# Install Dependencies
yum install -y jq gzip nano tar git unzip wget

```

## Login to Amazon

Being based in Dublin, Ireland, I ran this in eu-west-1, you may need to chose a new region.

```
# UI step was carried out here prior to pull down access keys to login to Aws account
# If you can't remember how to do this, go back and look up creating security access keys in your aws console.

aws configure

AWS Access Key ID [None]: ************
AWS Secret Access Key [None]: ************
Default region name [None]: eu-west-1
Default output format [None]: json
```

## Install Terraform CLI to management console

```
curl -o /tmp/terraform.zip -LO https://releases.hashicorp.com/terraform/0.13.1/terraform_0.13.1_linux_amd64.zip
unzip /tmp/terraform.zip
chmod +x terraform && mv terraform /usr/local/bin/
terraform
```

## Create Infrastructure - EKS, VPC, Security Groups, AutoScaling Group, EC2's

```
cd /work/terraform

terraform init

terraform plan
terraform apply

-----------------------
-----------------------
Plan: 48 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

# Enter yes as done here above, this step can take approx 12-15 to deploy everything

```

## Link Kubernetes config to interact with the created cluster

```
# grab EKS config
aws eks update-kubeconfig --name rperry-dev-track-eks --region eu-west-1

# Get kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl

kubectl get nodes
kubectl get deploy
kubectl get pods
kubectl get svc
```

## Render application
```
kubectl get svc

# Copy LoadBalancer URL and paste into a chosen browser

# Example ..
sh-4.2# kubectl get svc
NAME               TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)        AGE
kubernetes         ClusterIP      172.20.0.1      <none>                                                                    443/TCP        27m
rperry-dev-track   LoadBalancer   172.20.106.59   a7f33e88fc8d749e9abbd320bb6a33f8-1507540711.eu-west-1.elb.amazonaws.com   80:30308/TCP   22m

# Open that External-IP Link in a browser to renber the application
https://eu-west-1.console.aws.amazon.com/eks/home?region=eu-west-1#/clusters
```

## Clean up
```
terraform destroy
```
