#!/usr/bin/env bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y libssl-dev libffi-dev python-dev python-pip libxml2-dev libxslt1-dev
cd /vagrant
sudo pip install -r requirements.txt