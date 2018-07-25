# geoIP

## Overview
I wrote this to play around with Python's geoip library and MySQL. I though it'd be interesting to see which IPs were hitting restricted parts of my site. So why not see where they're from and dump that into MySQL?

## Requirements
* python3
* python-geoip
* python-geoip-geolite2
* mysql-connector
* pip3

### Installing

Clone this repo.

Install python3 (at least) and pip3. 

Run:
`pip3 install python-geoip python-geoip-geolite2 mysql-connector`
to install dependencies.

Create a MySQL database for this script. Something like this will work:

`CREATE DATABASE geoip;`

`CREATE TABLE log (country VARCHAR(255), ip VARCHAR(255), id INT AUTO_INCREMENT PRIMARY KEY);`

`GRANT INSERT on log.* to 'geo'@'localhost' identified by 'password';`

Then edit geoIP.py to include your database information. 

Then, `chmod 0700 geoIP.py; chmod 0700 getErrorIP.sh`

## Running
Create the directory structure for the script. By default, it's `/opt/geoIP/`. So, `mkdir /opt/geoIP`
Run the shell script to generate the error file. By default, the log file is named `errors-%m-%d.log` (i.e. errors-07-25.log). If you change this format, you'll need to change the Python script.

After that, run the Python script. Now you have country and IP location from your Apache error log in a database. Yay!
