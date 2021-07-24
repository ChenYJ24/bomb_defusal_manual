# define
# red : 0 1
# blue : 0 2
# star : 0 4
# LED : 0 8

# 序列最後一位 = 奇 or 偶
# index         1     2

# parallel port : 0 1
# number of bomb 
# number of batteries

import tkinter as tk
from tkinter.constants import FALSE, INSERT

class ComplicatedWires():
    def __init__(self):
        window = tk.Tk()
        window.title("ComplicatedWires")
        window.geometry('800x600')

        # value
        self.redvalue = tk.IntVar()
        self.bluevalue = tk.IntVar()
        self.starvalue = tk.IntVar()
        self.ledvalue = tk.IntVar()

        # check button
        cbred = tk.Checkbutton(window, text = 'red', variable=self.redvalue, onvalue = 1, offvalue = 0, command = self.callback).grid(row=0, column=0)
        cbblue = tk.Checkbutton(window, text = 'blue', variable=self.bluevalue, onvalue = 2, offvalue = 0, command = self.callback).grid(row=1, column=0)
        cbstar = tk.Checkbutton(window, text = 'star', variable=self.starvalue, onvalue = 4, offvalue = 0, command = self.callback).grid(row=2, column=0)
        cbled = tk.Checkbutton(window, text = 'led', variable=self.ledvalue, onvalue = 8, offvalue = 0, command = self.callback).grid(row=3, column=0)

        # radiobutton
        self.radioValue1 = tk.IntVar()
        self.radioValue2 = tk.IntVar()
        
        rdio11 = tk.Radiobutton(window, text = '奇', variable=self.radioValue1, value = 1, command = self.callback).grid(row=4, column=0)
        rdio12 = tk.Radiobutton(window, text = '偶', variable=self.radioValue1, value = 2, command = self.callback).grid(row=4, column=1)

        rdio11 = tk.Radiobutton(window, text = 'no parallel port', variable=self.radioValue2, value = 0, command = self.callback).grid(row=5, column=0)
        rdio12 = tk.Radiobutton(window, text = 'has paraller port', variable=self.radioValue2, value = 1, command = self.callback).grid(row=5, column=1)
        # label & entry

        lable1 = tk.Label(window, text="number of batteries:").grid(row=8,columnspan=2)
        self.entry1_txt = tk.IntVar()
        text1 = tk.Entry(window,bd=4, textvariable=self.entry1_txt)
        text1.bind("<Return>", self.bind_callback)
        text1.grid(row=8,column=2, columnspan=2)

        # label --> show result

        self.result = tk.Label(window, text="error", fg="red", font=56)
        self.result.grid(row=11, column=3)

        window.mainloop()

    def callback(self):
        self.process()

    def bind_callback(self, event):
        self.process()

    def process(self):
        sum = self.redvalue.get() + self.bluevalue .get()+ self.starvalue.get() + self.ledvalue.get()
        number_of_batteries = self.entry1_txt.get()
        even = self.radioValue1.get()
        has_parallel = self.radioValue2.get()
        if sum == 0 or sum == 4 or sum == 5:
            self.result.configure(text='cut the wire')
        elif sum == 6 or sum == 7 or sum == 8 or sum == 15:
            self.result.configure(text='do not cut the wire')
        elif sum == 1 or sum == 2 or sum == 3 or sum == 11:
            print('s') # debug
            if even == 2:
                self.result.configure(text='cut the wire')
            else:
                self.result.configure(text='do not cut the wire')
        elif sum == 10 or sum == 14:
            print('p') # debug
            if has_parallel == 1:
                self.result.configure(text='cut the wire')
            else:
                self.result.configure(text='do not cut the wire')
        elif sum == 9 or sum == 12 or sum == 13:
            print('b') # debug
            if number_of_batteries > 1:
                self.result.configure(text='cut the wire')
            else:
                self.result.configure(text='do not cut the wire')
        return 0


ComplicatedWires()