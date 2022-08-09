from turtle import speed
import msgParser
import carState
import carControl
import model
import keyboard
import pandas as pd
import numpy as np

class Driver(object):
    def __init__(self, stage):
        '''Constructor'''
        self.WARM_UP = 0
        self.QUALIFYING = 1
        self.RACE = 2
        self.UNKNOWN = 3
        self.stage = stage
        
        self.parser = msgParser.MsgParser()
        
        self.state = carState.CarState()
        
        self.control = carControl.CarControl()
        
        self.steer_lock = 0.785398
        self.max_speed = 80
        self.prev_rpm = None

        self.keyPress=[]
        self.filename="data.csv"
        self.predict=model.carPredict(self.filename)

    
    def init(self):
        '''Return init string with rangefinder angles'''
        self.angles = [0 for x in range(19)]
        
        for i in range(5):
            self.angles[i] = -90 + i * 15
            self.angles[18 - i] = 90 - i * 15
        
        for i in range(5, 9):
            self.angles[i] = -20 + (i-5) * 5
            self.angles[18 - i] = 20 - (i-5) * 5
        
        return self.parser.stringify({'init': self.angles})
    def drive(self, msg):
       print('drive')
       keypressed=''
       test=self.state.setFromMsg(msg)
       gear = self.state.getGear()
       accel = self.control.getAccel()
       angle = self.state.angle
       sp = self.state.getSpeedX()
       
       prediction=self.predict.newPrediction(test)
       print("Pred: ", prediction)
       if prediction == "space":
           sp -= 1
           self.state.setSpeedX(sp)

       if prediction == "up arrow":
           keypressed = 'up arrow'
           self.gear()
           self.speed()
       elif prediction == "down arrow":
           keypressed = 'down arrow'
           accel -= -0.1
           self.control.setAccel(accel)
           self.control.setGear(-1)
       else:
           accel -= 0.02
           if accel < 0:
               accel = 0.0
       if prediction == "left arrow":
           self.speed1()

           keypressed = 'left arrow'
           angle += 0.15
           if angle > 3.4:
               angle = 3.4
           self.control.setSteer(angle)
       elif prediction == "right arrow":
           self.speed1()
           
           keypressed = 'right arrow'
           angle -= 0.15
           if angle < -3.4:
               angle = -3.4
           self.control.setSteer(angle)
       else:
           self.control.setSteer(0)
       self.keyPress.append(keypressed)


       return self.control.toMsg()

       
    
    def steer(self):
        angle = self.state.angle
        dist = self.state.trackPos
        
        self.control.setSteer((angle - dist*0.5)/self.steer_lock)
    
    def gear(self):
        rpm = self.state.getRpm()
        gear = self.state.getGear()
        
        if self.prev_rpm == None:
            up = True
        else:
            if (self.prev_rpm - rpm) < 0:
                up = True
            else:
                up = False
        
        if up and rpm > 7000:
            gear += 1
        
        if not up and rpm < 3000:
            gear -= 1
        
        self.control.setGear(gear)

    def speed1(self):
        speed = self.state.getSpeedX()
        accel = self.control.getAccel()
        if speed < self.max_speed:
            accel += 0.05
            if accel > 1:
                accel = 1.0
        else:
            accel -= 0.05
            if accel < 0:
                accel = 0.0

        self.control.setAccel(accel)

        return
    
    def speed(self):
        speed = self.state.getSpeedX()
        accel = self.control.getAccel()
        
        if speed < self.max_speed:
            accel += 0.1
            if accel > 1:
                accel = 1.0
        else:
            accel -= 0.1
            if accel < 0:
                accel = 0.0
        
        self.control.setAccel(accel)

        return
            
        
    def onShutDown(self):
        print("Shut Down func")
        print(self.state.dataset.shape)
        self.state.dataset['keyPress']=self.keyPress
        print(self.state.dataset.shape)
        #self.state.dataset.to_csv(self.filename,mode = 'a', index = False, header = False)
        #self.state.dataset.to_csv("dataset.csv")
        pass
    
    def onRestart(self):
        pass
        