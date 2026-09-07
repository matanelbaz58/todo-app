# Todo App - GitOps CI/CD

A Python-based (Flask) Todo application optimized for ARM64 architecture, deployed automatically via a complete GitOps pipeline.

**System Architecture**
* **CI Pipeline:** Automated testing (Pytest) on every Pull Request to prevent faulty code from being merged.
* **CD Pipeline:** Building a Docker Image compiled for Apple Silicon and pushing it to Docker Hub upon merge to `main`.
* **GitOps:** Automated updates of the Image tag in the Manifest Repository directly from the GitHub Action.
* **Deployment:** Continuous deployment to a Kubernetes cluster using ArgoCD (Zero-Downtime).

**Core Technologies**
* Python 3.10, Pytest
* Docker, GitHub Actions
* Kubernetes, ArgoCD   