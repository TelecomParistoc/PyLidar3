import threading
import PyLidar3
import matplotlib.pyplot as plt
import math    
import time

def draw():
    global is_plot
    while is_plot:
        plt.figure(1)
        plt.cla()
        plt.ylim(-5000,5000)
        plt.xlim(-5000,5000)
        plt.scatter(x,y,c='r',s=8)
        plt.pause(0.001)
    plt.close("all")


is_plot = True
x=[]
y=[]
for _ in range(360):
    x.append(0)
    y.append(0)

chunk = 3000
ports = ["/dev/ttyUSB0", "/dev/ttyUSB1"]

for port in ports:
    Obj = PyLidar3.YdLidarX4(port, chunk) #PyLidar3.your_version_of_lidar(port,chunk_size) 
    if Obj.Connect():
        break
else:
    print("Error connecting to device")
    exit(1)
threading.Thread(target=draw).start()
print(Obj.GetDeviceInfo())
gen = Obj.StartScanning(0, 180)
t = time.time() # start time 
while time.time() < t + 30 : #scan for 30 seconds
    #print("One loop turn")
    data = next(gen)
    #print(len(data), min(data), max(data))
    for (angle, dist) in data.items():
        if(dist>10):
            x[angle] = dist * math.cos(math.radians(angle))
            y[angle] = dist * math.sin(math.radians(angle))
is_plot = False
Obj.StopScanning()
Obj.Disconnect()


