#!/bin/bash
sudo apt-get update -y
sudo apt-get install docker.io -y
sudo usermod -aG docker vagrant
sudo docker --version
sudo systemctl enable docker
sudo systemctl start docker
sudo apt-get install docker-compose -y
sudo docker-compose --version
sudo apt-get install curl -y
sudo apt-get install build-essential -y
echo "success - Provisioning completed"