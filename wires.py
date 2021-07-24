# define
# color 無、紅、白、藍、黑、黃
# index 0   1  2   3   4  5

# 序列最後一位 = 奇 or 偶
# index         1     2

import tkinter as tk
from tkinter.constants import FALSE, INSERT
from typing import Sized, Text

class Wires():
    def __init__(self):
        window = tk.Tk()
        window.title("wires")
        window.geometry('800x600')

        # value
        self.radioValue1 = tk.IntVar()
        self.radioValue2 = tk.IntVar()
        self.radioValue3 = tk.IntVar()
        self.radioValue4 = tk.IntVar()
        self.radioValue5 = tk.IntVar()
        self.radioValue6 = tk.IntVar()

        self.radioValue7 = tk.IntVar()

        # list
        self.radioValue_list = []
        self.radioValue_list.append(self.radioValue1)
        self.radioValue_list.append(self.radioValue2)
        self.radioValue_list.append(self.radioValue3)
        self.radioValue_list.append(self.radioValue4)
        self.radioValue_list.append(self.radioValue5)
        self.radioValue_list.append(self.radioValue6)

        # radiobutton
        rdio11 = tk.Radiobutton(window, text = '無', variable=self.radioValue1, value = 0, command = self.callback).grid(row=0, column=0)
        rdio12 = tk.Radiobutton(window, text = '紅', variable=self.radioValue1, value = 1, command = self.callback).grid(row=0, column=1)
        rdio13 = tk.Radiobutton(window, text = '白', variable=self.radioValue1, value = 2, command = self.callback).grid(row=0, column=2)
        rdio14 = tk.Radiobutton(window, text = '藍', variable=self.radioValue1, value = 3, command = self.callback).grid(row=0, column=3)
        rdio15 = tk.Radiobutton(window, text = '黑', variable=self.radioValue1, value = 4, command = self.callback).grid(row=0, column=4)
        rdio16 = tk.Radiobutton(window, text = '黃', variable=self.radioValue1, value = 5, command = self.callback).grid(row=0, column=5)

        rdio21 = tk.Radiobutton(window, text = '無', variable=self.radioValue2, value = 0, command = self.callback).grid(row=1, column=0)
        rdio22 = tk.Radiobutton(window, text = '紅', variable=self.radioValue2, value = 1, command = self.callback).grid(row=1, column=1)
        rdio23 = tk.Radiobutton(window, text = '白', variable=self.radioValue2, value = 2, command = self.callback).grid(row=1, column=2)
        rdio24 = tk.Radiobutton(window, text = '藍', variable=self.radioValue2, value = 3, command = self.callback).grid(row=1, column=3)
        rdio25 = tk.Radiobutton(window, text = '黑', variable=self.radioValue2, value = 4, command = self.callback).grid(row=1, column=4)
        rdio26 = tk.Radiobutton(window, text = '黃', variable=self.radioValue2, value = 5, command = self.callback).grid(row=1, column=5)

        rdio31 = tk.Radiobutton(window, text = '無', variable=self.radioValue3, value = 0, command = self.callback).grid(row=2, column=0)
        rdio32 = tk.Radiobutton(window, text = '紅', variable=self.radioValue3, value = 1, command = self.callback).grid(row=2, column=1)
        rdio33 = tk.Radiobutton(window, text = '白', variable=self.radioValue3, value = 2, command = self.callback).grid(row=2, column=2)
        rdio34 = tk.Radiobutton(window, text = '藍', variable=self.radioValue3, value = 3, command = self.callback).grid(row=2, column=3)
        rdio35 = tk.Radiobutton(window, text = '黑', variable=self.radioValue3, value = 4, command = self.callback).grid(row=2, column=4)
        rdio36 = tk.Radiobutton(window, text = '黃', variable=self.radioValue3, value = 5, command = self.callback).grid(row=2, column=5)

        rdio41 = tk.Radiobutton(window, text = '無', variable=self.radioValue4, value = 0, command = self.callback).grid(row=3, column=0)
        rdio42 = tk.Radiobutton(window, text = '紅', variable=self.radioValue4, value = 1, command = self.callback).grid(row=3, column=1)
        rdio43 = tk.Radiobutton(window, text = '白', variable=self.radioValue4, value = 2, command = self.callback).grid(row=3, column=2)
        rdio44 = tk.Radiobutton(window, text = '藍', variable=self.radioValue4, value = 3, command = self.callback).grid(row=3, column=3)
        rdio45 = tk.Radiobutton(window, text = '黑', variable=self.radioValue4, value = 4, command = self.callback).grid(row=3, column=4)
        rdio46 = tk.Radiobutton(window, text = '黃', variable=self.radioValue4, value = 5, command = self.callback).grid(row=3, column=5)

        rdio51 = tk.Radiobutton(window, text = '無', variable=self.radioValue5, value = 0, command = self.callback).grid(row=4, column=0)
        rdio52 = tk.Radiobutton(window, text = '紅', variable=self.radioValue5, value = 1, command = self.callback).grid(row=4, column=1)
        rdio53 = tk.Radiobutton(window, text = '白', variable=self.radioValue5, value = 2, command = self.callback).grid(row=4, column=2)
        rdio54 = tk.Radiobutton(window, text = '藍', variable=self.radioValue5, value = 3, command = self.callback).grid(row=4, column=3)
        rdio55 = tk.Radiobutton(window, text = '黑', variable=self.radioValue5, value = 4, command = self.callback).grid(row=4, column=4)
        rdio56 = tk.Radiobutton(window, text = '黃', variable=self.radioValue5, value = 5, command = self.callback).grid(row=4, column=5)

        rdio61 = tk.Radiobutton(window, text = '無', variable=self.radioValue6, value = 0, command = self.callback).grid(row=5, column=0)
        rdio62 = tk.Radiobutton(window, text = '紅', variable=self.radioValue6, value = 1, command = self.callback).grid(row=5, column=1)
        rdio63 = tk.Radiobutton(window, text = '白', variable=self.radioValue6, value = 2, command = self.callback).grid(row=5, column=2)
        rdio64 = tk.Radiobutton(window, text = '藍', variable=self.radioValue6, value = 3, command = self.callback).grid(row=5, column=3)
        rdio65 = tk.Radiobutton(window, text = '黑', variable=self.radioValue6, value = 4, command = self.callback).grid(row=5, column=4)
        rdio66 = tk.Radiobutton(window, text = '黃', variable=self.radioValue6, value = 5, command = self.callback).grid(row=5, column=5)

        rdio71 = tk.Radiobutton(window, text = '奇數', variable=self.radioValue7, value = 1, command = self.callback).grid(row=6, column=0)
        rdio72 = tk.Radiobutton(window, text = '偶數', variable=self.radioValue7, value = 2, command = self.callback).grid(row=6, column=1)

        # label --> show line color

        self.line1 = tk.Label(window, text="--------------------------", bg='gray95')
        self.line1.grid(row=0, column=7, columnspan=20)

        self.line2 = tk.Label(window, text="--------------------------", bg='gray95')
        self.line2.grid(row=1, column=7, columnspan=20)

        self.line3 = tk.Label(window, text="--------------------------", bg='gray95')
        self.line3.grid(row=2, column=7, columnspan=20)

        self.line4 = tk.Label(window, text="--------------------------", bg='gray95')
        self.line4.grid(row=3, column=7, columnspan=20)

        self.line5 = tk.Label(window, text="--------------------------", bg='gray95')
        self.line5.grid(row=4, column=7, columnspan=20)

        self.line6 = tk.Label(window, text="--------------------------", bg='gray95')
        self.line6.grid(row=5, column=7, columnspan=20)

        self.line_list = []
        self.line_list.append(self.line1)
        self.line_list.append(self.line2)
        self.line_list.append(self.line3)
        self.line_list.append(self.line4)
        self.line_list.append(self.line5)
        self.line_list.append(self.line6)

        # label --> show result

        self.result = tk.Label(window, text="error", fg="red", font=56)
        self.result.grid(row=10, column=8)
        # candidate line

        self.candidate = 0
        self.candidates = [] 

        window.mainloop()

    def callback(self):
        self.process()

    def three_lines(self):
        print(self.candidates)
        red_line = 0
        blue_line = 0
        for canditate in self.candidates:
            if canditate[1] == 1:
                red_line += 1
            elif canditate[1] == 3:
                blue_line += 1

        if red_line == 0:
            return self.result.configure(text="cut 2 line")
        elif self.candidates[2][1] == 2:
            return self.result.configure(text="cut last line")
        elif blue_line > 1:
            return self.result.configure(text="cut last blue line")
        else:
            return self.result.configure(text="cut last line")
    
    def four_lines(self):
        print(self.candidates)
        red_line = 0
        blue_line = 0
        yellow_line = 0
        for canditate in self.candidates:
            if canditate[1] == 1:
                red_line += 1 
            elif canditate[1] == 3:
                blue_line += 1
            elif canditate[1] == 5:
                yellow_line += 1
        
        if red_line > 1 and self.radioValue7.get() == 1:
            return self.result.configure(text="cut last red line")
        elif red_line == 0 and self.candidates[3][1] == 5:
            return self.result.configure(text="cut first line")
        elif blue_line == 1:
            return self.result.configure(text="cut first line")
        elif yellow_line > 1:
            return self.result.configure(text="cut last line")
        else:
            return self.result.configure(text="cut second line")


    def five_lines(self):
        print(self.candidates)
        red_line = 0
        black_line = 0
        yellow_line = 0
        for canditate in self.candidates:
            if canditate[1] == 1:
                red_line += 1 
            elif canditate[1] == 4:
                black_line += 1
            elif canditate[1] == 5:
                yellow_line += 1

        if self.candidates[4][1] == 4 and self.radioValue7.get() == 1:
            return self.result.configure(text="cut forth line")
        elif red_line == 1 and yellow_line > 1:
            return self.result.configure(text="cut first line")
        elif black_line == 0:
            return self.result.configure(text="cut second line")
        else:
            return self.result.configure(text="cut first line")
    def six_lines(self):
        print(self.candidates)
        red_line = 0
        white_line = 0
        yellow_line = 0
        for canditate in self.candidates:
            if canditate[1] == 1:
                red_line += 1 
            elif canditate[1] == 2:
                white_line += 1
            elif canditate[1] == 5:
                yellow_line += 1

        if yellow_line == 0 and self.radioValue7.get() == 1:
            return self.result.configure(text="cut third line")
        elif yellow_line == 1 and  white_line > 1:
            return self.result.configure(text="cut forth line")
        elif red_line == 0:
            return self.result.configure(text="cut last line")
        else:
            return self.result.configure(text="cut forth line")

    def process(self):
        index = 0
        self.candidate = 0
        self.candidates.clear()
        for i in self.radioValue_list:
            self.candidate += 1
            if i.get() != 0:
                self.candidates.append([self.candidate, i.get()])
                index += 1
        self.process_line()
        self.num_to_func(index)

    def process_line(self):
        print(self.candidates)
        # default line
        self.line1.configure(bg="gray95")
        self.line2.configure(bg="gray95")
        self.line3.configure(bg="gray95")
        self.line4.configure(bg="gray95")
        self.line5.configure(bg="gray95")
        self.line6.configure(bg="gray95")
        for i in self.candidates:
            if i[0] == 1:
                self.process_color(i)
            elif i[0] == 2:
                self.process_color(i)
            elif i[0] == 3:
                self.process_color(i)
            elif i[0] == 4:
                self.process_color(i)
            elif i[0] == 5:
                self.process_color(i)
            elif i[0] == 6:
                self.process_color(i)
    
    def process_color(self,i):
        if i[1] == 1:
            self.line_list[i[0]-1].configure(bg="red")
        elif i[1] == 2:
            self.line_list[i[0]-1].configure(bg="white")
        elif i[1] == 3:
            self.line_list[i[0]-1].configure(bg="blue")
        elif i[1] == 4:
            self.line_list[i[0]-1].configure(bg="black")
        elif i[1] == 5:
            self.line_list[i[0]-1].configure(bg="yellow")

    def num_to_func(self,num):
        numbers = {
            3 : self.three_lines,
            4 : self.four_lines,
            5 : self.five_lines,
            6 : self.six_lines
        }

        func = numbers.get(num, lambda: "Invalid lines")
        func()

    
    

Wires()