# Flask App Deployment with Helm

This repository contains files for deploying a Flask application to Kubernetes using Helm.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Helm](https://helm.sh/docs/intro/install/)

## Getting Started

1. Clone this repository:

```bash
   git clone <repository_url>
   cd <repository_directory>
```

2. Build The Docker image

```
docker build -t zezo001/flask-app .
```

3. Start Minikube:

```
minikube start
```

4. Install the Helm chart:

```
helm install python-chart python-chart-0.1.0.tgz
```

## **Usage**

This will open your default web browser and navigate to your Flask application.

## **Configuration**

Modify the `values.yaml` file to customize the deployment configuration, such as the number of replicas, resource limits, and service type.

## **Cleanup**

To remove the deployed resources, run:
```bash
helm uninstall python-chart
minikube delete
```







