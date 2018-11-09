#!/bin/bash

ps -eaf | grep $1 | while read t; do PID=$(awk '{ print $2 }');echo $PID; kill -9 $PID; done

