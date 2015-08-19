__author__ = 'Panagiotis Filiotis'

# Importing the libraries needed for Python 2.7
import Tkinter as tk
import tkMessageBox
import PIL
from PIL import Image, ImageTk
from window_size import Window
#import pygame
import threading
from naoqi import ALProxy

# Imports from setting python file the class Settings
from settings import Settings


class Top_Bar_Frame():

    #initializes the Top Bar Frame
    def __init__(self,master):
        
        
         # Declaration of the master frame which will hold all the frames of
         # the window.Also a title has given to master frame
         self.master = master
         self.master.title('Nao Robot Demonstrator')
      
        
         # Declaration of instance variable for the name of the robot
         # self.name is the variable that determines the name of the robot : default value is NAO
         self.name = tk.StringVar()
         self.name.set("NAO")
        
        
         # Top bar frame that provides information about the name of the robot
         top_bar_frame = tk.Frame(master,relief='groove', bd=3)
         top_bar_frame.pack(side='top',padx=(20,0) ,ipady= 10 ,ipadx = 10)


         # Declaration and packing of top frame widgets(label name and value of the name)
         self.robot_name= tk.Label(top_bar_frame, text="Robot's Name  :  " , font=("AnuDaw", 11))
         self.robot_name.pack(side='left', padx =(5,0))
        
         self.name_value= tk.Label(top_bar_frame , textvariable = self.name , font=("AnuDaw", 11 ,"bold") , fg = '#3366FF')
         self.name_value.pack(side='left')

       

class Bottom_Frame():

    #initializes the bottom bar frame
    def __init__(self,master):

        
         # Declaration of the frames that exist on the bottom frame and packing
         # bottom_frame frame that holds the title and an info message of the main window
         # buttons_frame frame that holds all the buttons of the main window 
         self.master = master
         bottom_fr = tk.Frame(master)
         buttons_fr = tk.Frame(bottom_fr)
         bottom_fr.pack(side='bottom')
         buttons_fr.pack(side='bottom')

         # Declaration of the widgets of the bottom frame
         # top_header_lbl label that the text is the main title inside of the window
         # info header_lbl label that holds an information message of the functionality that is provided from the main window
         self.top_header_lbl= tk.Label(bottom_fr, width=50, text="Welcome to NAO's world", fg='#6666FF',font=("AnuDaw", 25))
         self.info_header_lbl= tk.Label(bottom_fr,wraplength=450, height=10 ,text="'' Here is the main panel of the application . "
                                         "Please press on the button of your preference and then Nao will respond accordingly ''" , font=("Arial", 11, 'italic' ))


         # Declaration of the eleemnts of the buttons frame and packing of the elments on a grid layout
         # motion _bt button that when is clicked opens the motion window
         # speech_bt button that when is clicked opens the speech window
         # demonstration_bt button that when is clicked opens the demo window
         # lab_info_bt button that when is clicked opens the lab info window
         # manual_bt button that when is clicked opens the manual window
         # settings_bt button that when is clicked opens the manual window
         self.motion_bt = tk.Button(buttons_fr, text="Motion", width=15, height=3, wraplength=50, relief ="raise" , bd=5 , bg = "#3399FF", fg = "white" , command = self.motion_window )
         self.speech_bt = tk.Button(buttons_fr, text="Speech", width=15, height=3, wraplength=50, relief ="raise" , bd=5 , bg = "#009966" ,  fg = "white" ,  command= self.speech_window)
         self.demonstration_bt = tk.Button(buttons_fr, text="Demonstrations", width=15, height=3, wraplength=95, relief ="raise" , bd=5 , bg = "#9999FF" , fg = "white" ,command = self.demo_window)
         self.lab_info_bt = tk.Button(buttons_fr, text="Robotics Lab Information", width=15, height=3, wraplength=80, relief ="raise" , bd=5 ,   bg = "#CC9966",fg = "white" ,command = self.lab_info_window)
         self.manual_bt = tk.Button(buttons_fr, text="How to connect Nao", width=15, height=3, wraplength=90,  relief ="raise" , bd=5 , bg = "#FF9966" ,fg = "white", command = self.manual_window)
         self.settings_bt = tk.Button(buttons_fr, text="Settings", width=15, height=3  , wraplength=50, relief ="raise" , bd=5 , bg = "#6633FF"  , fg="white"  , command = self.settings_window)
         self.stiffness_fr = tk.Frame(buttons_fr , relief='groove', bd=3)
         self.stiffness_lbl = tk.Label(self.stiffness_fr, text="Stiffness : " ,font=("AnuDaw", 10))
         self.stiffness_on_bt = tk.Button(self.stiffness_fr, text="ON" ,width=3 ,height = 1 , relief ="raise" , bd=3 ,command = self.stiffness_on)
         self.stiffness_off_bt = tk.Button(self.stiffness_fr, text="OFF" ,width=3 ,relief ="raise" , bd=3  , command = self.stiffness_off)
         
         
         
         # Packing of the widgets of the bottom and buttons frames
         self.top_header_lbl.pack(side='top', pady=(45,5))
         self.info_header_lbl.pack(pady=(0,15))
         
         self.motion_bt.grid(row=1, column=1, pady=(0,40))
         self.speech_bt.grid(row=1, column=2, pady=(0,40) ,padx=50)
         self.demonstration_bt.grid(row=1, column=3, pady=(0,40))
         self.manual_bt.grid(row=2 , column=2 , pady=(0,80),padx=50)
         self.lab_info_bt.grid(row=2, column=3, pady=(0,80))
         self.settings_bt.grid(row=2, column=1,pady=(0,80) )
         self.stiffness_fr.grid(row=3, column=1 , columnspan=2,  ipady=10 )
         self.stiffness_lbl.pack(side='left' ,padx = (5,5))
         self.stiffness_on_bt.pack(side='left' , padx = 5)
         self.stiffness_off_bt.pack(side='left' ,padx=(0,5))
        
 
  
    def stiffness_on(self):
        if (main_right.ip.get()) == "Disconnected":
             return    
        else :
             main_right.motion.setStiffnesses("Body", 1.0) 
             self.stiffness_on_bt.config(fg = "#009966", font=("Arial", 10 ,"bold"))
             self.stiffness_off_bt.config(fg = "black" , font=("Arial", 6 ,"normal")) 
    
             main_right.tts.say("Stiffness is on")
  
  
    
    def stiffness_off(self):
        if (main_right.ip.get()) == "Disconnected":
             return
        else :
            if(main_right.posture.getPostureFamily()) == "Sitting":
                main_right.motion.setStiffnesses("Body" , 0.0)
                self.stiffness_off_bt.config(fg = "red",font=("Arial", 10 ,"bold"))
                self.stiffness_on_bt.config(fg = "black" ,font=("Arial", 6 ,"normal")) 
                main_right.tts.say("Stiffness has removed") 
            else: 
                question = tkMessageBox.askyesno("Remove Stifness", "The robot is on an upright position.\nAre you sure you want to remove the stiffness?\nIf you choose yes robot may fall.") 
                if question==True:
                    main_right.motion.setStiffnesses("Body" , 0.0)
                    self.stiffness_off_bt.config(fg = "red",font=("Arial", 11 ,"bold"))
                    self.stiffness_on_bt.config(fg = "black" ,font=("Arial", 7 ,"normal")) 
                    main_right.tts.say("Stiffness has removed")
                else:
                    return
     
    
     
    def update_stiffness(self):
        
         if (main_right.ip.get()) == "Disconnected":
             return
         else :
            self.stiffness_status = main_right.motion.getStiffnesses("Body")
            
            if (self.stiffness_status[0]) == 0.0:
              self.stiffness_off_bt.config(fg = "red",font=("Arial", 11 ,"bold"))
              self.stiffness_on_bt.config(fg = "black" ,font=("Arial", 7 ,"normal")) 
            else:  
              self.stiffness_on_bt.config(fg = "#009966", font=("Arial", 11 ,"bold"))
              self.stiffness_off_bt.config(fg = "black" , font=("Arial", 7 ,"normal"))     
     
             
             
    # Opens the motion window
    # initially imports the class from the relevant python file and then creates a pop-up window
    # that will hold all the elements of the class and make a proper interface
    # Next an object from the class Window is created in purpose of calling the center_window method to put the 
    # new window on the center of the screen.Finally the protocol when the window will colse is set to call the iconify__main_panel method 
    def motion_window(self):
        
         from motion import Motion
         self.motion_window = tk.Toplevel(self.master)
         main_window.withdraw()
         new_window = Window()
         new_window.center_window(self.motion_window,805,680)
         self.app = Motion(self.motion_window)       
         
         self.motion_window.protocol("WM_DELETE_WINDOW", lambda: self.iconify_main_panel(self.motion_window) )
      
        
    # Opens the speech window
    # initially imports the class from the relevant python file and then creates a pop-up window
    # that will hold all the elements of the class and make a proper interface
    # Next an object from the class Window is created in purpose of calling the center_window method to put the 
    # new window on the center of the screen.Finally the protocol when the window will colse is set to call the iconify__main_panel method 
    def speech_window(self):
        
         from speech import Speech
         self.speech_window = tk.Toplevel()
         main_window.withdraw()
         new_window = Window() 
         new_window.center_window(self.speech_window,910,790)
         self.app = Speech(self.speech_window)
         self.speech_window.protocol("WM_DELETE_WINDOW", lambda: self.iconify_main_panel(self.speech_window) )
    
    
    # Opens the lab_info window
    # initially imports the class from the relevant python file and then creates a pop-up window
    # that will hold all the elements of the class and make a proper interface
    # Next an object from the class Window is created in purpose of calling the center_window method to put the 
    # new window on the center of the screen.Finally the protocol when the window will colse is set to call the iconify__main_panel method   
    def lab_info_window(self):
        
         from robotics_lab import Lab_Info
         self.lab_info_window = tk.Toplevel(self.master)
         main_window.withdraw()
         new_window = Window() 
         new_window.center_window(self.lab_info_window,520,410)
         self.app = Lab_Info(self.lab_info_window)
         self.lab_info_window.protocol("WM_DELETE_WINDOW", lambda: self.iconify_main_panel(self.lab_info_window) )
         

    # Opens the settings window
    # initially imports the class from the relevant python file and then creates a pop-up window
    # that will hold all the elements of the class and make a proper interface
    # Next an object from the class Window is created in purpose of calling the center_window method to put the 
    # new window on the center of the screen.Finally the protocol when the window will colse is set to call the iconify__main_panel method 
    def settings_window(self):
    
         self.settings_window = tk.Toplevel(self.master)
         new_window = Window() 
         main_window.withdraw()
         new_window.center_window(self.settings_window,400,675)
         self.app = Settings(self.settings_window)
         self.settings_window.protocol("WM_DELETE_WINDOW", lambda: self.iconify_main_panel(self.settings_window) )
   
    
    # Opens the demo window
    # initially imports the class from the relevant python file and then creates a pop-up window
    # that will hold all the elements of the class and make a proper interface
    # Next an object from the class Window is created in purpose of calling the center_window method to put the 
    # new window on the center of the screen.Finally the protocol when the window will colse is set to call the iconify__main_panel method     
    def demo_window(self):
        
         from demonstration import Demonstration
         self.demo_window = tk.Toplevel(self.master)
         main_window.withdraw()
         new_window = Window() 
         new_window.center_window(self.demo_window,450,580)
         self.app = Demonstration(self.demo_window)
         self.demo_window.protocol("WM_DELETE_WINDOW", lambda: self.iconify_main_panel(self.demo_window) )
    
    
    
    # Creates a new window which consists of an image   
    # The dimensions and the title of the window are set
    # The protocol when the window closes remain the same like the other windows so the iconify_main_panel method is called 
    def manual_window(self):
        
         self.manual_window = tk.Toplevel(self.master)
         self.manual_window.title('How to connect Nao')
         main_window.withdraw()
         new_window = Window() 
         new_window.center_window(self.manual_window,500,645)
         
         image = Image.open("the_manual.jpg")
         photo = ImageTk.PhotoImage(image)
         self.image_lbl = tk.Label(self.manual_window, image=photo) 
         self.image_lbl.image = photo
        
         self.exit_bt = tk.Button(self.manual_window, text = "Go Back to the Main Panel" ,width=15, height=3, wraplength=90,  relief ="raise" , bd=5 , bg = "#3399FF", fg = "black" , command = lambda: self.iconify_main_panel(self.manual_window)) 
         
         self.image_lbl.grid(row=0 , column =0)
         self.exit_bt.grid(row=1 , column =0 , pady = (10,0) , columnspan=2)
         
         
         self.manual_window.protocol("WM_DELETE_WINDOW", lambda: self.iconify_main_panel(self.manual_window) )
    
        
    
    
    # Sets the values of some variables of the class to specific values depending what is read from the text file
    # ip_and_name_txt  and calls the battery_label method to check the percentage of the battery  
    def iconify_main_panel(self,root):
         
         
         # reads the data from the ip_and_name text file,saves it to a temporary list
         #and then set the right values on the relevant widgets of name and ip variables
         filein = open("ip_and_name.txt", "r")
         temporary_list = filein.readlines()
         temporary_list = [lines.rstrip() for lines in temporary_list] 
        
         for lines in temporary_list:
            main_right.ip.set(temporary_list[0])
            main_top.name.set(temporary_list[1])
            filein.close()
            
            
         #main_right.update_battery()   
         main_right.battery_label()
         main_bottom.update_stiffness()
         main_window.deiconify()
         
         root.destroy()
    
    
    # When the x is pressed on the top right of the window a message is thrown asking the user if is sure to exit the application or not
    # Depending the choice an action is taken
    def main_window_close(self):
    
        question = tkMessageBox.askyesno("Exit", "Are you really want to quit the application?")
        # If the answer is yes then the default values for the ip and name of the robot are wrtten on the text file
        if question==True:
            main_window.destroy()
            filein = open("ip_and_name.txt", "r")
            temporary_list = filein.readlines()
             
            temporary_list = [lines.rstrip() + '\n' for lines in temporary_list] 
            temporary_list.pop(0)
            temporary_list.pop(0)
            temporary_list.insert(0, "Disconnected" +'\n')
            temporary_list.insert(1, "NAO" +'\n')
            fileout = open("ip_and_name.txt", "w")
            fileout.writelines(temporary_list)
            filein.close()
            fileout.close()           
        else:
            return
            

class Right_Frame():
    
    
    def __init__(self,master):
               
         # Declaration of the instance variables used within the class
         # ip  holds a value for the ip address of the robot
         # battery_status holds a value displayong the percentage has left in the battey
         self.ip = tk.StringVar()
         self.battery_status = tk.StringVar()

         self.ip.set("Disconnected")  

         # Declaration of the frames that exist on the right frame and packing
         # left_fr frame that holds a label and an other frame
         # image_fr frame that holds an image of Nao robot
         # ip_battery_fr  holds elements dispalyong info about the ip and the battery staus of the robot
         left_fr = tk.Frame(main_window)
         left_fr.pack(side='right', fill= 'y')
         
         image_fr =tk.Frame(left_fr)
         image_fr.grid(row=0 ,column=0 ,pady = (10,10))
         
         self.ip_battery_fr =tk.Frame(left_fr ,relief='groove', bd=3)
         self.ip_battery_fr.grid(row=1 ,column=0)    
         
         # Declaration of the image showing NAO and positionng in a label  
         image = Image.open("naoStand.png")
         photo = ImageTk.PhotoImage(image)
         self_label_image = tk.Label(image_fr, image=photo)
         self_label_image.image = photo
         self_label_image.pack (padx=(40,0))
         
         # Called to create and position the label related to the battery information
         self.battery_label() 
         
    
         # Label that displays the percentage of the battery 
         self.battery_val= tk.Label(self.ip_battery_fr, textvariable = self.battery_status , font=("Arial", 11 ,"italic"))
         self.battery_val.grid(row=0 ,column=1 , padx=(0,55))
        
         # Declaration of the network image and positionng in a label
         ip_image = Image.open("network.png")
         ip_photo = ImageTk.PhotoImage(ip_image)
         self_ip_lbl = tk.Label(self.ip_battery_fr, image=ip_photo , text = " IP address : " , compound = 'left' , padx = 5)
         self_ip_lbl.image = ip_photo
         self_ip_lbl.grid(row=0 ,column=2 )
  
         # Label that displays the ip of the robot
         self.ip_val= tk.Label(self.ip_battery_fr, textvariable = self.ip , font=("Arial", 11 ,"italic"))
         self.ip_val.grid(row=0 ,column=3 ,padx=(0,20))
    
     
    # Depending of th value that the battery_status variable gets displays a different image on the label of the battery     
    def battery_label(self):
         
        
         self.update_battery()
     
         if  "0 %" <= self.battery_status.get() <= "10 %":      
           self.battery_image = Image.open("battery00.png")
  
         elif  "11 %" <= self.battery_status.get() <= "25 %":
           self.tts.say("My battery level is low")   
           self.battery_image = Image.open("battery20.png")
           
         elif  "26 %" <= self.battery_status.get() <= "45 %":          
           self.battery_image = Image.open("battery40.png") 
         
         elif  "46 %" <= self.battery_status.get() <= "65 %": 
           self.battery_image = Image.open("battery60.png")    
           
         elif  "66 %" <= self.battery_status.get() <= "79 %": 
           self.battery_image = Image.open("battery80.png")

         elif  "80 %" <= self.battery_status.get() <= "100 %": 
           self.battery_image = Image.open("battery100.png")
         
         else:
           self.battery_image = Image.open("battery00.png")
                   
        # Declaration of the image that the battery label will hold and packing of the widget on a grid layout
         self.battery_photo = ImageTk.PhotoImage(self.battery_image)
         self_battery_label = tk.Label(self.ip_battery_fr, image=self.battery_photo)
         self_battery_label.image = self.battery_photo
         self_battery_label.grid(row=0 ,column=0 , padx=(20,15) ,ipady=10)
         

    
    # Responsble of updating the value of the battery on real time.
    # an initial check is done to check if the connection is active or not 
    # if the robot is disconnected nothing happens
    # if the robot is connected then ALProxy is inserted ant the relevant modules are created in  order to get the value of the robot 
    # when the value is extracted is set instantly to the battery_status variable.
    def update_battery(self):
         
         if (self.ip.get()) == "Disconnected":
             self.battery_status.set("0 %")
         else :
             try:
                ## import naoqi library and creates all the relevant modules that will be used 
                from naoqi import ALProxy
                                
                self.memory = ALProxy("ALMemory", self.ip.get() , 9559)
                self.memory.ping()       
                self.battery = ALProxy("ALBattery", self.ip.get() , 9559)
                self.tts = ALProxy("ALTextToSpeech", self.ip.get() , 9559)
                self.motion = ALProxy("ALMotion" , self.ip.get() , 9559)
                self.posture = ALProxy("ALRobotPosture", self.ip.get(), 9559)
                
                #Sets the status of the battery to the existent value
                self.battery_status.set(str(self.battery.getBatteryCharge())  + " %")
              
                # Thread that updates the battery status after specific period of time   
                #threading.Timer(5.0, self.update_battery).start()  
                threading.Timer(15.0, self.update_battery).start() 

             except BaseException:
				 
                 self.ip.set("Disconnected")  
                 return    


# A new window with specified dimensions and a title has been created
# The window has been declared to remain on the same size and the user cannot alter its dimensions
main_window = tk.Tk()
main_window.title('Panos Nao Robot Demonstrator')
main_window.resizable(width="false", height="false")

# Objects of the three classes of the file are declared
main_right = Right_Frame(main_window)
main_top = Top_Bar_Frame(main_window)
main_bottom = Bottom_Frame(main_window)

# An object from the class Windowis created with the purpose to set the window on the center of the screen
new_window = Window() 
new_window.center_window(main_window,1100,605)
#new_bar= Top_Bar()
#new_bar.top_bar(main_window)

# When the window closes the main_close_window method is called at the same time
main_window.protocol("WM_DELETE_WINDOW", lambda: main_bottom.main_window_close() )

main_window.mainloop()
