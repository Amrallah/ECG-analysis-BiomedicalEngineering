import matplotlib.pyplot as plt
import numpy as np
def moving_average(a, n=31) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def autoColleration(x):
    autoc=[]
    leng=int(len(x))
    for t in range(leng):
        n=0
        d=1
        for k in range(len(x)):
            if (k-t)>0:
                xim = x[k]
                n += xim * (x[(k-t)])
        autoc.append(n/d)
    return autoc

f = open ('Data1.txt','r')
f_contents = f.readlines()
data=[]
time=[]
data_deriv=[]
data_sq=[]
timei=0
T=1/512

for item in f_contents:
    item.replace("\n","")
    data.append(float(item))
    time.append(timei)
    timei+=T
f.close()

"""plt1=plt.plot(time[0:2000],data[0:2000])
plt1=plt.title("Raw ECG")
plt.show(plt1)"""

for index in range(len(data)):
    if index == 0 or index ==1 or index == len(data)-1 or index == len(data)-2 :
        continue
    else:
        x = (1 / (8 * T)) * (-data[index - 2] - 2 * data[index - 1] + 2 * data[index + 1] + data[index + 2])
        data_deriv.append(x)

time.pop()
time.pop()
time.pop(0)
time.pop(0)

"""plt2=plt.plot(time[0:2000],data_deriv[0:2000])
plt2=plt.title("ECG Derivative")
plt.show(plt2)"""

for value in data_deriv:
    data_sq.append((value*value))

"""plt3=plt.plot(time[0:2000],data_sq[0:2000])
plt3=plt.title("Derivative Squared")
plt.show(plt3)"""

"""Smoothing implementation manually instead of Moving average function"""

"""sm_time=[]
j=15
for index in range (len(time)):
    if index == j:
        sm_time.append(time[index])
        j+=31
sum=0
data_sm=[]
data_sq2=data_sq
while len(data_sq2) !=0:
    if len(data_sq2) >= 31:
        for index in range(0,30):
            sum+=data_sq[index]
    else:
        for index in range(len(data_sq2)):
            sum += data_sq[index]
    data_sm.append((1/31)*sum)
    sum=0
    del data_sq2[:31]
data_sm.pop()"""

data_sm=moving_average(data_sq)
sm_time=moving_average(time)

"""plt4=plt.plot(sm_time[0:2000],data_sm[0:2000])
plt4=plt.title("Smoothed")
plt.show(plt4)"""

lag=[]
for i in range(0,4136):
    lag.append(i)
auto=autoColleration(data_sm)
auto2=auto

"""Code to compute avg heartbeat from pb2"""
peaks=[]
max=0
for index in range(len(auto2)):
    if auto2[index] >= (6000000):
        if auto2[index]>max:
            max=auto2[index]
        else:
            if max not in peaks:
                peaks.append(max)
    else:
        max=0

peaks.pop(0)

lags=[]
for value in peaks:
    for i in range(0,4136):
        if value == auto[i]:
            lags.append(i)

lags.reverse()
print(lags)

bpm=[]
for index in range(len(lags)-1):
    bpm.append((60/((lags[index]-lags[index+1])/512)))

print(bpm)
avg_bpm=sum(bpm)/len(bpm)
print(avg_bpm)

if avg_bpm>100:
    print("Atrial Fibrillation detected!")


plt5=plt.plot(lag,auto)
plt5=plt.title("Autocorrelation")
plt.show(plt5)

