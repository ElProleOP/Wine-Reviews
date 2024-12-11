#!/bin/bash

echo "Ready to clean data? Type 1 to continue or 0 to exit"
read answer

if [ $answer == 1 ]
then
    echo "Cleaning data..."
    python script.py
    echo "Exiting..."
else
    echo "Please come back when you are ready"
fi

