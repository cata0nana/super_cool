#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT

dbus-uuidgen > /var/lib/dbus/machine-id

while true
do
	echo "NEW ..............."
	timeout 4m python3 v0rtex_go.py
done
