#!/bin/bash
echo "Provisioning the system..."
sudo apt-get install docker.io -y
sudo usermod -aG docker vagrant
sudo docker --version
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker
sudo apt-get install docker-compose -y
sudo docker-compose --version