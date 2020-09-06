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


print(X)
print(Y)

#Wave info
v = 343
f = float(input('어떤 진동수(Hz)의 파동을 보고 싶나요?:'))
ld = v/f
k = 2*np.pi/ld
w = 2*np.pi*f



#source 1, 2: 중앙 양 옆
x1 = 0
y1 = 16/2
x2 = 16
y2 = 16/2

#source 3, 4: 1/3 지점 양 옆
x3 = 0
y3 = 16/3
x4 = 16
y4 = 16/3

#source 5, 6: 2/3 지점 양 옆
x5 = 0
y5 = 16/3*2
x6 = 16
y6 = 16/3*2

#source 7, 8: 앞 1/3, 2/3 지점
x7 = 16/3
y7 = 0
x8 = 16/3*2
y8 = 0


#Wave
def s1(x,y,t):
    return np.sin(k*((x-x1)**2+(y-y1)**2)**0.5-w*t)/(((x-x1)**2+(y-y1)**2)**0.5)

def s2(x,y,t):
    return np.sin(k*((x-x2)**2+(y-y2)**2)**0.5-w*t)/(((x-x2)**2+(y-y2)**2)**0.5)

def s3(x,y,t):
    return np.sin(k*((x-x3)**2+(y-y3)**2)**0.5-w*t)/(((x-x3)**2+(y-y3)**2)**0.5)

def s4(x,y,t):
    return np.sin(k*((x-x4)**2+(y-y4)**2)**0.5-w*t)/(((x-x4)**2+(y-y4)**2)**0.5)

def s5(x,y,t):
    return np.sin(k*((x-x5)**2+(y-y5)**2)**0.5-w*t)/(((x-x5)**2+(y-y5)**2)**0.5)

def s6(x,y,t):
    return np.sin(k*((x-x6)**2+(y-y6)**2)**0.5-w*t)/(((x-x6)**2+(y-y6)**2)**0.5)

def s7(x,y,t):
    return np.sin(k*((x-x7)**2+(y-y7)**2)**0.5-w*t)/(((x-x7)**2+(y-y7)**2)**0.5)

def s8(x,y,t):
    return np.sin(k*((x-x8)**2+(y-y8)**2)**0.5-w*t)/(((x-x8)**2+(y-y8)**2)**0.5)


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

