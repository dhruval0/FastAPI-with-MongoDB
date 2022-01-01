#!/bin/sh

# navigate into our working directory where we have all our github files
/home/ec2-user/firstdeploy

# Install pip
# sudo apt install -y python3-pip

# # Install Node
# curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
# sudo apt install nodejs
sudo npm i pm2 -g

# Install virtualenv
pip install virtualenv
# or sudo apt install python3.8-venv
python3 -m venv ~/env

source env/bin/activate

pip3 install -r requirements.txt

cd FastAPI-with-MongoDB/app/

pm2 start ecosystem.config.js