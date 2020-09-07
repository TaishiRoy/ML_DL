'''=======================================================================================
K, d, theta val -> set as test    
< Needs import modification from 2.7 to 3.0 >
=========================================================================================='''

import numpy as np
import random
import matplotlib.pyplot as plt


Pi2=1.57
pi = 3.14
M = 20
K=2000
d= 0.2
thetaS = 0.349

#-------------------------------------------------------------------------------------

thetaI = [ (-50*pi)/180, (-20*pi)/180 , (-15*pi/180) , (40*pi)/180 , (60*pi)/180]    # test value
snr = 10   # signal to noise ratio
D = len(thetaI)
T = 0.001
t_ = range(K)
t = []


for i in range(len(t_)):
    t.append(t_[i] * (T/K))

it = range(1,2001)            # set as K+1



temp = np.array(t)
S = np.cos(2*pi * (temp/T)) 
S = list(S)  

#thetaS=thetaS*3.14/180


I=np.random.rand(D,K)

#thetaI=list(np.array(thetaI)*3.14/180)   

vS,vI=[],[]

for a in range(1,21):
     vS.append( np.exp(1j*(a-1)*2*3.14*d*np.sin(thetaS)))
#print vS  


for k in range(D):
    temp=[]
    for i in range(1,21):
        temp.append(np.exp(1j * (i-1)*2*3.14*d*np.sin(thetaI[k])))
    vI.append(temp)    
vI=np.transpose(np.array(vI))
#print vI


w=np.zeros(M)  
#print w  
  
X=[]
for m in range(D):
    X1=vS+vI[:,m]
    #print X1
    X.append(X1)



#X=np.array(X)
#XT=np.transpose(X)    
#RX=np.multiply(X,XT)


mu = 0.0007         # learning rate 
wi = np.zeros([20,2000])        # weight matrix

#wi=np.zeros([M,max(it)])
#print wi


x = []
y = []
yy = []
esave = []
S = np.array(S)
vS = np.array(vS)


for n in range(len(S)-1):               # updation loop
    x = vS*S[n] + np.dot(vI, I[:,n] )
    y = np.dot(np.transpose(w), x)
    e = S[n] - y
    esave.append(np.abs(e)**2)
    w = np.array(w) + np.array(mu * np.conjugate(e) * x)
    #print w.shape
    #print w
    wi[:,n] = w
    yy.append(y)


yy = np.array(yy)  
wi = np.array(wi)
print wi 


for i in range(len(w)):         # normalisation 
   w[i]= w[i]/w[0]


theta = np.linspace(-Pi2, Pi2, 31400.0)     # visualisation aid

AF = np.zeros(len(theta))
for i in range(M):
    AF.append(AF + np.conjugate(w[i]) * np.exp(1j *(i-1)) *2 *pi *d *np.sin(theta))


theta = theta*180/3.14
AF = -20*np.log(np.abs(AF)/max(abs(AF)))        # array factor
AF = -np.abs(AF)
plt.plot(theta,AF)          # visualisation
plt.show()   

#---------------------------------------------------------------------------------------
#plt.polar(theta,AF)
#plt.show()    
      
