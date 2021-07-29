import RPi.GPIO as IoPort
import time

IoPort.setmode(IoPort.BCM)

class doorlock:
    def __init__(self):
        self.input_arr=[0,0,0,0,0]
        self.initial_arr=[0,0,0,0,0]
        self.arr=[1000,100,10,1]
        self.i=0
        
        self.buzzer=16
        IoPort.setup(self.buzzer, IoPort.OUT)
    def NumberLock(self, data):
        self.input_arr[self.i]=data
        print(self.input_arr)
        self.i=self.i+1
        
        if(self.i==5):
            if(self.input_arr==self.initial_arr):
                print("The door is open")
                for a in range(0,3):
                    IoPort.output(self.buzzer,True)
                    time.sleep(0.564)
                    IoPort.output(self.buzzer,False)
                    time.sleep(0.564)
                time.sleep(0.5)
                for a in range(0,3):
                    IoPort.output(self.buzzer,True)
                    time.sleep(0.00664)
                    IoPort.output(self.buzzer,False)
                    time.sleep(0.00664)
                time.sleep(0.5)
                for a in range(0,3):
                    IoPort.output(self.buzzer,True)
                    time.sleep(0.00085)
                    IoPort.output(self.buzzer,False)
                    time.sleep(0.00085)
                time.sleep(0.5)
            else:
                print("Passwords do not match")
                for a in range(0,3):
                    IoPort.output(self.buzzer,True)
                    time.sleep(0.00764)
                    IoPort.output(self.buzzer,False)
                    time.sleep(0.00764)
                time.sleep(0.5)
                for a in range(0,3):
                    IoPort.output(self.buzzer,True)
                    time.sleep(0.00764)
                    IoPort.output(self.buzzer,False)
                    time.sleep(0.00764)
                time.sleep(0.5)
                for a in range(0,3):
                    IoPort.output(self.buzzer,True)
                    time.sleep(0.00764)
                    IoPort.output(self.buzzer,False)
                    time.sleep(0.00764)
                time.sleep(0.5)

            self.i=0
            for j in range(0,5):
                self.input_arr[j]=0
            print("DoorLock arr ReSet")
    
    def NumberProcessing(self, number):
        k=0
        while(k<4):
            self.initial_arr[k]=int(number/self.arr[k])
            number=number%self.arr[k]
            k=k+1
            if(k==4):
                self.initial_arr[k]='Q'
                
        print(self.initial_arr)
        
    def BuzzerNumber(self):
        for a in range(0,5):
            IoPort.output(self.buzzer,True)
            time.sleep(0.00764)
            IoPort.output(self.buzzer,False)
            time.sleep(0.00764)
            
    def BuzzerOpen(self):
        for a in range(0,3):
            IoPort.output(self.buzzer,True)
            time.sleep(0.564)
            IoPort.output(self.buzzer,False)
            time.sleep(0.564)
        time.sleep(0.5)
        for a in range(0,3):
            IoPort.output(self.buzzer,True)
            time.sleep(0.00664)
            IoPort.output(self.buzzer,False)
            time.sleep(0.00664)
        time.sleep(0.5)
        for a in range(0,3):
            IoPort.output(self.buzzer,True)
            time.sleep(0.00085)
            IoPort.output(self.buzzer,False)
            time.sleep(0.00085)
        time.sleep(0.5)
        
    def BuzzerClose(self):
        for a in range(0,3):
            IoPort.output(self.buzzer,True)
            time.sleep(0.00764)
            IoPort.output(self.buzzer,False)
            time.sleep(0.00764)
        time.sleep(0.5)
        for a in range(0,3):
            IoPort.output(self.buzzer,True)
            time.sleep(0.00764)
            IoPort.output(self.buzzer,False)
            time.sleep(0.00764)
        time.sleep(0.5)
        for a in range(0,3):
            IoPort.output(self.buzzer,True)
            time.sleep(0.00764)
            IoPort.output(self.buzzer,False)
            time.sleep(0.00764)
        time.sleep(0.5)       
    


        
        