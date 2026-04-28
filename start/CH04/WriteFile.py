#!/usr/bin/env python3
# Sample script that writes to a file
# By Daniel on 4/28
import os
#open file for writing
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/newtextfile.txt", "w")

#write to the file
print ("Hello world")
f.write("Hello World\n")
f.write("Have a good day, wonderful seeing you\n")

#closing the file
f.close()