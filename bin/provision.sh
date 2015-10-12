#!/usr/bin/env bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y libssl-dev libffi-dev python-dev python-pip libxml2-dev libxslt1-dev
sudo apt-get install -y postgresql libpq-dev
sudo pip install -r /vagrant/requirements.txt


DB_NAME="flask"
DB_USER="flask"
DB_PASS="flask"

sudo -u postgres bash -c "psql -c \"CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';\""
sudo -u postgres bash -c "psql -c \"ALTER USER $DB_USER CREATEDB;\""
sudo -u postgres bash -c "psql -c \"CREATE DATABASE $DB_NAME ENCODING 'UTF8';\""
sudo -u postgres bash -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE $DB_NAME to $DB_USER;\""