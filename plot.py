#!/usr/bin/python
import matplotlib.pyplot as plt
import csv
import sys
  
x = []
y = []
 
if (len(sys.argv) == 1):
    print('usage: ./plot <name>.csv')
    print('exiting...')
    exit(1)


with open(sys.argv[1],'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(float(row[1]))
  
plt.plot(x, y, color = 'brown', linestyle = 'dashed',
         marker = 'o',label = "EMG sensor output")
  
# plt.xticks(rotation = 25)
plt.xticks([])
plt.xlabel('time (10 s)')
plt.ylabel('sensor output (mV)')
# plt.title('myoware sensor output', fontsize = 20)
plt.title(sys.argv[1], fontsize = 20)
plt.grid()
plt.legend()
plt.show()
