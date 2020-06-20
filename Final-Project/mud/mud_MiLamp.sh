#! /bin/bash

MUDGEE_PATH="/home/draane/Programs/mudgee/target/mudgee-1.0.0-SNAPSHOT.jar"

CONFIG_FILE="/mnt/raid/Università/IoT/repository/Final-Project/mud/config/MiLamp.json"

java -jar $MUDGEE_PATH $CONFIG_FILE

