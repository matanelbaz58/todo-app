# System Setup & Execution Guide

## Prerequisites
- A running Kubernetes cluster (K3s or Minikube)
- Docker installed and logged in to Docker Hub
- `kubectl` and `argocd` CLI installed

## 1) Configure GitHub Secrets
In the app repo, go to: **Settings → Secrets and variables → Actions**  
Add:
- `DOCKER_USERNAME` — your Docker Hub username
- `DOCKER_PASSWORD` — your Docker Hub password or access token
- `REPO_TOKEN` — GitHub PAT with access to the manifests repo

## 2) Install ArgoCD
Run:
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## 3) Connect ArgoCD to the Manifest Repo
Create the GitOps app with auto-sync:
```bash
argocd app create todo-app \
  --repo https://github.com/<YOUR_GITHUB_USER>/todo-manifests.git \
  --path . \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default \
  --sync-policy automated
```

## 4) End-to-End Flow
1. Create a branch and make a small app change.
2. Open a PR and confirm CI (Pytest) passes.
3. Merge into `main`.
4. Monitor CD in GitHub Actions until manifest update completes.
5. In ArgoCD UI, verify new pods replace old pods.