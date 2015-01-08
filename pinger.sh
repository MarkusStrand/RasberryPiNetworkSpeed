#!/bin/bash 

target=www.sonera.fi

while [ 1 ]
do
	date +"%Y-%m-%dT%T" 
	/bin/ping $target  -c 2 -s 1 -W 1 &> /dev/null
	if  [ $? -eq 0 ]; then
		echo "Ping worked"
		sleep 60
	else
		echo "Ping failed"
		date +"%Y-%m-%dT%T" >> pingfailed.log
		sleep 10
	fi
done
