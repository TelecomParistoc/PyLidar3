import threading
import PyLidar3
import math    
import time
import numpy

#TODO: type hints
#TODO: comments

#TODO: adjust threshold
DISTANCE_DETECTION_THRESHOLD = 1000
NB_SWEEPS = 10
NB_AREA = 6
OFFSET = 0

class LidarStub():
    def __init__(self, port, chunk_size=6000):
        self.port = port
        self.chunck_size = 6000

    def Connect(self):
        #Test connection errors
        return True
    
    def GetDeviceInfo(self):
        return {
                "model_number":1,
                "firmware_version":1,
                "hardware_version":1,
                "serial_number":1
            }

    def StartScanning(self):
        def repeat(object):
            while True:
                yield object
        HIGH_TEST_VALUE = 10000
        LOW_TEST_VALUE = 100
        data = ([HIGH_TEST_VALUE] * 60 + [LOW_TEST_VALUE] * 60 + [HIGH_TEST_VALUE] * 60)*2
        return repeat(data)


    def StopScanning(self):
        return True

    def Disconnect(self):
        return True

class LidarThread(threading.Thread):
    def __init__(self, LidarClass, sync, port=None):
        threading.Thread.__init__(self)
        self.Obj = LidarClass
        self.sync = sync
        self.port = port

    def run(self):
        if self.port = None:
            #TODO: automatic port detection
            port =  input("Enter port name which lidar is connected:")
        
        #Allow the use of stub
        Obj = self.obj(port)

        if(Obj.Connect()):
            print(Obj.GetDeviceInfo())
            data_generator = Obj.StartScanning()
            #TODO: stoping method
            while 1:
                for_sweeps, back_sweep = [], []
                for i in range(NB_SWEEPS):
                    data = next(data_generator)
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
                
                #TODO: determine what information to transfer to saving module
                for_mean = np.mean(for_sweeps)
                back_mean = np.mean(back_sweep)


            Obj.StopScanning()
            Obj.Disconnect()
        else:
            #TODO: specific error
            print("Error connecting to device")
