import tkinter as tk
from tkinter.constants import FALSE, INSERT

red_list = ['error','C','B','A','A,C','B','A,C','A,B,C','A,B','B']
blue_list = ['error','B','A,C','B','A','B','B,C','C','A,C','A']
black_list = ['error','A,B,C','A,C','B','A,C','B','B,C','A,B','C','C']

class Wire_sequences():
    def __init__(self):
        window = tk.Tk()
        window.title("wire_sequences")
        window.geometry('300x100')

        # value
        self.red_num = 0
        self.blue_num = 0
        self.black_num = 0

        # label
        red = tk.Label(window, text="red number:")
        red.grid(row=0, column=2)
        self.red_num_show = tk.Label(window, text =[self.red_num])
        self.red_num_show.grid(row=0,column=3,sticky='w')
        
        blue = tk.Label(window, text="blue number:")
        blue.grid(row=1, column=2)
        self.blue_num_show = tk.Label(window, text =[self.blue_num])
        self.blue_num_show.grid(row=1,column=3,sticky='w')
        
        black = tk.Label(window, text="black number:")
        black.grid(row=2, column=2)
        self.black_num_show = tk.Label(window, text =[self.black_num])
        self.black_num_show.grid(row=2,column=3,sticky='w')

        # button
        red_button_add = tk.Button(window, text='+', command=self.callback_redba)
        red_button_add.grid(row=0,column=0)
        red_button_minus = tk.Button(window, text='-', command=self.callback_redbm)
        red_button_minus.grid(row=0,column=1)
        
        blue_button_add = tk.Button(window, text='+', command=self.callback_blueba)
        blue_button_add.grid(row=1,column=0)
        blue_button_minus = tk.Button(window, text='-', command=self.callback_bluebm)
        blue_button_minus.grid(row=1,column=1)

        black_button_add = tk.Button(window, text='+', command=self.callback_blackba)
        black_button_add.grid(row=2,column=0)
        black_button_minus = tk.Button(window, text='-', command=self.callback_blackbm)
        black_button_minus.grid(row=2,column=1)

        # label show result
        self.red_result = tk.Label(window, text="error")
        self.red_result.grid(row=0, column=4, sticky='w')
        
        self.blue_result = tk.Label(window, text="error")
        self.blue_result.grid(row=1, column=4, sticky='w')

        self.black_result = tk.Label(window, text="error")
        self.black_result.grid(row=2, column=4, sticky='w')

        window.mainloop()

    def callback_redba(self):
        self.red_num += 1
        self.red_num_show.configure(text=[self.red_num])
        self.process()
    def callback_redbm(self):
        self.red_num -= 1
        self.red_num_show.configure(text=[self.red_num])
        self.process()
    
    def callback_blueba(self):
        self.blue_num += 1
        self.blue_num_show.configure(text=[self.blue_num])
        self.process()
    def callback_bluebm(self):
        self.blue_num -= 1
        self.blue_num_show.configure(text=[self.blue_num])
        self.process()

    def callback_blackba(self):
        self.black_num += 1
        self.black_num_show.configure(text=[self.black_num])
        self.process()
    def callback_blackbm(self):
        self.black_num -= 1
        self.black_num_show.configure(text=[self.black_num])
        self.process()

    def process(self):
        self.red_result.configure(text=[red_list[self.red_num]])
        self.blue_result.configure(text=[blue_list[self.blue_num]])
        self.black_result.configure(text=[black_list[self.black_num]])
        

   

Wire_sequences()