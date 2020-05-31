
# ============================================= TEXT TO SPEECH SCRIPT ================================================ #

# -------- English version -------------

__author__ = "red_ant"

# ---------------------- imports -------------------
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from playsound import playsound
from gtts import gTTS
# --------------------------------------------------

# ============================================ Window Settings ======================================================= #
root = Tk()  # window
root.minsize(width=100, height=100)
root.geometry('700x300+300+100')
root.title("Text To Speech")
root.configure(background='cyan')
root.resizable(0, 0)
# ==================================================================================================================== #


# ============================= Inside Window ======================================================================== #

# --------------------------- Frame ------------------------------------------------------------------------ #
Tops = Frame(root, bg='white', bd=5, pady=1, relief=RIDGE)
Tops.pack(side=TOP)
# ----------------------------------------------------------------------------------------------------------- #
# ----------------------------------------- Labels ---------------------------------------------------------- #

lblTitle = Label(Tops, font=('arial', 50, 'bold'), text='Text To Speech',bd=8, bg='cyan', fg='cornsilk', justify=CENTER)
lblTitle.grid(row=0)
# ----------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------- #

# -------------------------------- Frames ------------------------------------------------------------------ #
MenuFrame = Frame(root, bg='cornsilk', bd=2, relief=RIDGE)
MenuFrame.pack()
# ---------------------------------------------------------------------------------------------------------- #
# ---------------------------- Text input ------------------------------------------------------------------ #
text = scrolledtext.ScrolledText(MenuFrame, width=78, height=10)
text.pack()
# ---------------------------------------------------------------------------------------------------------- #

# ------------------------------- Defs --------------------------------------------------------------------- #


def showAbout():
	# Info to show when user click info
	messagebox.showinfo(title='About',
	message='''Text To Speech\n\nAuthor: red_ant\nGithub: https://github.com/02-red-Ant-02\ntelegram: https://t.me/red_a_n_t\n\tThank You !''')


def openFile():
	filedialog.askopenfile()  # open file


def iExit():
	iExit = messagebox.askyesno("Exit Text to speech", "Confirm to quit")
	if iExit > 0:
		root.destroy()
		return

def showHelp():
	messagebox.showwarning(title='Help', message='''
	Type text in white area
	And then click on any language
	related on what you have type in.''')


def license_():
	messagebox.showinfo(title='License', message='''\n\tText To Speech\n\n 
	Software Uses:\n
	  * Text to speech\n\nCopyright 2020\n''')
# -------------------------------- Listen to Audio ------------------------------------------------------- #

# Comming soon

# -------------------------------------------------------------------------------------------------------- #

# ------------ read text in english ----------------------------------------------------------------------- #
def textEn():
	texte = text.get('0.0', END)# Get input text
	tts = gTTS(text=texte, lang='en')
	tts.save("text.mp3")# save text
	playsound("text.mp3")# play sound

# --------------------------------------------------------------------------------------------------------- #
# -------------- read text in FRENCH ---------------------------------------------------------------------- #


def textFr():
	texte = text.get('0.0', END)                                                 # Get input text
	tts = gTTS(text=texte, lang='fr')                
	tts.save("text.mp3")                                                         # save text
	playsound("text.mp3")                                                        # play sound

# -------------- read text in HINDI ---------------------------------------------------------------------- #


def textHindi():
	texte = text.get('0.0', END)  # Get input text
	tts = gTTS(text=texte, lang='hi')
	tts.save("text.mp3")  # save text
	playsound("text.mp3")

# -------------- read text in Espanol ---------------------------------------------------------------------- #


def textSpan():
	texte = text.get('0.0', END)		  # Get input text
	tts = gTTS(text=texte, lang='es')
	tts.save("text.mp3")  										  			    # save text
	playsound("text.mp3")
# --------------------------------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------- Tabs ----------------------------------------------- #


# ---------------------- menubar -------------------------------------------------------------------------- #


root.option_add('*tear0ff', False)
menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu=file, label='File')
menubar.add_cascade(menu=edit, label='Edit')
menubar.add_cascade(menu=help_, label='Help')

# --------------- Inside Help menu -------------------- #
help_.add_command(label="License", command=license_)
help_.add_command(label="About", command=showAbout)
help_.add_command(label='? Help', command=showHelp)
# ----------------------------------------------------- #
# --------------- Inside File menu -------------------- #
file.add_command(label='Open...\t^o', command=openFile)
file.add_separator()
file.add_command(label='Exit   \t^q', command=iExit)
# ----------------------------------------------------- #
# -------------- Inside Edit Menu --------------------- #
edit.add_command(label="Undo\t\t^z", command='')
edit.add_command(label="Redo\tCtrl ^z", command='')
edit.add_separator()
edit.add_command(label="Copy\t\t^c", command='')
edit.add_command(label="Cut\t\t\t^x", command='')
edit.add_command(label="Paste\t\t^v", command='')

# ------------------------------------------------------------------------------------------------------- #

# ------------------------------ BUTTONS ---------------------------------------------------------------- #

btn = ttk.Button(root, text='Play In English ', command=textEn)# Play button in english
btn.pack()
btn.place(x=94, y=255)

btn = ttk.Button(root, text='Play In Hindi  ', command=textHindi)# Play button in Hindi
btn.pack()
btn.place(x=223, y=255)

btn = ttk.Button(root, text='Play In French  ', command=textFr)# Play button in French
btn.pack()
btn.place(x=344, y=255)

btn = ttk.Button(root, text='Play In Spanish  ', command=textSpan)# Play button in Espanol
btn.pack()
btn.place(x=476, y=255)

root.mainloop()
# ============================================ END OF TEXT TO SPEECH SCRIPT ========================================== #
