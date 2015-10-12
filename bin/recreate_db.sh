#!/usr/bin/env bash
DB_NAME="flask"
DB_USER="flask"
DB_PASS="flask"

sudo -u postgres bash -c "psql -c \"DROP DATABASE $DB_NAME;\""
sudo -u postgres bash -c "psql -c \"CREATE DATABASE $DB_NAME ENCODING 'UTF8';\""
sudo -u postgres bash -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE $DB_NAME to $DB_USER;\""