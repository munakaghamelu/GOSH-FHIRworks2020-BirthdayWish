import requests
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *

class BirthdayWish(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Birthday Wish")

        img = Image.open('C:/Users/mgodw/Documents/GOSH-FHRworks2020-BirthdayWish/BirthdayWish/logo.png')
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        Style().configure("BW.TLabel", fg="black", bg="white", width=20, font='serif 10')

        self.columnconfigure(0, pad=2)
        self.columnconfigure(1, pad=2)
        self.columnconfigure(2, pad=2)

        self.rowconfigure(0, pad=2)
        self.rowconfigure(1, pad=2)
        self.rowconfigure(2, pad=2)
        self.rowconfigure(3, pad=2)
        self.rowconfigure(4, pad=2)

        self.rowconfigure(5, pad=2)
        self.rowconfigure(6, pad=2)
        self.rowconfigure(7, pad=2)
        self.rowconfigure(8, pad=2)

        Label(self, text="", style="BW.TLabel").grid(row=5, columnspan=5)
        Label(self, text="Click to call someone!", style="BW.TLabel").grid(row=6, columnspan=5)
        Label(self, text="", style="BW.TLabel").grid(row=7, columnspan=5)
        Label(self, text="", style="BW.TLabel").grid(row=8, columnspan=5)

        self.rowconfigure(9, pad=2)
        self.rowconfigure(10, pad=2)
        self.rowconfigure(11, pad=2)
        self.rowconfigure(12, pad=2)
        self.rowconfigure(13, pad=2)

        panel = Label(self, text="Please select a month")
        panel.grid(row=0, column=1)

        janBtn = Button(self, text="JAN", command=lambda: self.button_click(1))
        janBtn.grid(row=1, column=0)

        febBtn = Button(self, text="FEB", command=lambda: self.button_click(2))
        febBtn.grid(row=1, column=1)

        marBtn = Button(self, text="MAR", command=lambda: self.button_click(3))
        marBtn.grid(row=1, column=2)

        aprBtn = Button(self, text="APR", command=lambda: self.button_click(4))
        aprBtn.grid(row=2, column=0)

        mayBtn = Button(self, text="MAY", command=lambda: self.button_click(5))
        mayBtn.grid(row=2, column=1)

        junBtn = Button(self, text="JUN", command=lambda: self.button_click(6))
        junBtn.grid(row=2, column=2)

        julyBtn = Button(self, text="JUL", command=lambda: self.button_click(7))
        julyBtn.grid(row=3, column=0)

        augBtn = Button(self, text="AUG", command=lambda: self.button_click(8))
        augBtn.grid(row=3, column=1)

        sepBtn = Button(self, text="SEP", command=lambda: self.button_click(9))
        sepBtn.grid(row=3, column=2)

        octBtn = Button(self, text="OCT", command=lambda: self.button_click(10))
        octBtn.grid(row=4, column=0)

        novBtn = Button(self, text="NOV", command=lambda: self.button_click(11))
        novBtn.grid(row=4, column=1)

        decBtn = Button(self, text="DEC", command=lambda: self.button_click(12))
        decBtn.grid(row=4, column=2)

        self.pack()

    def button_click(self, number):
        data = requests.get('http://127.0.0.1:5002/p/muna/').json()

        i = 9
        while i < 14:
            Button(self, text="Call").grid(row=i, column=2)
            i += 1

        if number == 1:
            txt = data["january"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 2:
            txt = data["february"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 3:
            txt = data["march"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 4:
            txt = data["april"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 5:
            txt = data["may"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 6:
            txt = data["june"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 7:
            txt = data["july"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 8:
            txt = data["august"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 9:
            txt = data["september"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 10:
            txt = data["october"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 11:
            txt = data["november"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        elif number == 12:
            txt = data["december"].split(',')
            Label(self, text=txt[0], style="BW.TLabel").grid(row=9, columnspan=2)
            Label(self, text=txt[1], style="BW.TLabel").grid(row=10, columnspan=2)
            Label(self, text=txt[2], style="BW.TLabel").grid(row=11, columnspan=2)
            Label(self, text=txt[3], style="BW.TLabel").grid(row=12, columnspan=2)
            Label(self, text=txt[4], style="BW.TLabel").grid(row=13, columnspan=2)
        return

def main():
    root = Tk()
    root.geometry('300x500')
    root.resizable(False, False)
    app = BirthdayWish()
    root.mainloop()

if __name__ == '__main__':
    main()

# print(data["january"])
