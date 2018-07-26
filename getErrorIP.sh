#!/bin/bash
cat /var/log/apache2/error.log | grep "authz" | cut -f 11 -d ' ' | cut -f 1 -d ':' | uniq > /opt/geoIP/errors.log
