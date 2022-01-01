#!/bin/sh

# Install pip
sudo yum install -y python3-pip

# Install Node
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo yum install nodejs
sudo npm i pm2 -g

# Install virtualenv
pip install virtualenv
# or sudo yum install python3.8-venv
python3 -m venv ~/env