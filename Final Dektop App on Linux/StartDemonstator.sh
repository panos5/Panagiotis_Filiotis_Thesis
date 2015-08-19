#!/bin/bash



echo "Setting up PYTHONPATH..."

pynaoqi_dir="${PWD}/pynaoqi-python-2.6-naoqi-1.14-linux64"  # for Python version 2.6
#pynaoqi_dir="${PWD}/pynaoqi-python-2.7-naoqi-1.14-linux64" # for Python version 2.7

pygame_dir="${PWD}/pygame-1.9.1release"  # for Pygame version 1.9

PYTHONPATH=$PYTHONPATH:$pynaoqi_dir:$pygame_dir

echo "Starting NAO Demonstrator..."
#python Main.py

LD_PRELOAD=/usr/lib64/libX11.so python Main.py

#python2.6 file.py # force version 2.6
#python2.7 file.py # force version 2.7
