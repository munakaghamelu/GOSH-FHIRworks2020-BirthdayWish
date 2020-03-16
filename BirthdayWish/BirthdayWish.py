import requests
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *

class BirthdayWish(Frame):


    def __init__(self):
        super().__init__()
        root = Tk()
        root.withdraw()
        self.startPageUI(root)
        root.mainloop()

    def startPageUI(self, root):

        #add logo

        top = Toplevel()
        #top.iconbitmap('C:/Users/mgodw/Documents/GOSH-FHRworks2020-BirthdayWish/BirthdayWish/logo.ico')
        top.geometry('300x500')
        top.resizable(False, False)

        #img = Image.open('C:/Users/mgodw/Documents/GOSH-FHRworks2020-BirthdayWish/BirthdayWish/logo.png')
        #img = img.resize((100, 100), Image.ANTIALIAS)
        #img = ImageTk.PhotoImage(img)

        #display the loading page + click button to reshow the root screen and hide top
        top.configure(bg='white')
        top.columnconfigure(0, pad=10)
        top.columnconfigure(1, pad=10)
        top.columnconfigure(2, pad=10)
        top.rowconfigure(0, pad=10)
        top.rowconfigure(1)
        top.rowconfigure(2)
        top.rowconfigure(3, pad=10)

        canvas = Canvas(top, bg="PaleTurquoise1", width=50, height=200).grid(row=0, column=0)
        canvas2 = Canvas(top, bg="PaleTurquoise1", width=50, height=200).grid(row=0, column=2)
        canvas3 = Canvas(top, bg="plum1", width=50, height=200).grid(row=2, column=0)
        canvas3 = Canvas(top, bg="plum1", width=50, height=200).grid(row=2, column=2)

        #display logo + button to loading application
        logo = ImageTk.PhotoImage(file="logo.png")
        label = Label(top, image=logo)
        label.image = logo
        label.grid(row=0, column=1)

        #label containing the quote, need to change the colour
        Label(top, text="'Empathy is a quality character").grid(row=1, columnspan=3)
        Label(top, text="that can change the world.'").grid(row=2, columnspan=3)

        #add button to main page
        button = Button(top, text="Load Application", command=lambda :[top.withdraw(), self.startMainUI(root, top)]).grid(row=3, columnspan=3)

        #Label(top, text="logo", image=logo).grid(row=1, columnspan=2)
        # img = Image.open('C:/Users/mgodw/Documents/GOSH-FHRworks2020-BirthdayWish/BirthdayWish/logo.png')
        # img = img.resize((100, 100), Image.ANTIALIAS)
        # img = ImageTk.PhotoImage(img)

    def startMainUI(self, root, top):
        mainTop = Toplevel()
        mainTop.configure(bg='white')
        mainTop.master.title("Birthday Wish")
        mainTop.geometry('300x500')
        mainTop.resizable(False, False)

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        Style().configure("BW.TLabel", fg="black", bg="white", width=20, font='serif 10')

        mainTop.columnconfigure(0, pad=2)
        mainTop.columnconfigure(1, pad=2)
        mainTop.columnconfigure(2, pad=2)

        mainTop.rowconfigure(0, pad=2)
        mainTop.rowconfigure(1, pad=2)
        mainTop.rowconfigure(2, pad=2)
        mainTop.rowconfigure(3, pad=2)
        mainTop.rowconfigure(4, pad=2)

        mainTop.rowconfigure(5, pad=2)
        mainTop.rowconfigure(6, pad=2)
        mainTop.rowconfigure(7, pad=2)
        mainTop.rowconfigure(8, pad=2)

        Label(mainTop, text="", style="BW.TLabel").grid(row=5, columnspan=5)
        Label(mainTop, text="Click to call someone!", style="BW.TLabel").grid(row=6, columnspan=5)
        Label(mainTop, text="", style="BW.TLabel").grid(row=7, columnspan=5)
        Label(mainTop, text="", style="BW.TLabel").grid(row=8, columnspan=5)

        mainTop.rowconfigure(9, pad=2)
        mainTop.rowconfigure(10, pad=2)
        mainTop.rowconfigure(11, pad=2)
        mainTop.rowconfigure(12, pad=2)
        mainTop.rowconfigure(13, pad=2)

        mainTop.rowconfigure(14, pad=2)

        panel = Label(mainTop, text="Please select a month")
        panel.grid(row=0, column=1)

        janBtn = Button(mainTop, text="JAN", command=lambda: self.button_click(1, mainTop))
        janBtn.grid(row=1, column=0)

        febBtn = Button(mainTop, text="FEB", command=lambda: self.button_click(2, mainTop))
        febBtn.grid(row=1, column=1)

        marBtn = Button(mainTop, text="MAR", command=lambda: self.button_click(3, mainTop))
        marBtn.grid(row=1, column=2)

        aprBtn = Button(mainTop, text="APR", command=lambda: self.button_click(4, mainTop))
        aprBtn.grid(row=2, column=0)

        mayBtn = Button(mainTop, text="MAY", command=lambda: self.button_click(5, mainTop))
        mayBtn.grid(row=2, column=1)

        junBtn = Button(mainTop, text="JUN", command=lambda: self.button_click(6, mainTop))
        junBtn.grid(row=2, column=2)

        julyBtn = Button(mainTop, text="JUL", command=lambda: self.button_click(7, mainTop))
        julyBtn.grid(row=3, column=0)

        augBtn = Button(mainTop, text="AUG", command=lambda: self.button_click(8, mainTop))
        augBtn.grid(row=3, column=1)

        sepBtn = Button(mainTop, text="SEP", command=lambda: self.button_click(9, mainTop))
        sepBtn.grid(row=3, column=2)

        octBtn = Button(mainTop, text="OCT", command=lambda: self.button_click(10, mainTop))
        octBtn.grid(row=4, column=0)

        novBtn = Button(mainTop, text="NOV", command=lambda: self.button_click(11, mainTop))
        novBtn.grid(row=4, column=1)

        decBtn = Button(mainTop, text="DEC", command=lambda: self.button_click(12, mainTop))
        decBtn.grid(row=4, column=2)

        closeBtn = Button(mainTop, text="Click and Quit", command=lambda: self.quit(root))
        closeBtn.grid(row=14, columnspan=3)

        #add a back button

        self.pack()

    def button_click(self, number, mainTop):
        data = requests.get('http://127.0.0.1:5002/p/birthdayWish_Api/').json()

        i = 9
        while i < 14:
            Button(mainTop, text="Call").grid(row=i, column=2)
            i += 1

        if number == 1:
            txt = data["january"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 2:
            txt = data["february"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 3:
            txt = data["march"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 4:
            txt = data["april"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 5:
            txt = data["may"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 6:
            txt = data["june"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 7:
            txt = data["july"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 8:
            txt = data["august"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 9:
            txt = data["september"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 10:
            txt = data["october"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 11:
            txt = data["november"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 12:
            txt = data["december"].split(',')
            Label(mainTop, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(mainTop, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(mainTop, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(mainTop, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(mainTop, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        return

    def quit(self, root):
        Label(root, text="Click ------^ to Exit", style="BW.TLabel").grid(row=13, columnspan=2)
        root.destroy()

def main():
    #root.geometry('300x500')
    #root.resizable(False, False)
    #add icon
    #root.iconbitmap('C:/Users/mgodw/Documents/GOSH-FHIRworks2020-BirthdayWish/BirthdayWish/logo.ico')
    app = BirthdayWish()

if __name__ == '__main__':
    main()

# print(data["january"])
