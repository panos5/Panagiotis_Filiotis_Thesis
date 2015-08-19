__author__ = 'Panagiotis Filiotis'


###importing libraries python 2.7
import Tkinter as tk
import tkMessageBox
import PIL
from PIL import Image, ImageTk
from window_size import Window
import webbrowser
import threading

import os
import sys
import time
import math
import webbrowser


class Lab_Info():
   
    def __init__(self , master):
        
         # Initialization of the widgets of the Lab_Info window
         self.master = master
         self.master.title('Robotics Lab')
         
#Var    # Declaration of the instance variables 
        # ip is the ip address of the robot
        # speech_counter is a counter variable used for counting on a while loop within the class 
        # Vocbulary holds the words that will be placed in the memory module of the robot        
         self.ip = tk.StringVar()    
         self.speech_counter = tk.BooleanVar()
         self.speech_counter = True
         self.user_absence = tk.IntVar()
         self.user_absence = 0 
         self.robot_name = tk.StringVar()         
          
         self.vocabulary = ["Robots" , "Research" ,"Course" ,"News", "Group", "Publications" ,"Menu", "stop"]
         
          
         # Declaration of instance variables that hold url addresses
         self.news_url = "http://www.macs.hw.ac.uk/RoboticsLab/news"
         self.group_url = "http://www.macs.hw.ac.uk/RoboticsLab/about-us"
         self.research_url = "http://www.macs.hw.ac.uk/RoboticsLab/research"
         self.publications_url = "http://www.macs.hw.ac.uk/RoboticsLab/publications"
         self.robots_url = "http://www.macs.hw.ac.uk/RoboticsLab/robots"
         self.services_url = "http://www.macs.hw.ac.uk/RoboticsLab/study/courses"
         
 
         
#Header  # Declaration of all the frames used and packing on the master window  
         # header_fr frame holds the header title of the window
         # sub_header_fr frame holds the sub-header of the window
         # links_fr frame that holds the buttons on the bottom of the page related to the links guide to the robotics lab website
         self.header_fr = tk.Frame(master)
         self.header_fr.grid(row=0 , column =0 , columnspan = 5 ,pady=(10,30))

         self.sub_header_fr = tk.Frame(master)
         self.sub_header_fr.grid(row=1 ,column =0 ,padx=10)

         self.links_fr = tk.Frame(master)
         self.links_fr.grid(row=2 , column =0 , padx=100 )
         
   
         # Declaration of the elements placed on the window and packing
         # window_lbl       label that displays a title of the window
         # sub_header_lbl   label that displays a sub -title on the main window
         # speak_bt         button that allows user speak to the robot and give it commands             
         self.window_lbl = tk.Label(self.header_fr, text='Robotics Lab Information', fg="#663399",font=("AnuDaw", 14))
         self.window_lbl.grid(row=0 , column = 0, columnspan=2)

         self.sub_header_lbl = tk.Label(self.header_fr, text="'' Click on a link to get further information for the Robotics Lab online\n or press Induction to the lab so the robot will give you any information you ask for about the lab ''",
         font=("Arial", 9 ,"italic"))
         self.sub_header_lbl.grid(row=1 , column = 0 , columnspan=2 , pady =(10,40))
             
         self.speak_bt= tk.Button(self.header_fr, text=' Induction to the lab by NAO', wraplength =125 , width=15, height=2, relief ="raise"  , bd=5  ,fg = "black", bg = "#66FF99" , command = self.run_thread)
         self.speak_bt.grid(row=2 , column = 0 , pady =(0,30))
    
         self.stop_bt= tk.Button(self.header_fr, text=' Stop Induction to the lab', wraplength =125 , width=15, height=2, relief ="raise"  , bd=5  ,fg = "black", bg = "red" , command = self.stop_thread)
         self.stop_bt.grid(row=2 , column = 1 , pady=(0,30))

#Links   # Declaration of the elements placed on the links frame and packing    
         # links_lbl        label that displays a title for the links section
         # news_bt          button that opens the url related to the news of the lab    
         # research_bt      button that opens the url related to the research prohectsof the lab    
         # our_group_bt     button that opens the url related to the froups of the lab    
         # publications_bt  button that opens the url related to the publications of the lab    
         # robots_bt        button that opens the url related to the robots of the lab    
         # services_bt      button that opens the url related to the services provided from the lab
         self.links_lbl = tk.Label(self.links_fr, text = "Website's Links" , font=("AnuDaw", 13 ) , fg = "#9966FF")
         self.news_bt = tk.Button(self.links_fr, text="News", width=7, height=2, wraplength=20,relief='raised', bd=3 , command = lambda : self.open_url(self.news_url) )
         self.research_bt = tk.Button(self.links_fr, text="Research", width=7, height=2, wraplength=40 ,relief='raised', bd=3 ,  command = lambda : self.open_url(self.research_url))
         self.our_group_bt = tk.Button(self.links_fr, text="The Group", width=7, height=2, wraplength=40,relief='raised', bd=3 , command = lambda : self.open_url(self.group_url) )
         self.publications_bt = tk.Button(self.links_fr, text="Publications", width=7, height=2, wraplength=60 ,relief='raised', bd=3 , command = lambda : self.open_url(self.publications_url) )
         self.robots_bt = tk.Button(self.links_fr, text="Robots", width=7, height=2, wraplength=40 ,relief='raised', bd=3 , command = lambda : self.open_url(self.robots_url) )
         self.services_bt = tk.Button(self.links_fr, text="The Course", width=7, height=2, wraplength=40 ,relief='raised', bd=3, command = lambda : self.open_url(self.services_url) )
      
                   
         self.links_lbl.grid(row = 1 ,column = 0 ,columnspan = 3)    
         self.news_bt.grid(row = 2 ,column = 0 ,padx = (0,30) ,pady = 20)
         self.research_bt.grid(row = 2 ,column = 1 ,padx=(0,30))
         self.our_group_bt.grid(row = 2 ,column = 2)
         self.publications_bt.grid(row = 3 ,column = 0 ,padx = (0,30) )
         self.robots_bt.grid(row = 3 ,column = 1 ,padx=(0,30))
         self.services_bt.grid(row = 3 ,column = 2 )

         
         self.connection()
         
    # Reads the file ip_and_name and puts in a temporay list the first line of the text which is the ip address of the robot
    # Then according this value of the first line two conditions are checked. 
    # If the value equals to Discconeccted then a message is thrown and warns the user which action has to follow.
    # If the value is a proper IP address then imports naoqi library,creates all the modules that will be used from the robot   
    # and changes the values of some variables.
    def connection(self):
         
        filein = open("ip_and_name.txt", "r")
        temporary_list = filein.readlines()
        temporary_list = [lines.rstrip() for lines in temporary_list] 
        self.ip.set(temporary_list[0])
        self.robot_name.set(temporary_list[1])
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
            #self.stop_bt.config(state = "disabled")
      
 
        except BaseException:
            
             self.ip.set("Disconnected")  
             self.speak_bt.config(state = "disabled")
             self.stop_bt.config(state = "disabled")
             tkMessageBox.showwarning("Error - Nao is Disconnected", "       You haven't\n     connected NAO.\n\n"
             "1) Go to 'How to connect Nao' on the main panel to see a guide about how NAO has to be connected")
             return    
                

    # Opens a url address everytime is called         
    def open_url(self,url):
         webbrowser.open(url)



    # When is called opens a dialog window between the user and the robot that lasts 3 seconds.During that time the robot listens 
    # the words that the user says ,retrieves from memory the list of the predefined words given at the beginning and 
    # with the help of the getMostConfWord method acts in a different way every time depending on the word has been received.
    # At the beggining of the dialog robot speaks to the user and informs him that is ready to accept any words want to provide.         
    def start_vocabulary(self):
       
        
        # Imports the words declared at the beginning of the class into the momory's vocabulary of the robot
        self.speechrec.setVocabulary(self.vocabulary , True)  
  
        if (self.posture.getPostureFamily() == "Sitting"): 
             self.posture.goToPosture("Stand", 0.8)   
        else:
             pass
             

        if (self.speech_counter)  == True :
             self.tts.say("Hello everyone.My name is"  + self.robot_name.get() )
             self.read_text_info("intro_message.txt")
        else:
             pass

        while self.speech_counter  == True :
            self.speechrec.subscribe("tts")
            print("subscribed")
            time.sleep(4)
            list = self.memory.getData("WordRecognized")
            self.getMostConfWord(list, 0.30)
            self.speechrec.unsubscribe("tts")
            print("unsubscribed")
        else:
            self.tts.say("You have selected to stop the induction to the lab.Thank you very much for your time today.Anytime you want any information about the lab don't hesitate to come back.Bye bye and I will see you next time")
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
                if (self.user_absence) == 2 and (self.speech_counter)  == True:
                    self.speech_counter = False
                    self.head(0.8 , 0, 0)
                    self.head(-0.8 , 0 , 0)
                    time.sleep(3)
                    self.tts.say("I think you have left the room.I presume it is about time to stop this induction if there is no audience around.Bye bye")      
                    self.user_absence = 0 
                    
                elif(self.user_absence) == 1 and (self.speech_counter)  == True:
                    self.tts.say("Are you still with me?I can't hear to choose any of the options I gave you.I fyou want to go back please say the word Menu")
                    self.user_absence += 1 
                    print(self.user_absence) 
                    
                elif(self.user_absence) == 0 and (self.speech_counter)  == True:
                    self.tts.say("Can you please repeat?")
                    self.user_absence += 1 
                    print(self.user_absence) 
                         
                return
        
        

        
    # Depending the word identified provides an action to the robot and sets the values of the command_origin variable accordingly
    def check_word(self , word):
        
        #self.motion.setStiffnesses("Body", 1.0)
        
        if (word) == "Robots":
                
            webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/robots")
            self.tts.say("I have already opened the webpage on the pc screen but I would like to tell you some words for my other friends in the lab.")
            self.read_text_info("robots.txt") 
            self.tts.say("That was all about the robots of the lab.What do you want to know now? Do you want to tell you"
            "about the robots, the news, the publications,the group,the course or just exit the induction?")     
            
            
        #elif(word) == "pleo": 
            #webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/robots/pleo/P1030028.JPG/view")
            #self.tts.say("This is pleo.Pleo is an animatronic pet dinosaur toy manufactured by Innvo Labs. The toy has the appearance and the behavior of a week-old baby Camarasaurus dinosaur."
            #"It was designed by Caleb Chung, the co-creator of the Furby. The species of dinosaur chosen allows for concealing the sensors and motors needed for the animation, since it has a big body "
            #"shape and relatively large head. Each Pleo would learn from its experiences and environment through artificial intelligence and develop an individual personality.")
            #self.tts.say("That was all for Pleo.Do you want to carry on with info for other robots or return to the main Menu")
        
        #elif (word) == "epucks":
            #webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/robots/epuck/e-puck_4.jpg/view")
            #self.tts.say("The e-puck is a small about 7 centimeters differential wheeled mobile robot. It was originally designed for micro-engineering education by Michael Bonani and Francesco Mondada at the ASL laboratory of Prof. Roland Siegwart at Lausanne in Switzerland."
            #"The e-puck is open hardware and its onboard software is open source")
            #self.tts.say("That was the info about epucks.Do you want to carry on with info for other robots or return to the main Menu")           
        
        #elif (word) == "aibo":
            #webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/robots/aibo/P1030142.JPG/view")
            #self.tts.say("AIBO  which means pal or partner in Japanese is an iconic series of robotic pets designed and manufactured by Sony" 
            #"Although most models were dog-like, other inspirations included lion-cubs and space explorer, and only the final ERS-7 version was explicitly a robot dog"
            #"IBOs have been used in many movies, music videos and advertising campaigns as futuristic icons")
            #self.tts.say("That was all for my friend Aibo.Do you want to carry on with info for other robots or return to the main Menu")
        
        #elif (word) == "sarah":
            #webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/robots/sarah/P1030585.jpg/view")
            #self.tts.say("Sarah joined the Heriot-Watt team to undertake a six week experiment, the first of its kind, into how humans would interact with a robot in a working environment. Earlier research shows that while people can find robots useful "
            #"and attractive working companions, they can also trigger annoyance and even violence")
            #self.tts.say("That was all about Sarah.Do you want to carry on with info for other robots or return to the main Menu")
        
        
        elif (word) == "Research": 
            webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/research")  
            self.tts.say("I have already opened the relevant website on the computer")
            self.read_text_info("research.txt")   
            self.tts.say("That was all the relevant inofrmation I could give you about the research projects of the lab.What do you want to know now? Do you want to tell you"
            "about the robots,the news, the publications,the group,the course or just exit the induction?")     


        elif (word) == "Publications":
            webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/publications") 
            self.tts.say("I have opened the relevant website on the computer displaying the past projects as well if you want to have a more detailed look.")
            self.read_text_info("publications.txt")    
            self.tts.say("That was all the relevant inofrmation I could give you about the publications of our lab.What do you want to know now? Do you want to tell you"
            "about the robots ,the news, the research projects, the group, the course or just exit?")  
            
            
        elif (word) == "Group":
            webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/about-us/faculty") 
            self.read_text_info("group.txt")
            self.tts.say("That was the info about the people related to the robotics lab.What do you want to know now? Do you want to tell you"
            "about the robots ,the news, the research projects, the publications, the course or just exit?")  
               
 
        elif (word) == "News":
             webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/news")   
             self.read_text_info("news.txt")
             self.tts.say("That was the news of the robotics lab.With which subject do you want to carry on now?"
            "The robots , the research projects, the publications, the group of the people related to the lab , the course or just exit?")  
       
 
        elif (word) == "Course":
            webbrowser.open("http://www.macs.hw.ac.uk/RoboticsLab/study/courses")
            self.read_text_info("courses.txt")
            self.tts.say("That was the information about the course taught in the University.With which subject do you want to carry on?"
            "The robots , the research projects, the publications, the group of the people related to the lab or the news of the lab?")  
   
     
        elif (word) == "Menu":
            self.tts.say("You have requested return to the Main Menu. Which option would you like to follow now? The words you can choose are research , news, publications, group, robots or course.At any time you want to stop just tell the word exit.")

        elif (word) == "stop":
            self.speech_counter = False 
            return  
            
    
    # Reads the data from a text file and pass the whole text into a temporary value
    #and returns the vlaue to the robot to express it 
    def read_text_info(self , text_file):
        
        #filein = open( text_file , "r")
        filein = open(os.path.join("Robotics_Lab_text_files" , text_file ), 'r')
        temporary_value = filein.read()
        
        self.tts.say(temporary_value)
        
        return temporary_value      
        filein.close()
   
   
    # Is responsible for the head movement.Takes 3 arguments which each one define the angles
    # that will be given to each movement of the head.The head moves on the side(right and left)
    #and also up and down.Regarding the values of the angles the heads moves that way.       
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
        self.tts.stopAll()

   
    def run_thread(self):
        
        self.speech_counter  = True
        self.x = threading.Thread(target=self.start_vocabulary)
        self.x.start()
   
        
    def stop_thread(self): 
         
         self.s = threading.Thread(target=self.stop_running_thread)
         self.s.start()
        
    


###title and position of the window on the screen
#lab_info_window = tk.Tk()
#lab_info_window.title('Interaction')
#app = Lab_Info(lab_info_window)
#new_window = Window() 
#new_window.center_window(lab_info_window,440,400)
#lab_info_window.mainloop()
