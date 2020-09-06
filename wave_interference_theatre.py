#교방공 수업시연 물리교육과 김두찬, 김민환, 서혜린

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

#figure info
fig = plt.figure()
ax1 = fig.gca(projection='3d')

x = np.linspace(0,16,100)
y = np.linspace(0,16,100)

X,Y = np.meshgrid(x,y)


#Wave info
v = 343
f = float(input('어떤 진동수(Hz)의 파동을 보고 싶나요?:'))
ld = v/f
k = 2*np.pi/ld
w = 2*np.pi*f


#source 1, 2: 중앙 양 옆
x11 = 0
y11 = 16/2
x21 = 16
y21 = 16/2

#source 3, 4: 1/3 지점 양 옆
x31 = 0
y31 = 16/3
x41 = 16
y41 = 16/3

#source 5, 6: 2/3 지점 양 옆
x51 = 0
y51 = 16/3*2
x61 = 16
y61 = 16/3*2

#source 7, 8: 앞 1/3, 2/3 지점
x71 = 16/3
y71 = 0
x81 = 16/3*2
y81 = 0


#invert wave info to seat plane
def l(x,y):
    return abs((x-(y-6))/1.414)

ld1 = ((l(x11,y11)+ld)**2-l(x11,y11)**2)**0.5
ld3 = ((l(x31,y31)+ld)**2-l(x31,y31)**2)**0.5
ld5 = ((l(x51,y51)+ld)**2-l(x51,y51)**2)**0.5
ld7 = ((l(x71,y71)+ld)**2-l(x71,y71)**2)**0.5

k1 = 2*np.pi/ld1
k3 = 2*np.pi/ld3
k5 = 2*np.pi/ld5
k7 = 2*np.pi/ld7



def seat(x,y):
    return x/1.414+(y-6)/1.414

#invert pos of speaker to seat plane
x12 = 0
x22 = 16
y12 = seat(x11, y11)
y22 = y12


x32 = x31
x42 = x41
y32 = seat(x31,y31)
y42 = y32

x52 = x51
x62 = x61
y52 = seat(x51,y51)
y62 = y52

x72 = x71
x82 = x81
y72 = seat(x71,y71)
y82 = y72


#Wave
def s1(x,y,t):
    return np.sin(k1*((x-x12)**2+(y-y12)**2)**0.5-w*t)/(((x-x12)**2+(y-y12)**2)**0.5)

def s2(x,y,t):
    return np.sin(k1*((x-x22)**2+(y-y22)**2)**0.5-w*t)/(((x-x22)**2+(y-y22)**2)**0.5)

def s3(x,y,t):
    return np.sin(k3*((x-x32)**2+(y-y32)**2)**0.5-w*t)/(((x-x32)**2+(y-y32)**2)**0.5)

def s4(x,y,t):
    return np.sin(k3*((x-x42)**2+(y-y42)**2)**0.5-w*t)/(((x-x42)**2+(y-y42)**2)**0.5)

def s5(x,y,t):
    return np.sin(k5*((x-x52)**2+(y-y52)**2)**0.5-w*t)/(((x-x52)**2+(y-y52)**2)**0.5)

def s6(x,y,t):
    return np.sin(k5*((x-x62)**2+(y-y62)**2)**0.5-w*t)/(((x-x62)**2+(y-y62)**2)**0.5)

def s7(x,y,t):
    return np.sin(k7*((x-x72)**2+(y-y72)**2)**0.5-w*t)/(((x-x72)**2+(y-y72)**2)**0.5)

def s8(x,y,t):
    return np.sin(k7*((x-x82)**2+(y-y82)**2)**0.5-w*t)/(((x-x82)**2+(y-y82)**2)**0.5)


a = []


##
def main():
    t0 = 0
    dt = 1/2400.
    b = int(input("파원 몇 개가 있는 것을 보고 싶나요? 1개, 2개, 4개, 6개 중에 고르세요:"))
    if b == 1:
        for i in range(240):
            z = s1(X,Y,t0)
            t0 = t0 + dt
            a.append(z)
    elif b == 2:
        d = int(input("파원이 양쪽 중간에 하나씩 있는 경우를 보고 싶으면 0을 입력하고, \n 같은 쪽 1/3과 2/3 지점에 스피커가 2개 있는 경우를 보고 싶으면 1을 입력하세요."))
        if d == 0:
            for i in range(240):
                z = s1(X,Y,t0)+s2(X,Y,t0)
                t0 = t0 + dt
                a.append(z)
        elif d == 1:
            for i in range(240):
                z = s3(X,Y,t0)+s5(X,Y,t0)
                t0 = t0 + dt
                a.append(z)
        else: print("올바른 숫자를 입력하세요.")
    elif b == 4:
        for i in range(240):
            z = s3(X,Y,t0)+s4(X,Y,t0)+s5(X,Y,t0)+s6(X,Y,t0)
            t0 = t0 + dt
            a.append(z)
    elif b == 6:
        for i in range(240):
            z = s3(X,Y,t0)+s4(X,Y,t0)+s5(X,Y,t0)+s6(X,Y,t0)+s7(X,Y,t0)+s8(X,Y,t0)
            t0 = t0 + dt
            a.append(z)
    else: print("올바른 숫자를 입력하세요.")

main()



#Adding the colorbar 
m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
m.set_array(a[0])
cbar = plt.colorbar(m)

p = 0
def animate(i):
    global p
    Z = a[p]
    p += 1
    ax1.clear()
    ax1.plot_surface(X,Y,Z,rstride=1, cstride=1,cmap=plt.cm.jet,linewidth=0,antialiased=False)
    ax1.set_zlim(0,5)


anim = animation.FuncAnimation(fig,animate,frames=220,interval=240)
plt.show()

