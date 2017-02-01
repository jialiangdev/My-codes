# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 14:53:34 2016

@author: Jialiang Yu
"""
import math
import numpy
import time
import csv
from matplotlib import pyplot as plt


buff = [2]
total = sum(buff)
record = [0.5]

Buf_now = sum(buff) #The current buffer occupancy, seconds .total= 180
r = 50      #The size of reservoir , seconds
cu = 100    #The size of cushion, seconds
Rate_prev = 0.5 # The previously used video rate, Mb/s
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

point = 0
diff_list = []
BW_init_1 = 1
BW_init_2 = 1
BW_list = []
prediction = []
pre_count = 0
thirty = 0
fifty = 0
delay = 0
cycle = 4
bit_sum = 0
bandwidth_sum = 0
Rate_next = 0.5

real_bandwidth = list(csv.reader(open("E:\\Purdue Courses\\Second semester\\ECE595 Computer Network System\\Main Project\\test.csv","rb"),delimiter=','))
for i in range(len(real_bandwidth[0])):
    r_bandwidth.append(float(real_bandwidth[0][i])/1000)

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
    
    
 
def RateSelect(Rate_prev, Buf_now, r, cu, arr1, arr2,BW):
    

    if BW > 0 and BW <2:
        Rate_next1 = 0.5
    elif BW >= 2 and BW < 5:
        Rate_next1 = 2
    elif BW >= 5 and BW < 15:
        Rate_next1 = 8
    else: 
        Rate_next1 = 20

    
    
    
    
    
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
        Rate_next2 = R_min
    elif (Buf_now >= (r + cu)):
        Rate_next2 = R_max
    elif (func(Buf_now) >= Rate_plus):
        for i in range(len(R_i)):
            if R_i[i] < func(Buf_now):
                arr2.append(R_i[i])
        Rate_next2 = max(arr2)
        arr2 = []
    elif (func(Buf_now) <= Rate_minus):
        for i in range(len(R_i)):
            if R_i[i] > func(Buf_now):
                arr2.append(R_i[i])
        Rate_next2 = min(arr2)
        arr2 = []
    else:
        Rate_next2 = Rate_prev
        
    return min(Rate_next1,Rate_next2)



"""
def RateSelect(Buf_now, BW):
    
   
    
    if Buf_now > 50:
        if BW > 0 and BW <2:
            Rate_next = 0.5
        elif BW >= 2 and BW < 5:
            Rate_next = 2
        elif BW >= 5 and BW < 15:
            Rate_next = 8
        elif BW >= 15 :
            Rate_next = 20
        else:
            Rate_next = 0.5
    else:
        Rate_next = 0.5
    return Rate_next
"""        





while len(r_bandwidth) > 1 :
#or len(r_bandwidth) > 0:
    
    Buf_now = sum(buff)
    #if len(record) <  45:
            
    
    if len(prediction) < 20:
        prediction.append(Rate_next)
    else:
        if numpy.std(prediction) >= 5:
            Rate_next = 2
            pre_count += 1
        elif numpy.std(prediction) > 2 and numpy.std(prediction) < 5:
            Rate_next = 8
            pre_count += 1
        else:
            pre_count = 0
            prediction = []
            
    if pre_count > 50:
        prediction = []
        pre_count = 0
    


    
    
    #Rate_next = RateSelect()    
    nextchunk = chunk_size[ind(Rate_next)]
    virtualchunk = nextchunk
    while virtualchunk > 0:
        if len(r_bandwidth) > 0:
            virtualchunk -= r_bandwidth[0]
            bandwidth.append(r_bandwidth[0])
            
        else:
            break
        
        if buff == []:
            tt += 1
            time_list.append(tt)
            #bit_rate.append(Rate_next) 
            
            #buff.append(0)
            Buf_now = 0
            Rate_next = 0
            #r_bandwidth.remove(r_bandwidth[0])
            bit_rate.append(Rate_next)                
            print (Rate_next, buff, Buf_now)
            #buff.remove(buff[0])
            time.sleep(1)        
        else:
            buff[0] -= record[0]
            Buf_now = sum(buff)
            Rate_next = RateSelect(Rate_prev, Buf_now, r, cu, arr1, arr2,r_bandwidth[0])
            Rate_prev = Rate_next            
            r_bandwidth.remove(r_bandwidth[0])
            if buff[0] == 0:
                buff.remove(buff[0])
                record.remove(record[0]) 

            tt += 1
            time_list.append(tt)
            #bit_rate.append(Rate_next)
            bit_rate.append(Rate_next)
            print (Rate_next, buff, Buf_now)
            time.sleep(1)

            
            
            
    #Rate_prev = Rate_next    
    buff.append(nextchunk) 
    record.append(R_i[ind(Rate_next)])
        
    
     else:
        while cycle > 0 and len(r_bandwidth) > 0:
            
            buff[0] -= record[0]
            Buf_now = sum(buff)
            Rate_next = RateSelect(Rate_prev, Buf_now, r, cu, arr1, arr2,r_bandwidth[0])
            bandwidth.append(r_bandwidth[0])
            r_bandwidth.remove(r_bandwidth[0])
            
            
            if buff[0] == 0:
                buff.remove(buff[0])
                record.remove(record[0]) 
    
            tt += 1
            time_list.append(tt)

            bit_rate.append(Rate_next)
            print (Rate_next, buff, Buf_now)
            time.sleep(1) 
            cycle -= 1
        cycle = 4
    
print sum(bandwidth)
print sum(bit_rate)

#print buff_occu   

fig, ax1 = plt.subplots()
ax1.set_ylim([0,25])
ax1.plot(time_list, bandwidth, 'r-')
ax1.set_xlabel('time(s)')
ax1.set_ylabel('bandwidth', color = 'r')
for tl in ax1.get_yticklabels():
    tl.set_color('r')

ax2 = ax1.twinx()
ax2.set_ylim([0,25])
ax2.plot(time_list, bit_rate, 'b-')
ax2.set_ylabel('bit_rate_selection', color = 'b')
for tl in ax2.get_yticklabels():
    tl.set_color('b')
plt.show()
























    
    
