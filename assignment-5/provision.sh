#!/bin/bash

echo "Updating the ubuntu system..."
sudo apt-get update -y 

echo "Installing Docker..."
sudo apt-get install -y docker.io

echo "Enable Docker..."
sudo systemctl enable docker
sudo systemctl start docker

echo "Install Docker Compose..."
sudo apt-get install -y docker-compose

echo "provision complete"