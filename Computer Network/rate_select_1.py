# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 14:53:34 2016

@author: Jialiang Yu
"""
import math
import time
import csv
from matplotlib import pyplot as plt


buff = [8]
total = sum(buff)
record = [2]

Buf_now = sum(buff) #The current buffer occupancy, seconds .total= 180
r = 200      #The size of reservoir , seconds
cu = 100    #The size of cushion, seconds
Rate_prev = 20 # The previously used video rate, Mb/s
R_max = 20   #Maximum video rate, Mbps
R_min = 0.5 #Minimum video rate, Mbps
tt = 1
time_list = []

R_i = [0.5,2,8,20]   # Mb/s
chunk_size = [2, 8, 32, 80]      # Mb
arr1 = [] # empty list
arr2 = []
buff_occu = []
total_time = []
bit_rate = []
bandwidth = []
r_bandwidth = []
real_bandwidth = list(csv.reader(open("E:\\Purdue Courses\\Second semester\\ECE595 Computer Network System\\Main Project\\test.csv","rb"),delimiter=','))
for i in range(len(real_bandwidth[0])):
    r_bandwidth.append(real_bandwidth[0][i])

def ind(x):
    if x == 0.5:
        return 0
    elif x == 2:
        return 1
    elif x == 8:
        return 2
    elif x == 20:
        return 3

def func(Buf_now):
    result = 35.74 * math.exp(-((Buf_now-170)/65) ** 2)
    return result
    
    
"""    
def RateSelect(Rate_prev, Buf_now, r, cu, arr1, arr2):
    if Rate_prev == R_max :
        Rate_plus = R_max
    else:
        for i in range(len(R_i)):
            if R_i[i] > Rate_prev:
                arr1.append(R_i[i])
        Rate_plus = min(arr1)
        arr1 = []
    if Rate_prev == R_min:
        Rate_minus = R_min
    else:
        for i in range(len(R_i)):
            if R_i[i] < Rate_prev:
                arr1.append(R_i[i])
        Rate_minus = max(arr1)
        arr1 = []
    if Buf_now <= r:
        Rate_next = R_min
    elif (Buf_now >= (r + cu)):
        Rate_next = R_max
    elif (func(Buf_now) >= Rate_plus):
        for i in range(len(R_i)):
            if R_i[i] < func(Buf_now):
                arr2.append(R_i[i])
        Rate_next = max(arr2)
        arr2 = []
    elif (func(Buf_now) <= Rate_minus):
        for i in range(len(R_i)):
            if R_i[i] > func(Buf_now):
                arr2.append(R_i[i])
        Rate_next = min(arr2)
        arr2 = []
    else:
        Rate_next = Rate_prev
    return Rate_next
"""

def RateSelect(Rate_prev, Buf_now):

    if Rate_prev == 0.5 and Buf_now >= 50 and Buf_now < 100:
        Rate_next = 2
    elif Rate_prev == 2 and Buf_now >= 100 and Buf_now < 300:
        Rate_next = 8
    elif Rate_prev == 8 and Buf_now > 300:
        Rate_next = 20
    elif Rate_prev == 20 and Buf_now <200:
        Rate_next = 0.5
    else:
        Rate_next = 0.5
    return Rate_next

#while(sum(buff) < 800):
for i in range(len(r_bandwidth)):
    #total += chunk_size[ind(Rate_prev)]

    Buf_now = sum(buff) 
     
    BW = r_bandwidth[i]
    Rate_next =  RateSelect(Rate_prev, Buf_now) 
  
    #BW = random.randint(1,20)
    #BW = 2    
    
    nextchunk = chunk_size[ind(Rate_next)]
    trans_time = float(nextchunk) / (float(BW) / 1000)
    while(trans_time >= 0):
        if buff == []:
            
            trans_time -= 1
            tt += 1
            time_list.append(tt)
            bit_rate.append(Rate_next)
            bandwidth.append(float(BW)/1000)
            buff.append(0)
            Buf_now = sum(buff)
            buff.remove(buff[0])
            
            print (Rate_next, buff, Buf_now)
            time.sleep(1)
            
        else:           
            buff[0] -= record[0]
            Buf_now = sum(buff)
            print (Rate_next, buff, Buf_now)
            
            if buff[0] == 0:
                buff.remove(buff[0])
                record.remove(record[0]) 
            trans_time -= 1
            tt += 1
            time_list.append(tt)
            bit_rate.append(Rate_next)
            bandwidth.append(float(BW)/1000)
            
            
            time.sleep(1)
    
    #buff_occu.append(Buf_now)
    Rate_prev = Rate_next
    buff.append(nextchunk)
    record.append(R_i[ind(Rate_prev)])

#print buff_occu   

fig, ax1 = plt.subplots()
ax1.set_ylim([0,25])
ax1.plot(time_list, bit_rate, 'b-')
ax1.set_xlabel('time(s)')
ax1.set_ylabel('bit_rate_selection', color = 'b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax2 = ax1.twinx()
ax2.set_ylim([0,25])
ax2.plot(time_list, bandwidth, 'r-')
ax2.set_ylabel('bandwidth', color = 'r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.show()



#print len(record), len(time_list)   

    
    
    
    
    
    
    
    
    
    
    
    
