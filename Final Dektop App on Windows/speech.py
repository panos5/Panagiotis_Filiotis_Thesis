__author__ = 'Panagiotis Filiotis'


###importing libraries python 2.7
import Tkinter as tk
import tkMessageBox
import PIL
from PIL import Image, ImageTk
from window_size import Window


class Speech():
   
    #Initialization of the widgets of the Speech window
    def __init__(self , master):
        
        self.master = master
        self.master.title('Speech Control')
        
        # Declaration of the instance variables of the class
        # entry_text_val is the value of the entry text 
        # predefined_val is the value of the selected item of the list on the right hand side
        # ip_address the ip of the robot
        self.entry_text_val = tk.StringVar()
        self.entry_text_val.set("Enter your text here.." )
        self.predefined_val = tk.StringVar()
        self.ip_address = tk.StringVar()
        self.connection_status = tk.StringVar()

        # Declaration and positioning of the frames of the Speech window
        # title_fr frame that holds the header and the subheader message of the window
        # left_fr frame that hols the elements on the left side
        # right_fr frame that holds the elements on the right side
        self.title_fr = tk.Frame(master, relief='ridge', height =50 , width=600)
        self.left_fr = tk.Frame(master, relief='groove', bd=6 , height =20,width=250 )
        self.right_fr = tk.Frame(master, relief='groove', bd=6 , height =400,width=250)

        self.title_fr.grid(row=0 ,column=0 , pady=(15 ,0), columnspan = 2)
        self.left_fr.grid(row=1 ,column=0 , padx=(20,20) , pady=(50,50) )
        self.right_fr.grid(row=1 ,column=1 , padx=(10,30) , pady=(0,50) ,ipadx=15)
    

        
#Top    # Top frame elements declared anddifferents attributes assigned
#Frame  # header_lbl is the label holds the text displays on the header of the window
        # sub_header label displays a message info below the header
        self.header_lbl = tk.Label(self.title_fr, text='NAO can speak...', fg= "#009966" ,font=("AnuDaw", 14))
        self.sub_header_lbl = tk.Label(self.title_fr, text="'' Make NAO speak either manually or through predefined phrases '' ", font=("Arial", 10 ,"italic"))

        # Packing of the widgets of top frame
        self.header_lbl.pack()
        self.sub_header_lbl.pack(side='bottom')
        
 
               
#Left   # Declaration of the widgets of the left frame and sorted based on a grid layout 
#Frame  # left_frame_lbl label that displays the text of the header of the left frame
        # entry_txt entry that allows user to enter text that will be provide to the robot in order to speak
        # delete_bt button that everytime is pressed clears everything inside the the entry text     
        self.left_frame_lbl = tk.Label(self.left_fr, text='Manual entry', font=("AnuDaw", 12) ,fg= "#009966")
        self.left__sub_lbl = tk.Label(self.left_fr, text=" '' Enter your text into the text field\n and press button to Speak '' ",font=("Arial", 9 ,"italic"))
        self.entry_txt = tk.Entry(self.left_fr, width=40 , bd=7, textvariable = self.entry_text_val,
                                   font=("Times", 14, "italic"), relief='sunken')
        
        # When mouse's single click used inside the box entrytxt_single_click method is called
        self.entry_txt.bind('<Button-1>' , self.entrytxt_single_click)                                                   

        self.delete_bt = tk.Button(self.left_fr , text= "Clear Text", relief='raised', wraplength=150 ,width=8 , bd=3 ,
                                     command= self.clear_entry_text)
        
       
        self.left_frame_lbl.grid(row=1, column=0, pady=(40, 5), ipadx=40, ipady=5)
        self.left__sub_lbl.grid(row=2, column=0, pady=(0, 10))
        self.entry_txt.grid(row=3, column=0, pady=(10, 15))
        self.delete_bt.grid(row=3, column=1, pady=(10, 15) , padx=(10,10))
        
        
        # Declaration of the buttons frame and the buttons of the buttons frame
        # button_fr frame that holds two buttons (speak and add_phrase)
        # speak_bt  button that gets the text from the entry box and make robot speak 
        # add_phrase_bt button that adds the text from the entry text to the list with the predefined phrases on the right
        self.buttons_fr =tk.Frame(self.left_fr, width=250 , height=250)
        self.buttons_fr.grid(row=4, column=0, pady=(10, 15))
        self.speak_bt = tk.Button(self.buttons_fr,  text="Press button to Speak", relief='raised', wraplength=80,
                                      width=8 , bd=3 , command=self.speak )
        self.add_phrase_bt = tk.Button(self.buttons_fr, text="Add Phrase to your List" ,relief='raised', wraplength=80,
                                      width=8 , bd=3 , command = self.add_phrase )
        self.speak_bt.pack(side='left', padx=(0,20) , ipadx =6 , ipady=5)
        self.add_phrase_bt.pack(side='left', padx=5 , ipadx =6 , ipady=5)

        
#Left   # Declaration of the log frame , the elements that holds and how they are packed
#Bottom # log_fr frame that holds a label ,  a list and a button
#Frame  # log_title_lbl  label that displays a text as header for the log frame 
        # clear_log button that clears the log file history
        self.log_fr =tk.Frame(self.left_fr, width=250 , height=250)
        self.log_fr.grid(row=5, column=0, padx=10, pady=25)
       
        self.log_title_lbl = tk.Label(self.log_fr , text= 'Log  History')
        self.log_title_lbl.pack(side='top', padx=(50,0),pady = (0,10))

        self.scrollbar = tk.Scrollbar(self.log_fr, orient='vertical')
        self.log_list = tk.Listbox(self.log_fr , height = 10, width =35 , yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.log_list.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.log_list.pack(side='bottom' , padx=(50,0))

        self.clear_log_bt = tk.Button(self.left_fr, text="Clear Log History" , wraplength=80 ,
                                      width=6 ,bd=3 , command = self.clear_log_text, )
        self.clear_log_bt.grid(row=6, column=0 , padx=(50,0), ipadx=10 ,pady =(0,10))


#Right  # Declaration of the widgets of the right frame and sorted based on a grid layout 
#Frame  # title_fr frame that holds a label that dispalys the header of the frame
        # right_fr_lbl label  is the header of the right frame
        # subheader_lbl label that displays a message below the header label
        # pre_phrases_list  
        self.title_fr = tk.Frame(self.right_fr)
        self.title_fr.grid(row=0 , column = 0, columnspan=2 , pady=(40, 20))
           
        self.right_frame_lbl = tk.Label(self.title_fr, text='Custom phrases', font=("AnuDaw", 12), fg="#009966")
        self.right_frame_lbl.pack(pady=(0,5) , ipadx=20, ipady=5 )
        
        self.subheader_lbl = tk.Label(self.title_fr, text=" '' Choose a phrase from the list\n and press Nao Speak '' ",font=("Arial", 9 ,"italic"))
        self.subheader_lbl.pack(side= "bottom")
        
        # ListBox widget declaration,attributer assigned and position on the right frame
        self.pre_phrases_list = tk.Listbox(self.right_fr, height = 15, width =32 )
        self.pre_phrases_list.grid(row=2 , column = 0 ,padx=(20,0))
        
        self.pre_phrases_list.bind("<Double-1>" , self.speak_double_click)
       
        
        # Scrollbar for the listbox of the predefined phrases
        self.scrollbar = tk.Scrollbar(self.right_fr ,orient='vertical',command= self.pre_phrases_list.yview) 
        self.scrollbar.grid(row=2 , column = 1 , sticky='n' + 's')
        self.pre_phrases_list.config(yscrollcommand=self.scrollbar.set)
 
 
       
#Bottom # Bottom frame elements with assigned attributes and positioning regarding to grid
#Right  # buttons_fr frame that contains 3 buttons with different functinalities
        # play_bt button that when is pressed make robot speak the selected item of the list
        # delete_bt deletes the selected item from the list
        # save_bt saves the list with the predefined phrases 
        self.buttons_fr = tk.Frame(self.right_fr)
        self.buttons_fr.grid(row=3 , column = 0, columnspan=2)
        self.play_bt = tk.Button(self.buttons_fr, text='Nao Speak', bd=3 ,relief='raised', command = self.speak_from_list)
        self.play_bt.pack(side='left' ,padx =(20,40), pady = 10 )
        self.delete_bt = tk.Button(self.buttons_fr, text='Delete Entry' , bd=3 ,relief='raised' , command = self.delete_item_list)
        self.delete_bt.pack(side='left' , padx=(10,10),pady = 15)
        
        
        

        # Is called at the initialization of the class to load the phrases of the list
        self.load_list()
        self.read_initial_values() 



    # Reads the data from the ip_and_name text file,saves it to a temporary list
    # and then sets the right value on the ip variable declared above
    def read_initial_values(self) :
         
        filein = open("ip_and_name.txt", "r")
        temporary_list = filein.readlines()
        temporary_list = [lines.rstrip() for lines in temporary_list] 
        self.ip_address.set(temporary_list[0])
   
        try:
            
            from naoqi import ALProxy
            # Imports ALMemory module and use pings to check if the connection with the robot is alive 
            self.memory = ALProxy("ALMemory", self.ip_address.get() , 9559)
            self.memory.ping()
            self.tts = ALProxy("ALTextToSpeech", self.ip_address.get() , 9559) 
            self.connection_status.set("online") 
       
        except Exception:
            
            self.speak_bt.config(state="disabled")
            self.play_bt.config(state="disabled")
            tkMessageBox.showwarning("Error - Nao is Disconnected", "                    You haven't connected NAO.\n\n"
             "         Go to 'How to connect Nao' on the main panel\n     to see a guide about how NAO has to be connected")
            self.connection_status.set("offline")
            
        filein.close()
        
      
    # Checks if the entry box is empty first and throws an information message to warn the user that has o provide a proper text into the field
    # if this is the case
    # Otherwise gets the value of the text and pass it to the robot.The robot speaks and the phrase is adde to the log hstory list.
    # The text is cleared after the user presses the speak button
    def speak(self):
        
        if (self.ip_address.get()) == "Disconnected":
            return    
        else:       
            if len(self.entry_text_val.get()) == 0:     
                tkMessageBox.showwarning("Error - Input Field Empty", "Please provide some text into the empty text field")
                self.entry_text_val.set("Enter your text here..." )  
            else:
                text = self.entry_text_val.get()
                self.tts.say(self.entry_text_val.get())
                self.log_list.insert('end' ,(" "  + text) )    
       
    
    # Clears the data from the entry box and checks if it is empty or not to throw a warning message 
    def clear_entry_text(self):
        
         if len(self.entry_txt.get()) == 0:
            tkMessageBox.showwarning("Warning - Input Field Empty", "Text field is already empty")
         else:
            self.entry_txt.delete(0, 'end')
    
            
    # Clears the data from the entry box when user uses single-click inside the entry text.
    def entrytxt_single_click(self , event):
        if (self.entry_text_val.get()) == "Enter your text here.." :
            self.entry_txt.delete(0, 'end')
        else:
            return
    
    
    # A phrase is selected from the list with a double click and robot speaks accordingly
    # Also phrase is inserted in the history log list
    def speak_double_click(self , event):
        
        if (self.connection_status.get()) == "offline":
            return
        else:
            index = self.pre_phrases_list.curselection()[0]
            value = self.pre_phrases_list.get(index)
            self.log_list.insert('end' , value )
            self.tts.say(value)
    
    
    # Clears the data from the history log list and checks if the text area is empty to throw a warning message in that case
    def clear_log_text(self):
            
        if (self.log_list.size()) == 0: 
          tkMessageBox.showwarning("Warning - Log History Empty", "Log History is already empty")
        else: 
            question = tkMessageBox.askyesno("Delete log file", "Are you sure you want to delete log file?")
            if question==True:
                self.log_list.delete(0, 'end')
            else:
                return



    # Adds the text provided from the entry text field to a list on the right hand side of the window which is
    # responsible to hold all the predefined phrases 
    def add_phrase(self):

        # Declaration of a local variable that will be used within the class and is responsible to pass the text
        # from the entry box to the list on the right hand side
        text =  " "  + self.entry_txt.get()

        # Checks if the entry text is empty and throws a warning message
        if len(self.entry_txt.get()) == 0 or (self.entry_txt.get()) == "Enter your text here.." :
          tkMessageBox.showwarning("Warning - Input Field Empty", "Please provide some text into the empty text field")
        else:   
          self.pre_phrases_list.insert('end' , text )
          self.save_list()
          self.entry_txt.delete(0, 'end')
          tkMessageBox.showinfo("Successful entry", "Phrase added successfully in the list. Well done!!! ")
          self.entry_text_val.set("Enter your text here.." )
          
  
  
     
    # Gets the value of the selected item of the list and pass itto the robot to speak
    # The selection is always inserted in the log history list on the left of the window 
    # Also throws an info message to the user if he hasn't selected an item from the list
    def speak_from_list(self):
        
        try:            
            index = self.pre_phrases_list.curselection()[0]
            value = self.pre_phrases_list.get(index)
            self.log_list.insert('end' , value )
            self.tts.say(value)
        except IndexError:
            tkMessageBox.showwarning("Error - No selection", "Please select a phrase from the list")
    
    

    # Deletes the selected index from the list .In case no index is selected an exception is thrown.   
    def delete_item_list(self):
        
        try:
        
         index = self.pre_phrases_list .curselection()[0]
         
         # A pop-up window is thrown and depending the selection of the user the system proceeds to the relevant action
         question = tkMessageBox.askyesno("Delete File", "Are you sure you want to delete the phrase from the list?")
        
         # If the answer is yes deletes the entry otherwise return withoun doing anything
         if question==True:           
            self.pre_phrases_list .delete(index)
            self.save_list()
         else:  
             return 
        
        except IndexError:
            tkMessageBox.showwarning("Item is not selected", "Please select a phrase from the list to delete")



    # Saves the list with the predefined phrases to a teporary list first and then to a text file
    def save_list(self):
   
         ## get a list of listbox lines
         temp_list = list(self.pre_phrases_list.get(0, 'end'))
         ## add a trailing newline char to each line
         temp_list = [lines + '\n' for lines in temp_list]
         fileout = open("phrases_list.txt", "w")
         fileout.writelines(temp_list)
         fileout.close()    


        
    # Loads the data with the predefined phrases from a text file. Initially it stores the file to
    # a temporary list and then insert the data into the predefined phrases list on the right hand side
    def load_list(self):
        # read the data file into a list
        filein = open("phrases_list.txt", "r")
        temp_list = filein.readlines()
        temp_list = [lines.rstrip() for lines in temp_list] 
        
        for lines in temp_list:
          self.pre_phrases_list.insert('end' , lines)
          filein.close()
          
    

###title and position of the window on the screen
#speech_window = tk.Tk()
#speech_window.title('Speech Control')
#app = Speech(speech_window)

#new_window = Window() 
#new_window.center_window(speech_window, 1000,720)
#speech_window.mainloop()
