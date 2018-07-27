#!/usr/bin/python3
from geoip import geolite2 as gl2
import datetime as dt
import mysql.connector
geodb = mysql.connector.connect (
  host = "localhost",
  user = "<user>",
  password = "<pw>",
  database = "<db>"
)
dbcursor = geodb.cursor()
#clear old
sql = "delete from log where id;"
dbcursor.execute(sql)
geodb.commit()

with open ('/opt/geoIP/errors.log') as ip:
  for line in ip:
    lines = line.rstrip('\n')
    match = gl2.lookup(lines)
    if match is not None:
      origin = match.country
      sql = "insert into log (country, ip) values (%s, %s)"
      val = (origin, line)
      dbcursor.execute(sql, val)
      geodb.commit()
      #good to have for troubleshooting
      #print(origin, "", lines)
    else:
      ip.close()
      break
ip.close()
