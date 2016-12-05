#!/usr/bin/env python
import sys
import math

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
room_name = sys.argv[1]
x_offset = float(sys.argv[2])
y_offset = float(sys.argv[3])
th = float(sys.argv[4])
filedir = './LE_' + room_name + '/bed.le'

file_nd = open(filedir, 'w')
file.write(file_nd, str(th)+'\n');

for x0 in range(-10,11):
    for y0 in range(-6,7):
        x = round(math.cos(th) * x0) / 10 - round(math.sin(th) * y0) / 10 + x_offset
        y = round(math.sin(th) * x0) / 10 + round(math.cos(th) * y0) / 10 + y_offset
        print(x,y)
        file.write(file_nd, str(x) + " " + str(y) + "\n")
file.close(file_nd)
        
