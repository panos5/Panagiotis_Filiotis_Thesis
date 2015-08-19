__author__ = 'Panagiotis Filiotis'

###importing libraries python 2.7
import Tkinter as tk
import tkMessageBox
import PIL
from PIL import Image, ImageTk
from window_size import Window
from naoqi import ALProxy
import threading

class Settings():

    #Initialization of the Settings class
    def __init__(self ,master):
        
        # Declaration of master window which contains all the elements of the class
        # The title Settings assigned to the window  
        self.master = master
        self.master.title('Settings')
        
        
    
#Var    # Declaration of the instance variables of the Setting class
        # scale_value is the variable that controls the volume of the robot 
        # ip_address handles the ip adress of the robot
        # new_ip_address handles the new value entered by the user
        # robot_name has been set to be the value that provides a name to the robot
        # new_robot_name is the value provided by the user to change the name of the robot  
        # connection status is boolean variable checking of the robot is connected or not to the application 
        self.scale_value = tk.IntVar()
        self.ip_address = tk.StringVar()
        self.new_ip_address = tk.StringVar()
        self.robot_name = tk.StringVar()
        self.new_robot_name = tk.StringVar()
        self.connection_status = tk.BooleanVar()



        # Declaration of the frames of the window
        # self.title_frame is the frame that holds the header and the subheader of the window
        # self.volume_frame holds two labels and a scaler responsible for the volume menu
        # self.ip_frame holds the widgets for the existing and the new value of ip of the robot
        # self.name_frame holds the widgets responsible for old and new values of the robot's name
        self.title_fr = tk.Frame(master, relief='ridge')    
        self.volume_fr = tk.Frame(master, relief='ridge')
        self.ip_fr = tk.Frame(master, relief='ridge' )
        self.name_fr = tk.Frame(master, relief='ridge')
        

        # Packing of the frames on the window on a griD layout
        self.title_fr.grid(row=0 ,column=0 , padx=30)
        self.volume_fr.grid(row=1 ,column=0 ,pady =(20,40) )
        self.ip_fr.grid(row=2 ,column=0  )
        self.name_fr.grid(row=3 ,column=0 ,pady =(60,0) )
        
        

#Title  # Declaration of the widgets used on the title_frame
        # window_header label that provides a text for the header of the window
        # window_sub_header label that provides a message below the header 
        self.window_header= tk.Label(self.title_fr, text='Settings', fg = "#0066FF" ,font=("AnuDaw", 14))
        self.window_sub_header = tk.Label(self.title_fr, text="'' In this section you can modify some of the robot's settings '' ", font=("Arial", 9 ,"italic"))

        # Packing of the widgets of title_frame
        self.window_header.grid(row=0, column=0, pady=(15,0))
        self.window_sub_header.grid(row=1, column=0, pady=(5,20))



#Volume # Declaration of the widgets used on the volume_frame
        # scaler_lbl label of the header of the volume fram panel
        # scale scale used to provide a range of values and adjust the volume of the robot's speaker
        # test_vol tests the volume of the spearks by producing a voice message from the robot
        self.scaler_lbl = tk.Label(self.volume_fr , text="Volume Adjustment" , font=("Arial", 10 ,"bold") )
        self.scale = tk.Scale( self.volume_fr, variable = self.scale_value ,from_ ='0', to= "100", orient='horizontal' , relief = 'groove' ,bd=3 , length =220 ,command = self.set_scale )
        self.test_vol_bt = tk.Button(self.volume_fr,text = "Test Volume" , height=1 ,bd=3,bg='#33CC66',command = self.test_sound  )
        
    

        # Packing of the widgets of volume_frame
        self.scaler_lbl.grid(row=0 ,column=1 ,pady=(0,15), columnspan=3 )
        self.scale.grid(row=1 ,column=1 ,columnspan=2 ,padx=(20,20) )
        self.test_vol_bt.grid(row=1 ,column=3 ,padx = (10,0) ,rowspan=2 , ipadx=5 )



#IP     # Declaration of the widgets used on the ip_frame
        # ip_lbl  header of ip modification panel 
        # current_ip_lbl  label showing a text  "current IP" 
        # new_ip_lbl  label showing a text  "new IP" 
        # current_ip_ent  entry box shows the default value for the ip
        # new_ip_ent  entry that allows user enter the new value of the desired ip
        # change_ip_bt  button that calls change_ip() function to replace the value of the ip
        self.ip_lbl = tk.Label(self.ip_fr , text="IP  Configuration" , font=("Arial", 9 ,"bold"))
        self.ip_subheader_lbl = tk.Label(self.ip_fr , text="The IP has to be in the format : xxx.xxx.xxx.xx" , font=("Arial", 10 ,"italic"))
        self.current_ip_lbl = tk.Label(self.ip_fr , text="Current IP" )
        self.new_ip_lbl = tk.Label(self.ip_fr , text="New IP" )
        self.current_ip_ent = tk.Entry( self.ip_fr, relief = 'groove' ,bd=5 ,textvariable = self.ip_address)
        self.current_ip_ent.config(state='disabled')
        self.new_ip_ent = tk.Entry( self.ip_fr, textvariable = self.new_ip_address , relief = 'groove' ,bd=5 )
        self.change_ip_bt = tk.Button(self.ip_fr, text="Connect" ,height=1 ,bd=3,bg='#3366FF' , fg = "white", command = self.change_ip)


        # Packing of the widgets of the ip frame
        self.ip_lbl.grid(row=0 ,column=0 ,pady=(0,15) ,columnspan=3 )
        self.ip_subheader_lbl.grid(row=1 ,column=0 ,padx =(0,30) , columnspan=3 )
        self.current_ip_lbl.grid(row=2 ,column=0 ,padx =(0,30) , pady=10 )
        self.current_ip_ent.grid(row=2 ,column=1 )
        self.new_ip_lbl.grid(row=3 ,column=0 ,padx = (0,30))
        self.new_ip_ent.grid(row=3 ,column=1 ) 
        self.change_ip_bt.grid(row=2 ,column=2, padx = (20,0) ,ipadx=10 ,rowspan=2)
        
    

#Name   # Declaration of the widgets used on the name_frame
        # robot_name_lbl  header of name modification panel 
        # current_name_lbl  label showing a text  "current name" 
        # current_name_val  value of the current name
        # new_name_ent   label showing a text "name entry"
        # change_name_ent  entry that allows user enter the new value of the desired name
        # change_name_bt  button that calls change_name() function to replace the value of the name 
        self.robot_name_lbl = tk.Label(self.name_fr , text="Name Modification" , font=("Arial", 10 ,"bold") )
        self.current_name_lbl = tk.Label(self.name_fr , text="Current Robot's Name : " )
        self.current_name_val = tk.Label(self.name_fr ,textvariable= self.robot_name , font=("Arial", 9 , "bold") )
        self.new_name_ent = tk.Entry( self.name_fr, relief = 'groove' , textvariable = self.new_robot_name , bd=5)
        self.change_name_bt = tk.Button(self.name_fr, text="Change Name" ,height=1 ,bd=3 ,bg='#33CC66' , command = self.change_name)


        # Packing of all the widgets of the frame which hold the details for changing the name
        self.robot_name_lbl.grid(row=0 ,column=0 ,pady=(0,15) ,columnspan=2 )
        self.current_name_lbl.grid(row=1 ,column=0  , pady=10 )
        self.current_name_val.grid(row=1 ,column=1 ,padx =(0,10) , pady=15 )
        self.new_name_ent.grid(row=2 ,column=0 )
        self.change_name_bt.grid(row=2 ,column=1 ,padx = 20 , ipadx=5)
        
        # Image label at the bottom of the page.Image is loaded and placed inside a label
        # which has been packed on the name frame
        image = Image.open("nao.png")
        photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.name_fr , image=photo) 
        self.image_label.image = photo
        self.image_label.grid(row=3 ,column=0 ,columnspan=2 ,pady = (20,0))
        
        
 
        # read_values method is called in order to get the default values and display it relatively into the boxes
        # check_connection is called to check if the connection is active or not
        self.read_values()
        self.check_connection()
        
    
    # Reads the data from the ip_and_name text file,gets the default values,saves them into a temporary list
    # and then sets the right values into the relevant widgets of name and ip variables   
    def read_values(self):
        
        filein = open("ip_and_name.txt", "r")
        temporary_list = filein.readlines()
        temporary_list = [lines.rstrip() for lines in temporary_list] 
        
        self.ip_address.set(temporary_list[0])
        self.robot_name.set(temporary_list[1])
        self.scale_value.set(temporary_list[2])
        filein.close()
        
    
    
    # Opens the file anytime is called and write the values to the same text file accordingly
    def write_values_to_text(self , place , value):
        
       
         # Reads the file ,gets the entry related to the name Of the robot and replaces it with the new one given
         filein = open("ip_and_name.txt", "r")
         temporary_list = filein.readlines()
             
         temporary_list = [lines.rstrip() + '\n' for lines in temporary_list] 
         temporary_list.pop(place)
         temporary_list.insert(place, value +'\n')
             
         fileout = open("ip_and_name.txt", "w")
         fileout.writelines(temporary_list)
             
         #Closes the files opened for writing and reading
         filein.close()
         fileout.close()   
      
        

    # Used to test the volume of the microphones just by playing a sound
    # A condition always is checked when the method is called
    # If the connection is active or not 
    def test_sound(self):
         if(self.ip_address.get()) == "Disconnected":
            return
         else:  
            self.write_values_to_text(2, str(self.scale_value.get()))  
            self.tts.say("Testing the sound")   
        
   
   
    # Sets the value of the scale according to the value of the volume that the robot has the specific moment 
    # A check is always done by checking the value of the ip_address if the connection is open or closed
    def set_scale(self ,value):
        
        if(self.ip_address.get()) == 'Disconnected':
            return
        else:  
            
            # Creates all the relevant modules that are related to the audio and sets the volume of the microphones depending the value
            # that the scale_value has
            
            self.audio = ALProxy("ALAudioDevice", self.ip_address.get(), 9559)
            value = self.scale_value.get()
            self.audio.setOutputVolume(value) 
    
     
    
    # Check if the connection is active or not
    # The check is been done by always reading the value of the ip address in the relevant box
    # If the value of ip_address is Disconnected just sets the value of the connection_status to false so other checks can be done 
    # simultaneously elsewhere in the program
    # If the connection is active creates some modules and sets the value of the scale according to the one that the robot has hat moment  
    def check_connection(self):
        
        if(self.ip_address.get()) == "Disconnected":
            self.connection_status = False
            return   
                         
        else: 
            #alconnman = ALProxy("ALConnectionManager",self.ip_address.get(), 9559)
            #print "network state: " + alconnman.state()
            #if(alconnman.state()) == "online":
            try:
      
                 # Imports ALMemory module and use pings to check if the connection with the robot is alive 
                 self.memory = ALProxy("ALMemory", self.ip_address.get(), 9559)
                 self.memory.ping()
                 
                 # Creates a module to check if a connection can be established or not 
                 self.tts = ALProxy("ALTextToSpeech", self.ip_address.get(), 9559)   
                 self.connection_status = True   
                 
            except RuntimeError, err:   
                    self.ip_address.set(self.temp_value)
                    self.connection_status = False
                    tkMessageBox.showwarning("Connection Error", "Please check again the IP that you have provided.\n\nThe IP has to be in the format xxx.xxx.xxx.xx")
          

    # Changes the value that holds the ip of the robot.Initially checks if the entry text is empty and throws a warning  message that
    # informs the user to set a proper text to the field.
    # Another condirtion checks if the ip in the two fields are the same so to throw again  a warning message to the user  
    def change_ip(self):
        
        #Checks if the entry text of the new ip address is empty and throws a message
        if len(self.new_ip_address.get()) == 0:
            tkMessageBox.showwarning("Error - Input Field Empty", "Please provide a proper IP into the empty field")
        elif self.new_ip_address.get() == self.ip_address.get():
            tkMessageBox.showwarning("Notification - Same IP address", "You have already provided the same IP")
        else:                   
           try:               
                self.temp_value = self.ip_address.get()
                # Replaces the value of the ip with the new one and checks the connectivity and sets the 
                self.ip_address.set(self.new_ip_address.get())
               
                self.check_connection()
  
                # If connection is active the robot confirms it with a voice message and also at the same time a message is displayed on the screen 
                if (self.connection_status) == True :
                    
      
                    self.tts.say("Great news.I have connected with the application")    
                                    
                    tkMessageBox.showwarning("Connection established", "Connection with Nao was successful")
                    
                    
                    # Generates the modules that are related to the audio functionalities of the robot
                    self.memory = ALProxy("ALMemory", self.ip_address.get() , 9559)
                    self.audio = ALProxy("ALAudioDevice", self.ip_address.get(), 9559)
                    self.scale_value.set(self.audio.getOutputVolume())
                   
                    # The new value is written to a text file
                    self.write_values_to_text(0, self.ip_address.get())   
                    
                    self.new_ip_ent.delete(0 ,'end')
                else : 
                    return
                     
            ##Throws an exception and a message in case that a connection didn't manage to be established
           except Exception, e:  
                tkMessageBox.showwarning("Connection Error", "Please check again the IP you have provided")               
                print("error was : " , e)

    
    # Changes the value that holds the name of the robot.Initially checks if the entry text is empty and throws a warning  message that
    # informs the user to set a proper name to the field.Then if a value exists in the the field ,reads a text file and writes to it the new value.
    def change_name(self):
        
        if len(self.new_robot_name.get()) == 0: 
            tkMessageBox.showwarning("Error - Input Field Empty", "Please provide a name into the empty text field")
        else:
          
            if(self.ip_address.get()) == "Disconnected":
                tkMessageBox.showwarning("Connection Error" , "You have to connect Nao first if you want to change the name")
                self.new_name_ent .delete(0 ,'end')
                return  
                
            else :  
      
                # Inserts the new name to the name label and then by calling the write_values_to_test method
                # writes/replaces the new value to the first line of the text file
                # Also clears the entry text box of the new name 
                self.robot_name.set(self.new_robot_name.get())
                self.write_values_to_text(1, self.new_robot_name.get())
                self.tts.say("My new name is" + self.new_robot_name.get())
                self.new_name_ent.delete(0 ,'end')
             
              
                 #self.panos = ALProxy("ALSystem", self.ip_address.get(), 9559)
                 #self.systemmm.setRobotName(self.new_robot_name.get())
                 #print(self.new_robot_name.get())
                 #print(self.memory.robotName.get())
                 #print(socket.gethostname())
            
             
             
## title and position of the window on the screen
#settings_window = tk.Tk()
#settings_window.title('Settings')

#new_window = Window() 
#new_window.center_window(settings_window,400,625)

#app = Settings(settings_window )

#settings_window.mainloop()

