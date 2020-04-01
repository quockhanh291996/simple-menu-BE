#!/bin/bash
# Script to load the environment

# Path to the settings file base on the environment
DEV_PATH=ecommerce.settings.development
PROD_PATH=ecommerce.settings.production

if [ $# -eq 0 ]
then
    echo "No arguments provided"
else
	if [ $1 = "dev" ]
	then
		echo 'Exported Development Settings!'
		export DJANGO_SETTINGS_MODULE=$DEV_PATH
	elif [ $1 = "prod" ]
	then
		echo 'Exported Production Settings!'
		export DJANGO_SETTINGS_MODULE=$PROD_PATH
	else
		echo 'Wrong input! Input should be:'
		echo ' - dev'
		echo ' - prod'
	fi
fi

