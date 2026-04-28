#!/usr/bin/env python3
# example workign with conditionals
#By Daniel Zhumabekov on 4/26/26

#Ask user if they are having a good day
if input("Is today a good day? (y/n)?") =="y":
    print("Yeah It is!")
answer = input("Is it correct? (y/n):")
if answer == "y":
    for i in range(10):
        print("Yeah it is")