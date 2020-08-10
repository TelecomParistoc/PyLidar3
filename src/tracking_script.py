import threading
import PyLidar3
import math    
import time
import numpy

#TODO: adjust threshold
DISTANCE_THRESHOLD = 1000
NB_SWEEPS = 10
NB_AREA = 6
OFFSET = 0
#TODO: threading skelton

#TODO: automatic port detection
port =  input("Enter port name which lidar is connected:")
Obj = PyLidar3.YdLidarX4(port)

#threading.Thread(target=draw).start()
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    #TODO: stoping method
    while 1:
        for_sweeps, back_sweep = [], []
        #TODO: do some post-treatment (means)
        for i in range(NB_SWEEPS):
            data = next(gen)
            data = np.array(data)

            #FORWARD PART
            forward_raw = data[(60+OFFSET)%360 : (120+OFFSET)%360]
            forward_area = np.array_split(forward_raw, NB_AREA)
            forward_mean = np.mean(forward_area, axis=1)
            for_sweeps.append(np.max(forward_mean))
            #BACKWARD PART
            backward_raw = data[(240+OFFSET)%360 : (300+OFFSET)%360]
            backward_area = np.array_split(backward_raw, NB_AREA)
            backward_mean = np.mean(backward_area, axis=1)
            back_sweep.append(np.max(backward_mean))


    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")
    #TODO: specific error
