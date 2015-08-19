import threading
 
 
    
class Battery():
    
    
    def battery_label(self):
         
         from naoqi import ALProxy
         battery = ALProxy("ALBattery", self.ip.get() , 9559)
        
         
         if  "0 %" <= str(self.battery.getBatteryCharge()) <= "40 %":      
           self.battery_image = Image.open("battery00.png")
           self.tts.say("My battery level is low")  
         else:
         
            pass
         
         threading.Timer(15.0, self.update_battery).start()       
            

         
                
      
                   
         
