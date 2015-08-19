__author__ = 'Panagiotis Filiotis'


###importing all the necessary libraries for python 2.7
import Tkinter as tk
import tkMessageBox
import PIL
from PIL import Image, ImageTk
from window_size import Window
import random
import sys
import time
import math
import threading


class Motion(tk.Frame):
    
    #Initialization of the widgets of the Motion window
    def __init__(self ,master):
             
        # Declaration of master window which contains all the elements of the class
        # Title assigned to the window        
        self.master = master
        self.master.title('Motion Control')
   
#Keyboard's commands Frame
        
        # Declaration of the frames holding the elements 
        # header_fr includes the header and the subheader of the window
        # top buttons_fr includes sit down and stand up button
        # directions_buttons_fr includes the buttons which are responsible providing direction commands to the robot
        # bottom_buttons_fr includes turn left and turn right buttons      
        self.header_fr = tk.Frame(master)
        self.header_fr.grid(row=0 , column=0 , pady =(10,30))

        self.top_buttons_fr = tk.Frame(master)
        self.top_buttons_fr.grid(row=1 , column=0 , pady =(10,30)) 
        
        self.direction_buttons_fr = tk.Frame(master, bd = 7 , relief = "groove")
        self.direction_buttons_fr.grid(row=2 ,column=0 )
        
        self.log_history_fr = tk.Frame(master)
        self.log_history_fr.grid(row=1 ,column=1 , rowspan=3 ,columnspan=2 )

        self.bottom_buttons_fr = tk.Frame(master)
        self.bottom_buttons_fr.grid(row=3 , column=0 , pady =(30,30)) 

        
#Header # Declaration of the widgets placed on the header frame and packing
        # header_lbl has the header of the window
        # sub_header_lbl  is the subheader of the window
        self.header_lbl = tk.Label(self.header_fr, text="Keyboard Commands", fg = "#0066FF" ,font=("AnuDaw", 14))
        self.sub_header_lbl = tk.Label(self.header_fr, text="''  Use buttons below to make NAO move accordingly ''", font=("Arial", 10 ,"italic"))        
        self.header_lbl.grid(row=0 ,column=0)
        self.sub_header_lbl.grid(row=1 ,column=0)
        
        
        
#Top    # Declaration of the widgets placed on the buttons frame and packing
        # sit_down button commands the robot to sit down
        # stand_up button commands the robot to go in an upright position
        self.sit_down_bt = tk.Button(self.top_buttons_fr, text="Sit down", width= 8, height=2, wraplength=75 ,relief='raised', bd=5 , command=self.sit_down)
        self.crouch_bt = tk.Button(self.top_buttons_fr, text="Crouch", width= 8, height=2, wraplength=75,relief='raised', bd=5 , command=self.crouch)
        self.stand_up_bt = tk.Button(self.top_buttons_fr, text="Stand up", width= 8, height=2, wraplength=75,relief='raised', bd=5 , command=self.stand_up)
        self.sit_down_bt.grid(row=0 ,column=0 , padx=(0,20))
        self.crouch_bt.grid(row=0 ,column=1 , padx=(0,20) )
        self.stand_up_bt.grid(row=0 ,column=2 )
        
        
        
#Direct # Declaration of the widgets placed on the directions buttons frame and placing according to a grid geometry
        # move_forward button gives the command to the robot to move forward 
        # move_left  button gives the command to the robot to move left
        # move_right button gives the command to the robot to move right
        # move_back  button gives the command to the robot to move back
        self.move_forward_bt = tk.Button(self.direction_buttons_fr, text="Move Forward", width=8, height=2,relief='raised',wraplength=60, bd=5 ,command=self.move_forward)
        self.move_left_bt = tk.Button(self.direction_buttons_fr, text="Move Left", width=8, height=2,relief='raised',wraplength=50, bd=5 , command=self.move_left)
        self.move_right_bt = tk.Button(self.direction_buttons_fr, text="Move Right", width=8, height=2,relief='raised',wraplength=60, bd=5,command = self.move_right)
        self.move_back_bt = tk.Button(self.direction_buttons_fr, text="Move Back", width=8, height=2,relief='raised',wraplength=60,  bd=5 , command= self.move_back)
        self.move_forward_bt.grid(row=0, column=1 ,pady=(10,10))
        self.move_left_bt.grid(row=1, column=0 ,padx=(20,10))
        self.move_right_bt.grid(row=1, column=2 ,padx=(10,20))
        self.move_back_bt.grid(row=2, column=1 ,pady=(10,20))
        
        
        # Declaration of the log frame , the elements that holds and how they are packed
        # log_fr frame that holds a label and a list
        # log_title_lbl  label that displays a text as header for the log frame 
        # clear_log button that clears the log file history
        self.log_fr =tk.Frame(self.log_history_fr, width=250 , height=250)
        self.log_fr.grid(row=0, column=0, padx=10)
        self.log_title_lbl = tk.Label(self.log_fr , text= 'Movements Log' ,fg = "#0066FF" , font=("AnuDaw", 11))
        self.log_title_lbl.pack(side='top',pady = (0,10))

        self.scrollbar = tk.Scrollbar(self.log_fr, orient='vertical')
        self.log_list = tk.Listbox(self.log_fr , height = 20, width = 30 , yscrollcommand=self.scrollbar.set)
        # self.log_list.bind( "<Double-Button-1>" , self.pass_value )
        self.scrollbar.config(command=self.log_list.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.log_list.pack(side='bottom')
        
        
#Bottom # Declaration and placing of the widgets placed on the bottom buttons frame
        # turn_left  button gives the command to the robot to turn left
        # turn_right button gives the command to the robot to turn right
        self.turn_left_bt = tk.Button(self.bottom_buttons_fr, text="Turn Left", width=8, height=2,relief='raised',wraplength=40,  bd=5 ,command=self.turn_left )
        self.turn_right_bt = tk.Button(self.bottom_buttons_fr, text="Turn Right", width=8, height=2,relief='raised',wraplength=60,  bd=5 ,command=self.turn_right)
        self.turn_left_bt.grid(row=1 ,column=0,pady=(0,15) , padx=(0,20))
        self.turn_right_bt.grid(row=1 ,column=2 ,pady=(0,15)) 
        
         
#Voice commands Frame  
        
        # Declaration and packing of the frame holding the voice command elements
        # voice_fr includes the header and the subheader of the voice frame 
        self.voice_fr = tk.Frame(master)
        self.voice_fr.grid(row=4 , column=0 , pady =(0,10))
        
        # Declaration of the widgets placed on the voice frame and packing of the elements
        # voice_head_lbl has the header of the voice frame
        # voice_sub_head_lbl displays a subheader message 
        # start_conversation_bt opens a dialog and allows user speak to the robot and give commands
        # stop_conversation_bt stops the dialog and the interaction betwwen the robot and the user
        self.voice_header_lb = tk.Label(self.voice_fr, text="Voice Commands", fg = "#0066FF" ,font=("AnuDaw", 14))
        self.voice_sub_header_lb = tk.Label( self.voice_fr, text="'' Start a conversation with the robot and make Nao move through voice commands ''", font=("Arial", 10 ,"italic"))
        self.start_conversation_bt = tk.Button( self.voice_fr, text="Start conversation", width=10, height=2,relief='raised',wraplength=90,  bd=5 ,command = self.start_thread)
        self.stop_conversation_bt= tk.Button(self.voice_fr, text="Stop conversation", width=10, height=2,relief='raised',wraplength=90,  bd=5 ,command=self.stop_thread)
        
        self.voice_header_lb.grid(row=0 ,column=0 , columnspan=2)
        self.voice_sub_header_lb.grid(row=1 ,column=0 , columnspan=2 ,pady=(0,20) ,padx=(20,0))
        self.start_conversation_bt.grid(row=2, column=0 , pady=(0,20))
        self.stop_conversation_bt.grid(row=2, column=1 , pady=(0,20) )
        
  
        
#Var    # Declaration of the instance variables used within the class
        # ip is the ip address of the robot 
        # robot_position check the position of the robot e.g Sitting or Standing 
        # command_origin is responsible to check if a coomands come from the keyboard or it is a voice command
        # speech_counter checks for how many times the connection betwwen the robot and the app opens each time
        # user_absence counts how many times user hasn't responded in one round of communication 
        self.ip = tk.StringVar()
        self.robot_position = tk.StringVar()
        self.command_origin = tk.IntVar()
        self.speech_counter = tk.BooleanVar()
        self.user_absence = tk.IntVar()
        self.user_absence = 0
        self.movements_log_list = []
        

        # A predefined list of expressions that will be used mainly to announce to user voice
        # messages when the robot cannot move to specfic positions
        self.expressions = ["I am afraid that I have to stand up first", 
               "Sorry but I can't move from this position.I have to stand up first" ,
               "I can't move in the direction you want if I don't get up first"]
  
    
        # Declaration of a list called vocabulary which will contain all the words that the robot can recognize when listens the user speak to its microphone.                
        # speechrec is the event that adds the vocabulary to memory and later can be retrieved from there and used for the needs of the robot
        self.words_list = ["stand up" ,"sit down" ,"move left" ,"move right" , "turn left" , "crouch","turn right" , "move back", " move forward" , "relax"]

       
        # The method connection is called to check if the robot is connectd to the network or not and procceed to the relevant actions 
        self.connection()  
        #self.update_battery()
       
        
    # Reads the file ip_and_name and puts in a temporay list the first line of the txt which is the ip address of the robot
    # Then according this value of the first line two conditions are checked. 
    # If the value equals to Discconeccted then a message is thrown and warns the user which action has to follow.
    # If the value is a proper IP address then imports naoqi library,creates all the modules that will be used from the robot   
    # and changes the values of some variables.
    def connection(self):

         filein = open("ip_and_name.txt", "r")
         temporary_list = filein.readlines()
         temporary_list = [lines.rstrip() for lines in temporary_list] 
         self.ip.set(temporary_list[0])
         
         #The file that has been opened for reading closes here             
         filein.close() 
         
         try:
            # Import naoqi library and creates all the relevant modules that will be used within the class
            from naoqi import ALProxy 
            self.memory = ALProxy("ALMemory", self.ip.get() , 9559)
            self.memory.ping()
            self.tts = ALProxy("ALTextToSpeech", self.ip.get() , 9559)
            self.motion = ALProxy("ALMotion", self.ip.get() , 9559)
            self.posture = ALProxy("ALRobotPosture", self.ip.get(), 9559)
            self.speechrec = ALProxy("ALSpeechRecognition", self.ip.get() , 9559)
            self.battery = ALProxy("ALBattery", self.ip.get() , 9559)


            # Sets the position of the robot variable according the value is returned from the getpostureFamily method
            # Enables both arms of the robot
            # Initializes the command origin variable by setting the value to 0 
            self.robot_position.set(self.posture.getPostureFamily())
            self.arms_status = self.motion.getWalkArmsEnabled()
            self.command_origin.set(0)  
            
            # Set the stifness of all the joints of the robot to 1.0
            # imports the words declared at the beginning of the class into the momory's vocabulary of the robot  
            self.motion.setStiffnesses("Body", 1.0) 
    
    
         except BaseException:
             
             self.turn_left_bt.config(state="disabled")
             self.turn_right_bt.config(state="disabled")
             self.move_left_bt.config(state="disabled")
             self.move_right_bt.config(state="disabled")
             self.move_back_bt.config(state = "disabled")
             self.move_forward_bt.config(state = "disabled")
             self.sit_down_bt.config(state="disabled")
             self.stand_up_bt.config(state="disabled")
             self.crouch_bt.config(state="disabled")
             self.stop_conversation_bt.config(state="disabled")
             self.start_conversation_bt.config(state="disabled")
             
             tkMessageBox.showwarning("Error - Nao is Disconnected", "       You haven't\n     connected NAO.\n\n"
             "1) Go to 'How to connect Nao' on the main panel to see a guide about how NAO has to be connected")
             
             return    
         
        
        

    # Checks initially the position of the robot and then acts according to conditions. 
    # if robot is sitting down a voice message from the robot informs the user that he is going to stand up straight away.
    # Simultaneously sets robot_position variable to "Standing".This is a common variable for all move methods that is used to 
    # help recognize every time the position of the robot.Otherwise if robot is standing up a voice message informs the user that
    # nothing will happen as it is in the desirable position.   
    def stand_up(self):
        if(self.robot_position.get()) == "Standing":
            self.tts.say("I am already standing up ")
        else:
            self.tts.say("I will stand up right now")
            self.posture.goToPosture("Stand", 0.8)
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Stand up (Keyboard Command)") )  
            else:
                pass
            self.robot_position.set("Standing")
    
    
                    
    # Checks initially the position of the robot and then acts according to the conditions. 
    # if robot is sitting down a voice message from the robot informs the user that already is in the desirable position.
    # Otherwise robot stands up and anounces that he is procceding to this action.Simultaneously sets robot_position variable 
    # to "Sitting".This is a common variable for all move methods  which is used to help recognize every time the position of the robot 
    # Also a check is done depending if the command comes from the voice or from the keyboard.
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard                 
    def sit_down(self):
        if(self.robot_position.get()) == "Sitting":
            self.tts.say("I am already sitting down")
        else:
            self.posture.goToPosture("Sit", 0.8)
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Sit down (Keyboard Command)") )  
            else:
                pass            
            self.tts.say("I sat down")      
            self.robot_position.set("Sitting")
    
    
    
    # Initially the robot moves to the crouch position and then sets the robot position variable to 1
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard 
    def crouch(self):
            self.posture.goToPosture("Crouch", 1.0)
            self.robot_position.set("Crouch")
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Crouch (Keyboard Command)") )
            else:
                 pass
            self.tts.say("This is my crouch position")  
            
     
     
     
    # Checks initially the position of the robot and then acts according to the conditions. 
    # if robot is sitting down a voice message from the robot informs the user that already is in that position. and is not gonna move.
    # Otherwise robot lay back and anounces that proceeds to this action.Simultaneously sets robot_position variable 
    # to "Sitting".This is a common variable for all move methods  which is used to help recognize every time the position of the robot 
    # Also a check is done depending if the command comes from voice or from keyboard.
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard        
    def relax(self):
        if(self.robot_position.get()) == "Sitting":
            pass
        else:
            self.posture.goToPosture("SitRelax", 0.8)
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Relax (Keyboard Command)") )  
            else:
                 pass             
            self.tts.say("I am chilling now")      
            self.robot_position.set("Sitting")     
    
    
    
            
    # Checks initially the position of the robot and then acts according to some conditions. 
    # if robot is sitting down a random voice message from a predefined list of expressions (declared at the top) informs the 
    # the user that the robot has to stand up first if needs to move in some direction.If robot though is on an upright position
    # moves forward to the x axis.Also for the forward movement the arms of the robot are enabled and moved accordingly. 
    # Also a check is done depending if the command comes from voice or from keyboard.
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard 
    def move_forward(self):
        
        #sets the arms of the robot true to enable them during  forward movement
        self.leftArmEnable  = True
        self.rightArmEnable  = True
        
        if(self.robot_position.get()) == "Sitting":
             self.tts.say(random.choice(self.expressions))
        else:
             self.motion.moveTo(0.2, 0, 0)
             self.motion.setWalkArmsEnabled(self.leftArmEnable, self.rightArmEnable)
             if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Move forward (Keyboard Command)") )
             else:
                 pass
             #print ('LeftArmEnabled: ',  self.arms_status[0])
             #print ('LeftArmEnabled: ',  self.arms_status[1])

    
    
    
    # Checks  the position of the robot and  acts accordingly. 
    # if robot is sitting down a random voice message from a predefined list of expressions (declared at the top) informs the 
    # the user that the robot has to stand up first if needs to move backwards.If robot though is on an upright position
    # moves back according the x axis.Also for the forward movement the arms of the robot are enables and moved accordingly. 
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard 
    def move_back(self):
        if(self.robot_position.get()) == "Sitting":
            self.tts.say(random.choice(self.expressions))
        else:
            self.motion.moveTo(-0.1 , 0, 0)
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Move back (Keyboard  Command)") ) 
            else:
                pass
            

    # Checks the position of the robot and if the robot is sitting down a random voice message from a predefined list of expressions 
    # (declared at the top) informs the the user that the robot has to stand up first if needs to move in any direction.If robot
    # though is on an upright position moves right regarding the y axis.
    # Also head function is called which allows the robot to move its  head and look at the direction is going to move . 
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard             
    def move_left(self):
        if(self.robot_position.get()) == "Sitting":
            self.tts.say(random.choice(self.expressions) )
        else:
            self.head(0.8 , 0.5 , 0)
            self.motion.post.moveTo(0 , 0.1, 0)
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Move left (Keyboard Command)") )
            else:
                pass
            



    # Checks the position of the robot and if robot is sitting down a random voice message from a predefined list of expressions 
    # (declared at the top) informs the the user that the robot has to stand up first if needs to move in any direction.If robot
    # though is on an upright position moves right regarding the y axis.
    # Also head function is called and allows the robot to look at the direction is going to move .  
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard    
    def move_right(self):
        if(self.robot_position.get()) == "Sitting":
            self.tts.say(random.choice(self.expressions))
        else:
            self.motion.post.moveTo(0 , -0.1, -0.1)
            self.head(-0.8 , 0.5 , 0)
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Move right(Keyboard Command)") )  
            else:
                pass
        
    
    
    # Checks the position of the robot and if robot is sitting down a random voice message from a predefined list of expressions 
    # (declared at the top) informs the the user that the robot has to stand up first if needs to turn right.If robot
    # though is on an upright position turns its body on the right regarding the theta axis.The movement equals to pi/2.
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard 
    def turn_right(self):
        if(self.robot_position.get()) == "Sitting":
            self.tts.say(random.choice(self.expressions))
        else:
            self.motion.moveTo(0 , 0 , -1.5709)
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Turn right (Keyboard Command)") ) 
            else:
                pass
    
    
    
    # Checks the position of the robot and if robot is sitting down a random voice message from a predefined list of expressions 
    # (declared at the top) informs the the user that the robot has to stand up first if the case is to turn left.If the robot
    # though is standind up,turns its body on the left regarding the theta axis.The movement equals to pi/2.
    # if the command has been given by voice inserts a relevant text to the list on the right otherwise sets a text saying that the command comes from the keyboard 
    def turn_left(self):
        if(self.robot_position.get()) == "Sitting":
            self.tts.say(random.choice(self.expressions))
        else:
            self.motion.moveTo(0 , 0 , 1.5709)
            if (self.command_origin.get()) == 0:
                self.log_list.insert('end' ,("Turn left (Keyboard Command)") )  
            else:
                pass

    
    # When is called opens a dialog window between the user and the robot that lasts 3 seconds.During that time the robot listens 
    # the words that the user says ,retrieves from memory the list of the predefined words given at the beggining and 
    # with the help of the getMostConfWord method acts in a different way every time depending on the word has been received.
    # At the beggining of the dialog robot speaks to the user and informs him that is ready to accept any words want to provide.
    def start_vocabulary(self):
              
        self.speechrec.setVocabulary(self.words_list , True) 
   
        if (self.speech_counter)  == True :
            
            self.tts.say("Hello my friend.Simply tell me in which direction you want me to move"
        "and I will do it. You can choose any of the movements displayed on the pc screen.In case you want me to stop "
        "just tell me the word relax. Please speak clear and loud now")
        
        else:
             pass
        
        
        # A loop opens a connection with the robot initially ,then gets the word that the user says and proceeds to the relevant action.  
        while self.speech_counter == True :
            self.speechrec.subscribe("tts")
            print("subscribed")
            time.sleep(4)
            list = self.memory.getData("WordRecognized")
            self.getMostConfWord(list, 0.25)
            self.speechrec.unsubscribe("tts")
            print("unsubscribed")  
        else: 
            self.tts.say("You have selected to exit the conversation.")
            self.tts.say("To be honest with you,I have started feeling a bit tired with all these movements.Bye Bye")
            pass
        
        return 
    
    

    # Selects the word with the highest level of confidentiality from a list of predefined
    # words (that has been set at initialization) when users speaks to the robot.
    def getMostConfWord(self,recogList, threshold):
        
        # Declaration of local variables used within the method
        i = 0
        wordMax = ""
        confMax = 0
        
        # A while loop checks that as long as the length of the list is bigger than 0
        # then the first element will be the word and the next the confidence level of that word.
        # There is a  step +2 every time to identify the next pair of word and confidence level.
        while i < len(recogList):
            word = recogList[i]      
            conf = recogList[i+1]
            i+=2
            print("%1.2f   %s" % (conf, word))
            # if the confidence level of the word is larger that the max level
            # and at the same time larger that a given value then returns that word.
            # Check_word is called at the end to attach an action to the word has been returned.
            if conf > confMax and conf > threshold:
                confMax = conf
                wordMax = word
                print(wordMax)
                self.check_word(wordMax)   
                self.user_absence = 0   
                print (self.user_absence)        
                return wordMax      
            # If the above condition isn't met then a counter holds for how many times this happens.
            # if there is no response after two times then the channel closes down
            # Each time the robot doesn't receive a word throws back amessage to the user so to repeat what he said
            # After the pass of two times then another message informs the user that the channel is closing down.                      
            else :
                if (self.user_absence) == 2 : 
                    self.speech_counter = False
                    self.head(0.8 , 0, 0)
                    self.head(-0.8 , 0 , 0)
                    time.sleep(3)
                    self.tts.say("I think you aren't any longer around.I presume it is about time to go and have some rest then.")  
                    self.user_absence = 0 
               
                elif((self.user_absence) == 1):
                    self.tts.say("I can't hear anything my friend or you haven't chosen one of the proper options.The options are the expressions, move forward, move back, move right , move left , turn right , stand up , sit down , turn right , turn left and crouch.So what about now? ")
                    self.user_absence += 1 
                    print(self.user_absence) 
                    
                elif((self.user_absence) == 0):
                    self.tts.say("I didn't hear what you said.Can you please repeat maybe a bit louder?")
                    self.user_absence += 1 
                    print(self.user_absence) 
                         
                return
                
         
        
    # Depending the word identified provides an action to the robot and sets the values of the command_origin variable accordingly
    def check_word(self , word):
        
        if (word) == "stand up":
            self.movements_log_list.append("Stand up (Voice Command)")
            self.command_origin.set(1)
            self.stand_up()
            self.command_origin.set(0)
            self.tts.say("In which direction you would prefer me to go?")
        
        elif (word) == "sit down":
            self.movements_log_list.append("Sit down (Voice Command)")
            self.command_origin.set(1)
            self.sit_down() 
            self.command_origin.set(0)
            self.tts.say("So what about now?")
        
        elif (word) == "move left":
            self.movements_log_list.append("Move left (Voice Command)")
            self.command_origin.set(1)
            self.move_left() 
            self.command_origin.set(0)
            time.sleep(4)
            self.tts.say("So what do you want to be the next move?")
        
        elif (word) == "move right":
            self.movements_log_list.append("Move right (Voice Command)")
            self.command_origin.set(1)
            self.move_right() 
            self.command_origin.set(0)
            time.sleep(4)
            self.tts.say("Great.What are we doing now?")
        
        elif (word) == "move back":
            self.movements_log_list.append("Move back (Voice Command)")
            self.command_origin.set(1)
            self.move_back() 
            self.command_origin.set(0)
            self.tts.say("I just want to remind you in case you want me to stop just tell me to relax.So what about next now?")
        
        elif (word) == "move forward":
            self.movements_log_list.append("Move forward (Voice Command)")
            self.command_origin.set(1)
            self.move_forward() 
            self.command_origin.set(0)
            self.tts.say("So what do you want me to do next?")
        
        elif (word) == "turn left":
            self.movements_log_list.append("Turn left(Voice Command)")
            self.command_origin.set(1)
            self.turn_left()
            self.command_origin.set(0) 
            self.tts.say("Alright.I just want to remind you in case you want me to stop just tell me to relax.So which would be your choice now?")
       
        #elif(word) == "stop":
            #self.command_origin.set(1)
            #speechrec.unsubscribe("tts")  
            #self.command_origin.set(0)
            #self.tts.say("So what about next?")
        
        elif (word) == "turn right":
            self.movements_log_list.append("Turn right(Voice Command)")
            self.command_origin.set(1)
            self.turn_right()
            self.command_origin.set(0)
            self.tts.say("Ok.That was a right turn,So what about now?")
       
        elif (word) == "crouch":
            self.movements_log_list.append("Crouch (Voice Command)")
            self.command_origin.set(1)
            self.crouch()  
            self.command_origin.set(0)
            self.tts.say("What are we doing now?")
       
        elif (word) == "relax":   
            self.movements_log_list.append("Relax(Voice Command)") 
            self.speech_counter = False
            self.command_origin.set(1)
            self.relax()     
            self.motion.setStiffnesses("Body", 0.0) 
            self.command_origin.set(0)
            return       
  
      
            
    # Is responsible for the head movement.Takes 3 arguments which each one define the angles
    # that will be given to each movement of the head.The head moves on the side(right and left)
    # and also up and down.Regarding the values of the angles the heads moves that way.       
    def head(self , angle1 ,angle2 ,angle3):
        name  = "HeadYaw"
        name1 = "HeadPitch"
        times  = 2.0
        isAbsolute = True
        self.motion.post.angleInterpolation(name, angle1, times, isAbsolute)
        self.motion.post.angleInterpolation(name1, angle2, times, isAbsolute)
        self.motion.post.angleInterpolation(name, angle3, times, isAbsolute)
        self.motion.post.angleInterpolation(name1, angle3, times, isAbsolute)
        


    def stop_running_thread(self):
        
            self.speech_counter = False                  
            #self.tts.stopAll()
            
            
    def start_thread(self):

             self.speech_counter  = True
             self.w = threading.Thread(target=self.start_vocabulary)
             self.w.start()   
  
             self.buttons_state()
             
         
    def stop_thread(self): 
       
             self.s = threading.Thread(target=self.stop_running_thread)
             self.s.start()
                  
             self.buttons_state()  
             self.input_movements_on_list()     
             
    
    def buttons_state(self):
        
        if (self.speech_counter)  == True: 
            
             self.move_forward_bt.config(state="disabled")
             self.move_back_bt.config(state="disabled")
             self.move_right_bt.config(state="disabled")
             self.move_left_bt.config(state="disabled")
             self.stand_up_bt.config(state="disabled")
             self.sit_down_bt.config(state="disabled")
             self.crouch_bt.config(state="disabled")
             self.turn_right_bt.config(state="disabled")
             self.turn_left_bt.config(state="disabled")
             
        
        elif(self.speech_counter)  == False:  
            
             self.move_forward_bt.config(state="normal")  
             self.move_back_bt.config(state="normal")  
             self.move_right_bt.config(state="normal")  
             self.move_left_bt.config(state="normal")  
             self.stand_up_bt.config(state="normal")  
             self.sit_down_bt.config(state="normal")  
             self.crouch_bt.config(state="normal")  
             self.turn_right_bt.config(state="normal")  
             self.turn_left_bt.config(state="normal") 
         
         
    def input_movements_on_list(self):
        
        for s in self.movements_log_list:
            self.log_list.insert('end' , s)
        
        
        del self.movements_log_list [:]
        
      
    #def update_battery(self):
         
         #try:            
             
             #self.memory.ping()
             
             #if  "0 %" <= str(self.battery.getBatteryCharge()) <= "20 %":      
                #self.tts.say("My battery level is low")  
                #threading.Timer(10.0, self.update_battery).start()   
             #else:
                #pass
         #except RuntimeError:
             
              #pass
              
          
      
##title and position of the window on the screen
#motion_window = tk.Tk()
#motion_window.title('Motion Control')

#new_window = Window() 
#new_window.center_window(motion_window,800,660)


#app = Motion(motion_window)

#motion_window.mainloop()
