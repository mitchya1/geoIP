#!/usr/bin/python3
from geoip import geolite2 as gl2
import datetime as dt
import mysql.connector
TODAY = dt.datetime.today().strftime("%m-%d")
ip = open("/opt/geoIP/errors-"+TODAY+".log", "r")
addr = ip.readlines()
geodb = mysql.connector.connect (
  host = "localhost",
  user = "<user>",
  password = "<password>",
  database = "<database name>"
)
dbcursor = geodb.cursor()

#delete yesterday's logs
sql = "delete from log where id;"
dbcursor.execute(sql)
geodb.commit()

for line in addr:
  line = line.rstrip('\n')
  match = gl2.lookup(line)
  if match is not None:
    origin = match.country
    sql = "insert into log (country, ip) values (%s, %s)"
    val = (origin, line)
    dbcursor.execute(sql, val)
    geodb.commit()
  else:
    print("")
    break
ip.close()
