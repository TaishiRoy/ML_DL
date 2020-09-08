import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

#====================================================
# m , k , d , theta values set as test --------------

m = 11.0
k = 200
d = 0.5

theta_s = 0.0
theta_i = [-50, -30, 25, 50]
#----------------------------------------------------

D = len(theta_i)
T = 1e-3
t = [(x + 1)*(T / k) for x in range(k)]
it = [(x + 1) for x in range(k)]
s = [math.cos(2 * math.pi *(x/T)) for x in t]       # original signal
theta_s = theta_s * (math.pi/180)

I = np.random.randn(D,k)                            #  interference
theta_i = [math.radians(x) for x in theta_i]

vS = [cmath.exp(1j * 2 * math.pi * d * x * math.sin(theta_s)) for x in range(m)]
vS_arr = np.reshape(vS,m,1)
vI = []

for K in range(D):
    for i in range(m):
        temp=[cmath.exp(1j*2*math.pi*d*i*math.sin(theta_i[K]))]
        vI.append(temp)
    vI_arr=np.reshape(vI,(m,D))

w = np.zeros((m,1))                  # set up weight matrix 
snr = 10                             # set up signal to noise ratio
x = []


for i in range(D):
    temp=vS_arr+vI_arr[:,i]
    x.append(temp)

x_arr = np.reshape(x,(m,D))
Rx = np.matmul(x_arr,x_arr.T)
#g = np.trace(Rx)


mu = 0.010              # lr
wi = []
esave = []
yy = []
for i in range(len(s)):
    X=np.add((s[i]*vS_arr),np.matmul(vI_arr,I[:,i]))

X=np.reshape(X,(m,1))
y = w.T*X
e = np.conjugate(s[i])-y[0,0]
#e=(s[i])-y[0,0]

esave.append( abs(e)*abs(e) )

w = np.add(w,mu*np.conjugate(e)*X)
wi.append(w)
yy.append(y)
wi_arr = np.reshape(wi, (k,m)).T
w = (1.0 / w[0,0]) * w                    # normalisation
start = -(math.pi/2)
stop = (math.pi/2)
step = 0.01
theta = np.arange(start, stop+step, step)


AF = np.zeros((1,len(theta)))            # array factor of antenna
for i in range(m):
    temp1 = (1j * (i-1) * 2 * math.pi * d * np.sin(theta))
    temp = w[i,0] * np.exp(temp1)
AF=np.add(AF,temp)



# -----------------------------------------------------------
# required for visualisation



fig1=plt.figure()
#plt.plot((-180.0/math.pi)*theta,20*np.log10(np.abs(AF)/np.max(np.abs(AF))).T)
#plt.show()
#fig1.suptitle(#NORMALIZED ARRAY FACTOR PLOT&#39;)
#plt.xlabel(#ANGLE OF ARRIVAL(DEGREE)&#39;)
#plt.ylabel(#&#39;NORMALIZED ARRAY FACTOR(dB)&#39;)
#fig1.savefig(#&#39;test1.png&#39;)
#plt.close()
#fig2 = plt.figure(i


plt.plot(it,esave)
plt.show()


#fig2.suptitle(#&#39;LMS ERROR PLOT WITH THE VARIATION OF ANTENNA ELEMENTS&#39;)
#plt.xlabel(&#39;SAMPLES&#39;)#plt.ylabel(#&#39;MEAN SQUARE ERROR&#39;)
#fig2.savefig(#&#39;test2.png&#39;)
#plt.close()






