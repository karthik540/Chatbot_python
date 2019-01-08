from tkinter import *
from main import *

def loadMyMessage(name , Message):
    if Message != '':
        chatWindow.config(state = NORMAL)
        lineNumber = float(chatWindow.index('end'))-1.0
        chatWindow.insert(END , name + ": " + Message)
        chatWindow.tag_add(name, lineNumber, lineNumber+0.5)
        if name == "You":
            chatWindow.tag_config(name, foreground="#FF8000", font=("Arial", 12, "bold"))	
        else:
            chatWindow.tag_config(name, foreground="#36DEE8", font=("Arial", 12, "bold"))
        chatWindow.config(state=DISABLED)
        chatWindow.yview(END)

###		Keyboard Functions		###
def PressAction(action):
	EntryBox.config(state = NORMAL)
	ClickAction()

def DisableEntry(action):
	EntryBox.config(state = DISABLED)

###		Message Loader 		###
def ClickAction():
    # Filtering the Message
    filteredMessage = messageFilter(EntryBox.get("0.0" , END))
    print(filteredMessage)

    # Loading the User Message
    loadMyMessage("You" , filteredMessage)
    EntryBox.delete("0.0" , END)        # Clears the entry message box
    chatWindow.yview(END)               # Moves the Chat window down 
    
    # Loading the Bot Message
    botMessage = botResponseReciever(filteredMessage[:-1])
    loadMyMessage("Deku" , botMessage)
    chatWindow.yview(END)  

###       GUI     ###


# Window Management
root = Tk()
root.title("Deku Bot")
root.geometry("400x500")
root.resizable(height= False , width= False)

# Chat Window
chatWindow = Text(root , bd = 0 , bg = "white" ,height = "8" , width = "50" , font = "Ariel")
#chatWindow.insert(END , "Start your conversation !")
chatWindow.config(state = DISABLED)

# ScrollBar
scrollBar = Scrollbar(root , command = chatWindow.yview)
chatWindow['yscrollcommand'] = scrollBar.set

#Send Button
SendButton = Button(root, font=30, text="Send", width="12", height="5",
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",
                    command = ClickAction)

EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", PressAction)

# Placing all the stuff inplace
scrollBar.place(x=376,y=6, height=386)
chatWindow.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

root.mainloop()