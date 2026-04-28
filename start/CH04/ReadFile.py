#!/usr/bin/env python3
# Sample script that reads from a file
# By 
import os
#open file for writing
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/newtextfile.txt", "r")
#Read the file and print to screen
contents = f.read()
print(contents)
#closing the file
f.close()