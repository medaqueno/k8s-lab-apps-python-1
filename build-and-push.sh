#!/bin/bash

# Build and push script for GitHub Container Registry

# Set your GitHub username and repository name
GITHUB_USERNAME="medaqueno"
REPOSITORY_NAME="k8s-lab-apps-python-1"
IMAGE_NAME="python-api"

# Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Tag the image for GitHub Container Registry
echo "Tagging image for GitHub Container Registry..."
docker tag $IMAGE_NAME ghcr.io/$GITHUB_USERNAME/$REPOSITORY_NAME:$IMAGE_NAME

# Login to GitHub Container Registry (you'll need a personal access token)
echo "Please login to GitHub Container Registry..."
docker login ghcr.io

# Push the image to GitHub Container Registry
echo "Pushing image to GitHub Container Registry..."
docker push ghcr.io/$GITHUB_USERNAME/$REPOSITORY_NAME:$IMAGE_NAME

echo "Image pushed successfully!"
echo "You can now use: ghcr.io/$GITHUB_USERNAME/$REPOSITORY_NAME:$IMAGE_NAME"