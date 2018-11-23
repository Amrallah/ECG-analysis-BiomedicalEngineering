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
            if(k-t)>0:
                xim = x[k]
                n += xim * (x[(k-t)])
        autoc.append(n/d)
    return autoc

f = open ('Data2.txt','r')
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


for value in data_deriv:
    data_sq.append((value*value))


data_sm=moving_average(data_sq)
sm_time=moving_average(time)

lag=[]
for i in range(0,4966):
    lag.append(i)
auto=autoColleration(data_sm)
auto2=auto

"""code to calculate avg heart rate from peaks and lags"""
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
    for i in range(0,4966):
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

