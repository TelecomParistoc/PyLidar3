import threading
import PyLidar3
import math    
import time

#TODO: automatic port detection
port =  input("Enter port name which lidar is connected:")
Obj = PyLidar3.YdLidarX4(port)

#threading.Thread(target=draw).start()
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    #TODO: stoping method
    t = time.time() # start time 
    while (time.time() - t) < 30: #scan for 30 seconds
        #TODO: do some post-treatment (means)
        data = next(gen)
        #FORWARD PART
        #TODO: some sort of offset to compensate the lidar angle offset
        for angle in range(60, 120):
            if(data[angle]>1000):
                #TODO: use something to transmit
                pass
        #BACKWARD PART
        for angle in range(240, 300):
            if(data[angle]>1000):
                """x[angle] = data[angle] * math.cos(math.radians(angle))
                y[angle] = data[angle] * math.sin(math.radians(angle))"""
                #TODO: use something to transmit
                pass
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")
    #TODO: specific error
